#!/usr/bin/env python3

import sys
args = sys.argv[1:]          # Skip the first element in sys.argv.
                             # It's the script name, which we usually don't care about.
i = 0
while i < len(args):
   print("i now = ", i)
   print("argv[i] now = ", args[i])
   print()
   i = i + 1
