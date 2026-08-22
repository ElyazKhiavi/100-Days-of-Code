# 1.TODO: Create a letter using starting_letter.txt done
# for each name in invited_names.txt done
# Replace the [name] placeholder with the actual name. done
# Save the Letters in the folder "ReadyToSend". done


def main():
    with open("./input/letters/starting_letter.txt", "r") as f:
        letter = f.read().strip()

    with open("./input/names/invited_names.txt", "r") as f:
        names = f.readlines()
    sender = (input("Enter Sender Name: ")).strip().title()
    for n in names:
        name = n.replace("\n", "").strip()
        new_letter = letter.replace("[name]", name).replace("[sender]", sender)
        new_letter_name = f"letter_to_{name}.txt"
        with open(f"./output/{new_letter_name}", "w") as f:
            f.write(new_letter)
            print(f"Created {new_letter_name}")


if __name__ == "__main__":
    main()
