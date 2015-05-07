#!/usr/bin/env python
# Filter out only matching files from preprocessor output
# Omit blank lines

import re, sys
comment = re.compile(r'^# (?P<lineno>\d+) "(?P<filename>[^\"]+)"')

allowed_filenames = re.compile(".*(stdin|SDL_.*)")

filename = ""
allowed = True
for line in sys.stdin:
    match = comment.match(line)
    if match:
        filename = match.group('filename')
        allowed = bool(allowed_filenames.match(filename))
    if not line.strip():
        continue
    if not allowed:
        continue
    if line[0] == "#":
        continue
    sys.stdout.write(line)

