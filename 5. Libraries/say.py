# import cowsay
# import sys

# if len(sys.argv) == 2:
#     cowsay.trex("hello, " + sys.argv[1])

import sys
#import from sayings.py
from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])

