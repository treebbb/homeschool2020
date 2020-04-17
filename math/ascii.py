import sys

def main():
    args = sys.argv
    argv = args[0]
    myst = args[1]
    print(myst)
    for c in myst:
        print(hex(ord(c)))

main()
