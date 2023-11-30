#!/usr/bin/python3
print(bytes(range(65, 91)).translate(bytes.maketrans(b"", b""), b"\n").decode())
