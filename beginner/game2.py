secret_word = "giraffe"
guess = ""
guess_Count = 0
guess_limit = 3
statement_count = 0
statement_limit = 3
out_of_guesses = False
print("Have a guess!")
while guess != secret_word and not(out_of_guesses):
    if statement_count < statement_limit and  1 <= statement_count:
       print("Have another guess!") 
       
    if guess_Count < guess_limit:
       guess = input("Enter guess: ")
       guess_Count += 1
       statement_count += 1
    else:
        out_of_guesses = True
        
if out_of_guesses:
    print("Out of guesses, YOU LOSE!")
else:
    print("You win!")





