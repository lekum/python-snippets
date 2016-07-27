import os
import time

def modified_within(top, seconds):
    now = time.time()
    for relpath, dirs, files in os.walk(top):
        for name in files:
            fullpath = os.path.join(top, relpath, name)
            if os.path.exists(fullpath):
                mtime = os.path.getmtime(fullpath)
                if mtime > (now - seconds):
                    print(fullpath)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print('Usage: {} dir seconds'.format(sys.argv[0]))
        raise SystemExit(1)

    modified_within(sys.argv[1], float(sys.argv[2]))
