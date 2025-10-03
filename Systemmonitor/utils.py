import sys

def gb(b):
    return b/1024**3

def press():
    input("\nTryck Enter för att fortsätta...")

def clr_line():
    sys.stdout.write("\r")
    sys.stdout.write(" " * 120)
    sys.stdout.write("\r")
    sys.stdout.flush()
