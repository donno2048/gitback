from os import chdir, mkdir, rmdir, getcwd
from os.path import exists
from subprocess import Popen, PIPE
from shutil import make_archive
from argparse import ArgumentParser
from urllib.request import urlopen
from json import loads
def backup()->None:
    parser = ArgumentParser(description='Makes a backup of all your repositories and gists from GitHub')
    parser.add_argument('-n', '--name', metavar='', type=str, help='Use a custom name for your backup [default: backup]')
    parser.add_argument('-P', '--path', metavar='', type=str, help='Use a custom path for your backup [default: current working directory]')
    parser.add_argument('-s', '--ssh', action='store_true', help='Use ssh cloning [default: http]')
    parser.add_argument('-f', '--full', action='store_true', help='Clone with full git history')
    parser.add_argument('-z', '--zip', action='store_true', help='Make a zip file of the backup')
    parser.add_argument('-q', '--quiet', action='store_true', help='Don\'t see cloning progress')
    parser.add_argument('-u', '--username', metavar='', type=str, help='Your GitHub username')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-r', '--repos', action='store_true', help='Backup only repos')
    group.add_argument('-g', '--gists', action='store_true', help='Backup only gists')
    args = parser.parse_args()
    if args.path is not None: chdir(args.path)
    username, git_command = args.username if args.username is not None else input("Your GitHub username: "), ' clone '
    name = 'backup' if args.name is None else args.name
    if exists(name + '.zip') and args.zip: exit(f'You already have a {name} zip, please move it somewhere else until the process is done')
    try: mkdir(name)
    except FileExistsError:
        try:
            rmdir(name)
            mkdir(name)
        except OSError: exit(f'You already have a {name} folder, please move it somewhere else until the process is done')
    chdir(name)
    if not args.full: git_command += '--depth 1 '
    if args.quiet: git_command += '-q '
    repo_clone_command = 'https://github.com/' if not args.ssh else 'git@github.com:'
    gist_clone_command = 'https://gist.github.com/' if not args.ssh else 'git@gist.github.com:'
    if not args.repos:
        i = 0
        while len(result := loads(urlopen(f"https://api.github.com/users/{username}/gists?type=all&per_page=100&page={i}").read())):
            for gist in result:
                Popen('git' + git_command + gist_clone_command + gist["id"], shell = True, stdout = PIPE).wait()
            i += 1
    if not args.gists:
        i = 0
        while len(result := loads(urlopen(f"https://api.github.com/users/{username}/repos?type=all&per_page=100&page={i}").read())):
            for repo in result:
                Popen('git' + git_command + repo_clone_command + repo["full_name"], shell = True, stdout = PIPE).wait()
            i += 1
    chdir('..')
    make_archive(name, 'zip', name)
