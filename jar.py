def main():
    size = input("Size for the jar? ")
    print(jar(size))


def jar(size):
    while True:
        try:
            size = int(size)
        except ValueError:
            return "Size cannot be a string"
        else:
            if size < 0:
                return "Size cannot be negative"
            else:
                break

    return f"Okay, I created a size {size} jar!"
    

if __name__ == "__main__":
    main()
