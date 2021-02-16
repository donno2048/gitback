# gitback
Makes a backup of all your repositories and gists from GitHub
# install
From Pypi:

`python -m pip install gitback`

From GitHub:

`python -m pip install git+https://github.com/donno2048/gitback`
# Usage
```
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
  -p, --password    Your GitHub password
  -r, --repos       Backup only repos
  -g, --gists       Backup only gists
```
