
show_instructions = ""

while show_instructions != "xxx":
    show_instructions = input("Have you played Lucky Unicorn before").lower()

    if show_instructions == "no" or show_instructions == "n":
        print("Display instructions ")
    elif show_instructions == "yes" or show_instructions == "y":
        print("program continues")
    else:
        print("Please enter yes or no :) ")
