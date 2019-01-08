# initialize.py
# Dave's initialization file for Python interactive sessions.

import sys, os, readline, pprint

histfile = os.path.join(os.environ["HOME"], ".pyhist")
try:
    readline.read_history_file(histfile)
except IOError:
    pass
import atexit
atexit.register(readline.write_history_file, histfile)
del os, histfile


try:
    import readline
except ImportError:
    print("Module readline not available.")
else:
    import rlcompleter
    readline.parse_and_bind("tab: complete")


# https://twitter.com/nedbat/status/817827164443840512
sys.displayhook = pprint.pprint
