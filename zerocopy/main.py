def send_from(arr, dest):
    view = memoryview(arr).cast('B')
    while len(view):
        nsent = dest.send(view)
        view = view[nsent:]

def recv_into(arr, source):
    view = memoryview(arr)
    while len(view):
        ncev = source.recv_into(view)
        view = view[nrecv:]
