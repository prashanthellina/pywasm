import os
import io
import pywasm
from pywasm import num, common

"""
PATH = os.path.dirname(__file__)

f = os.path.join(PATH, "../examples/add.wasm")
f = open(f, "rb")
m = pywasm.structure.Module.from_reader(f)

outf = io.BytesIO()
m.to_writer(outf)
"""

w = io.BytesIO()

for n in [0, 1, 5, 100, 127, 128, 200, 255, 256, 1024, 2043, 10000,
    40000, 66000]:
    w.seek(0)
    common.write_count(w, n)
    w.seek(0)
    _n = common.read_count(w)
    assert _n == n
