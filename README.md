# gitback
Makes a backup of all your repositories and gists from GitHub

## Install

### From PyPI

`pip3 install gitback`

### From GitHub

`pip3 install git+https://github.com/donno2048/gitback`

## Usage

```py
usage: gitback [-h] [-n] [-P] [-s] [-f] [-z] [-q] [-u] [-p]  [-r | -g]

Makes a backup of all your repositories and gists from GitHub

optional arguments:
  -h, --help        show this help message and exit
  -n, --name        Use a custom name for your backup [default: backup]
  -P, --path        Use a custom path for your backup [default: current working directory]
  -s, --ssh         Use ssh cloning [default: http]
  -f, --full        Clone with full git history
  -z, --zip         Make a zip file of the backup
  -q, --quiet       Don't see cloning progress
  -u, --username    Your GitHub username
  -r, --repos       Backup only repos
  -g, --gists       Backup only gists
```

### Example

Let's say I want to backup only my gists, and I want a zip file:

```sh
gitback -u donno2048 -g -z
```
