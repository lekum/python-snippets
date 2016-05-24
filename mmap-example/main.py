import os
import mmap

def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)

if __name__ == '__main__':
    f = open("data", "wb")
    for i in range(100):
        f.write(b'\xf0')
    f.close()
    with memory_map("data") as m:
        s = "This is l33t".encode()
        m[:len(s)] = s
