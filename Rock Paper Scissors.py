from random import choice

options = ["Rock", "Paper", "Scissors"]
number = input("Enter number of iterations: ")
number = int(number)

ai_score = 0
user_score = 0

for element in range(1, number + 1):
    ai_output = choice(options)
    user_input = input("Your choice: ")

    if ai_output == "Rock" and user_input == "Rock":
        print("AI: " + ai_output)
        print("It's a tie!")
        ai_score += 0.5
        user_score += 0.5
    if ai_output == "Rock" and user_input == "Paper":
        print("AI: " + ai_output)
        print("User wins!")
        user_score += 1
    if ai_output == "Rock" and user_input == "Scissors":
        print("AI: " + ai_output)
        print("AI wins!")
        ai_score += 1

    if ai_output == "Paper" and user_input == "Rock":
        print("AI: " + ai_output)
        print("AI wins!")
        ai_score += 1
    if ai_output == "Paper" and user_input == "Paper":
        print("AI: " + ai_output)
        print("It's a tie!")
        ai_score += 0.5
        user_score += 0.5
    if ai_output == "Paper" and user_input == "Scissors":
        print("AI: " + ai_output)
        print("User wins!")
        user_score += 1

    if ai_output == "Scissors" and user_input == "Rock":
        print("AI: " + ai_output)
        print("User wins!")
        user_score += 1
    if ai_output == "Scissors" and user_input == "Paper":
        print("AI: " + ai_output)
        print("AI wins!")
        ai_score += 1
    if ai_output == "Scissors" and user_input == "Scissors":
        print("AI: " + ai_output)
        print("It's a tie!")
        ai_score += 0.5
        user_score += 0.5

print("AI score: ", ai_score)
print("User score: ", user_score)
if ai_score > user_score:
    print("AI wins the tournament!!!")
if ai_score < user_score:
    print("User wins the tournament!!!")
if ai_score == user_score:
    print("The tournament ends in a tie!!!")