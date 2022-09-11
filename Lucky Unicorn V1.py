

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


how_much = num_check("How much would you like to pay with? ", 0, 10)

print("You will be spending ${}".format(how_much))
having_fun = input("Are you having fun? ")
print("you said {} to having fun".format(having_fun))
