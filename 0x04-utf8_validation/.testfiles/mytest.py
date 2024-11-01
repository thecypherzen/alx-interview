#!/usr/bin/env python3

import sys
if len(sys.argv) < 2:
    sys.exit(1)

num = int(sys.argv[1])

print("%d in binary is: %s" % (num, bin(num)))
print(format(num,'b'))
print("%x" % 255)
