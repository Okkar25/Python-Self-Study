def sentencesByLength(filename):
    with open(filename, "r") as file:
        content = file.read().replace("\n", " ").split(".")
        content = [sentence.strip() + "." for sentence in content if sentence != " "]

        # return content

        sentence_dict = {}

        for sentence in content:
            words_count = len(sentence.split(" "))

            if words_count in sentence_dict:
                sentence_dict[words_count].append(sentence)
            else:
                sentence_dict[words_count] = [sentence]

        return sentence_dict


# print(sentencesByLength("sentences1.txt"))


import random

random.seed(0)


class RandomCode:

    def __init__(self, length, char_list):
        # self.length = length
        # self.char_list = char_list
        # self.secret_code = "".join(random.choices(self.char_list, k=self.length))

        self.secret_code = "".join([random.choice(char_list) for i in range(length)])

    def __repr__(self):
        # secret_code = "".join(random.choices(self.char_list, k=self.length))
        # return f"RandomCode('{secret_code}')"
        return f"RandomCode('{self.secret_code}')"

    def getSecret(self):
        # return repr(self)[12:-2]
        return self.secret_code

    def getHint(self):
        # return "?" * self.length
        return "?" * len(self.secret_code)

    def correct(self, guess):
        return self.getSecret() == guess

    def correctPositions(self, guess_positions):
        correct_number = 0
        # for i in range(len(guess_positions)):
        for i in range(len(self.secret_code)):  # fix index out of range error
            if self.secret_code[i] == guess_positions[i]:
                correct_number += 1
        return correct_number

        # return sum([ guess_positions[i] == self.secret_code[i] for i in range(min(len(self.secret_code), len(guess_positions))) ])

    def correctLetters(self, guess_letters):  # ABEF
        guess_letters_list = list(guess_letters)
        correct_char = 0

        for i in range(len(self.secret_code)):  # FECB ["A", "B", "E", "F"]
            if self.secret_code[i] in guess_letters_list:
                guess_letters_list.pop(guess_letters_list.index(self.secret_code[i]))
                correct_char += 1

        return correct_char

        # return sum([min(self.secret_code.count(letter), guess_letters.count(letter)) for letter in set(self.secret_code) ])


# code = RandomCode(4, "ABCDEF")
# code = RandomCode(8, "AB")

# print(code)
# print(code.getSecret())
# print(code.getHint())
# print(code.correct("DDAC"))
# print(code.correctPositions("DDCA"))
# print(code.correctLetters("DAAC"))

# print("A" in ["A", "B"])
# print(["A", "B", "C"].pop())


import random

# random.seed(7)
random.seed(8)


def guessCode(length, letters):
    secret = RandomCode(length, letters)

    print(f"Try to guess my secret code: {secret.getHint()} (QUIT to stop)\n")
    # print(f"The secret code is {secret.getSecret()}")
    guess_count = 0

    while True:
        guess = input("What is your guess?: ")
        guess_count += 1

        if guess == "QUIT":
            guess_count -= 1
            # print(f"\nYou gave up after {guess_count} guesses. ")
            # print(f"The secret code is {secret.getSecret()}.")
            print(f"\nYou gave up after {guess_count} guesses. \nThe secret code is {secret.getSecret()}.")
            break

        elif secret.correct(guess):
            print(f"Congratulations, you got it in {guess_count} guesses!")
            break

        # elif not secret.correct(guess):
        elif guess != secret.getSecret():
            print(
                f"Your guess has {secret.correctLetters(guess)} correct letters, {secret.correctPositions(guess)} in the correct position.\n"
            )
            # guess_count += 1


# guessCode(6, "AB") # random.seed(7)
# guessCode(4, "ABCDEF")  # random.seed(8)
# guessCode(6,"ABCDEF")


if __name__ == "__main__":
    import doctest

    print(doctest.testfile("final_problemsTEST.py"))
