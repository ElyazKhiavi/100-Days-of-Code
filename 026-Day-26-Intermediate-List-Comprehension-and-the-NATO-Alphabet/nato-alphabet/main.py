import pandas as pd

data = pd.read_csv("./nato_phonetic_alphabet.csv")
nato = {row.letter: row.code for (i, row) in data.iterrows()}
# print(nato)


def main():
    while True:
        while True:
            user_input = input("Please enter work: ").strip().upper()
            if user_input:
                break
            print("Input can not be empty!")
        phonetic_code_list = [
            nato[letter.upper()] for letter in user_input if letter in nato
        ]
        print(phonetic_code_list)
        again = input("Have any other words? (y/n)").lower().strip()
        if again != "y":
            return
        print("Goodbye.")


if __name__ == "__main__":
    main()
    #usual 
