from struct import Struct

def write_records(records, format, f):
    """
    Write a sequence of iterables to a binary file
    """
    record_struct = Struct(format)
    for rec in records:
        f.write(record_struct.pack(*rec))

def unpack_records(format, data):
    """
    Yield the records contained in a binary string
    """
    record_struct = Struct(format)
    for offset in range(0, len(data), record_struct.size):
        yield record_struct.unpack_from(data, offset)

if __name__ == '__main__':

    records = [ [1, 2.3, 4.5],
                (6, 7.8, 9.0),
                (12, 13.4, 56.7) ]

    with open('data.b', 'wb') as f:
        write_records(records, '<idd', f)
    with open('data.b', 'rb') as f:
        data = f.read()
    for rec in unpack_records('<idd', data):
        print(rec)
