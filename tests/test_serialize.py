import os
import io
import pywasm
from pywasm import num, common

PATH = os.path.dirname(__file__)

f = os.path.join(PATH, "../examples/add.wasm")
f = open(f, "rb")
m = pywasm.structure.Module.from_reader(f)

outf = io.BytesIO()
m.to_writer(outf)

"""

w = io.BytesIO()

for n in [0, 1, 5, 100, 127, 128, 200, 255, 256, 1024, 2043, 10000, 40000, 66000]:

    for signed in (True, False):
        curn = -n if signed else n

        w.seek(0)
        common.write_count(w, curn)
        w.seek(0)
        _n = common.read_count(w, signed=signed)

        if _n != curn:
            print("failed for n=%d, signed=%s. got _n=%d" % (curn, signed, _n))
        else:
            print("success for n=%d, signed=%s" % (curn, signed))
"""
