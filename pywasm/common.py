from pywasm import num


def read_count(reader, maxbits=32, signed=False) -> int:
    return num.leb_decode(reader, maxbits, signed)[1]


def read_bytes(reader, maxbits=32, signed=False) -> bytearray:
    n = read_count(reader, maxbits, signed)
    return bytearray(reader.read(n))


def write_count(writer, n: int, maxbits=32):
    return num.leb_encode(writer, n, maxbits)


def write_bytes(writer, data: bytearray, maxbits=32, signed=False):
    n = len(data)
    n += write_count(w, len(data), maxbits)
    writer.write(data)
    return n
