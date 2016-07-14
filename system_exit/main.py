import sys
import getpass

if __name__ == '__main__':

    if len(sys.argv) < 2:
        raise SystemExit("Usage: python main.py arg1 arg2 ...")
    print("Everything right!")
    user = getpass.getuser()
    passwd = getpass.getpass()
    print("User:", user, "Password:", passwd)
