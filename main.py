#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Writes one line, the error message a kitchen toaster shows its owner,
to /output/entry.txt. Deterministic: no network, no randomness, no input,
no environment, no secrets. Gate: 1-120 UTF-8 characters, not only whitespace.
"""
import os

ENTRY = "Error 0x1EAF: Your breakfast is stuck inside me. I have opened a ticket. I am also the ticket."

assert 1 <= len(ENTRY) <= 120, f"entry length {len(ENTRY)} outside 1-120"
assert ENTRY.strip(), "entry is only whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)

with open("/output/entry.txt", encoding="utf-8") as f:
    written = f.read()

assert written == ENTRY, "re-read mismatch"
print(ENTRY)
