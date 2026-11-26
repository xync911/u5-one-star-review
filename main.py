"""Copy entry.txt to the output directory for the make.fun entry.

The entry is one single-line one-star review, at most 160
characters, of an everyday essential everyone relies on.
The sun rises at 5 a.m. with no snooze button, no off switch,
and no apology. A deadpan complaint filed in earnest against
a thing that cannot be fixed — and would not listen anyway.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
# The entry text is copied verbatim; the judge reads it exactly as written.
# Verify the copy is byte-identical to the source.
assert open(SRC, "rb").read() == open(OUT, "rb").read(), "output differs from entry.txt"
