
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response
        else:
            print("Please answer with yes/no or y/n")

def instructions():
    print("**** How to play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""

played_before = yes_no("Have you played this game before? ")


if played_before == "no":
    instructions()

print("Program continues")

