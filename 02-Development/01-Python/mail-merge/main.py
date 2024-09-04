PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as template_letter:
    letter_contents = template_letter.read()

    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open("./Output/ReadyToSend/" + stripped_name + ".txt", mode="w") as letter_to_send:
            letter_to_send.write(new_letter)
