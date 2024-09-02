import sys


def main():
    size = input("Size for the jar? ")
    print(jar(size))


def jar(size):
    try:
        size = int(size)
    except ValueError:
        sys.exit("Size can't be a string")
    if size < 0:
        sys.exit("Size can't be negative")
    return f"Okay, I created a size {size} jar!"
    

if __name__ == "__main__":
    main()
