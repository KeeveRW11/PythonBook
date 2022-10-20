#SYS
# import sys

# print("hello, my name is", sys.argv[1])
#IndexError: list index out of range - how do we fix this? with an exception

# import sys

# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")

# import sys

# if len(sys.argv) <2:
#     print("Too few arguments")
# elif len(sys.argv) >2:
#     print("Too many arguments")
# else:
#     print("hello, my name is", sys.argv[1])

# import sys

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")
# print("hello, my name is", sys.argv[1])

#: colon gives slice of list -1 remove oe from list
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
for arg in sys.argv[1:-1]:
    print("hello, my name is", arg)
