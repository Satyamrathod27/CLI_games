def new_game():
    guesses = []
    correct_guesses = 0
    questions_num = 1

    for key in questions:
        print(key)
        for i in options[questions_num - 1]:
            print(i)
        guess = input("Enter A,B,C,D:").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        questions_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong")
        return 0


def display_score(correct_guesses, guesses):
    print("--------------------------------")
    print("Results:")
    print("--------------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end="")
    for i in guesses:
        print(i, end="")

    score = int((correct_guesses / len(questions)) * 100)
    print("your score is : " + str(score) + "%")


def play_again():
    response = input("do you want to play more?(yes/no): ").upper()
    if response == "YES":
        return True
    else:
        return False


questions = {
    "who created python?:": "A",
    "what year was python created?:": "D",
    "python is tributed to which comedy group?:": "C",
    "is the earth round?:": "A"
}

options = [["A.guido van rossum", "B.Elon musk", "C.sam altman", "D.Jeff bezos"],
           ["A.1999", "B.2002", "C.2003", "D.1991"],
           ["A.Lonely island", "B.smosh", "C.monty python", "D.SNL"],
           ["A.Yes", "B.No", "C.dont know", "D.its flat"]]

while play_again():
    new_game()

print("Okay Bye!!")