print("This program is an implementation of the Rosenberg Self-Esteem Scale. This program will show you ten statements that you could possibly apply to yourself. Please rate how much you agree with each of the statements by responding with one of these four letters:")
print()
print("D means you strongly disagree with the statement.")
print("d means you disagree with the statement.")
print("a means you agree with the statement.")
print("A means you strongly agree with the statement.")

score = 0
#1,2,4,6,7
def answer_pos(score):
    letter = input("Enter D, d, a, or A: ")
    if letter == "A":
        score = 3
    elif letter == "a":
        score = 2
    elif letter == "D":
        score = 0
    elif letter == "d":
        score = 1
    return score
#3,5,8,9,10
def answer_neg(score):
    letter = input("Enter D, d, a, or A: ")
    if letter == "A":
        score = 0
    elif letter == "a":
        score = 1
    elif letter == "D":
        score = 3
    elif letter == "d":
        score = 2
    return score

print("1. I feel that I am a person of worth, at least on an equal plane with others.")
score += answer_pos(score)
print("2. I feel that I have a number of good qualities.")
score += answer_pos(score)
print("3. All in all, I am inclined to feel that I am a failure.")
score += answer_neg(score)
print("4. I am able to do things as well as most other people.")
score += answer_pos(score)
print("5. I feel I do not have much to be proud of.")
score += answer_neg(score)
print("6. I take a positive attitude toward myself.")
score += answer_pos(score)
print("7. On the whole, I am satisfied with myself.")
score += answer_pos(score)
print("8. I wish I could have more respect for myself.")
score += answer_neg(score)
print("9. I certainly feel useless at times.")
score += answer_neg(score)
print("10. At times I think I am no good at all.")
score += answer_neg(score)
print()
print(f"Your score is {score}")