import sys


def main():
    try:
        size = int(input("Size for the jar? "))
    except ValueError:
        sys.exit("Value can't be a string")
    if size < 0:
        sys.exit("Size can't be negetive")
    print(jar(size))


def jar(size):
    return f"Okay, I created a size {size} jar!"
    

if __name__ == "__main__":
    main()
