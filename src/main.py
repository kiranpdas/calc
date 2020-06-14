from calc import add, sub, mult, div


def main():
    x = int(input("Enter first number to add: "))
    y = int(input("Enter second number to add: "))

    sum = add(x, y)

    print("Sum is {sum}".format(sum=sum))


if __name__ == "__main__":
    main()
