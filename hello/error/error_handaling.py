def main():
    while True:
        try:
            age = int(input("Enter age:"))
            print(age * 12)
        except (ValueError, TypeError) as err:
            print(err)
        else:
            print("Bye")
            break


if __name__ == "__main__":
    main()
