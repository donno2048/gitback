from gitback import backup
from os import rmdir
if __name__ == '__main__':
    try: backup()
    except Exception: rmdir("backup")