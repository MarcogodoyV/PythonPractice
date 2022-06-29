def new_game():
    
    guesses = []
    correct_guesses = 0
    current_question_number = 0

    for key in questions:
        print(key)
        for option in options[current_question_number]:
            print(option, end= ' | ')
        print('')
        guess = input('Type your answer (A,B,C,D): ').upper()
        guesses.append(guess)
        current_question_number +=1
        correct_guesses += check_answer(questions.get(key),guess)
    
    display_score(correct_guesses)
#----------------------------
def check_answer(cAnswer,guess):

    if cAnswer == guess:
        print('Correct!')
        print('#----------------------------')
        return 1
    else:
        print('Incorrect! (correct answer) : '+str(cAnswer))
        print('#----------------------------')
        return 0

#----------------------------
def  display_score(correct_guesses):
    print('You got '+str(correct_guesses)+" correct answers")
#----------------------------
def play_again():
    new_game()
    res = input('Do you want to play again? :').lower()
    if res == 'yes':
        return False
    else:
        return True


questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group? :" : "C",
    "Is the earth round? :": "A"
}

options = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 1016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False", "C. Sometimes", "D. What's Earth?"]]


while not play_again():
    continue

