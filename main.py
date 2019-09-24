from time import sleep


def main(x: int, y: int):
    print("You entered " + str(x))
    sleep(1)
    print("\n")
    print(("In 100 years you will be " + str((x + 100)) + " years old! \n") * y)


main(int(input("Please enter your age below.\n")), int(input("Now please enter a random number! \n")))
