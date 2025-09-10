questions = ("How many elements are in the periodic table?: ",
            "Which animal lays are largest eggs?: ",
            "What is the most abundant gas in Earth's atmosphere?: ",
            "How many bones are in the human body?: ",
            "Which planet in the solar system in the hottest?: ")


options = (("A. 116","B. 118","C. 189","D. 106"),
           ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
           ("A. Nitrogen","B. Oxygen","C. Carbon-Dioxide","D. Hydrogen"),
           ("A. 206","B. 207","C. 208","D. 209"),
           ("A. Venus","B. Mercury","C. Earth","D. Mars"))



answers = ("B","D","A","A","A")
guesses = []  
score = 0
question_num = 0

for question in questions:
    print("----------------------------")
    print(question) 
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")    
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1


print("----------------------------")
print("           RESULT           ")
print("----------------------------")    


print("answer: ",end="")
for answer in answers:
    print(answer, end=" ")
print() 


print("guesses: ",end="")
for guess in guesses:
    print(guess, end=" ")
print() 



score = (score / len(questions) * 100)
print(f"Your score is: {score}%")


if score < 40 :
    print("FINAL GRADE-->Fail!!!")
else:
    print("FINAL GRADE-->Pass!!!")    