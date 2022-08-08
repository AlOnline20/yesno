
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "no" or response == "n":
            response = "no"
            return response

        elif response == "yes" or response == "y":
            response = "yes"
            return response

        else:
            print("Please enter yes or no :) ")


show_instructions = input("Have you played Lucky Unicorn before")

print("you chose {} ".format(show_instructions))
print()
having_fun = yes_no("Are you having fun? ")
print("you said {} to having fun".format(having_fun))
