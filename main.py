# READ Letter and Names
with open("./starting_letter.txt", "r") as start:
    text = start.read()
with open("./invited_names.txt", "r") as names_list:
    names = names_list.readlines()

# Save Letters
for n in names:
    clear_name = n.strip("\n")
    with open(f"./letter_for_{clear_name}.txt", "w") as letter:
        new_text = text.replace("[name]", clear_name)
        print(f"Letter for {clear_name} saved...")
        letter.write(new_text)
print("\nAll letters saved!")
