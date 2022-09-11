
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
def num_check(question, low, high):
    error = "Please enter an whole number between 1 and 10\n"
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if low < response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

how_much = num_check("How much would you like to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))
