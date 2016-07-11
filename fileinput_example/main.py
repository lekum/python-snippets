import fileinput

with fileinput.input('/etc/passwd') as f:
    for line in f:
        print(f.filename(), f.fileno(), line, end='')
