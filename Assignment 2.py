lottery  = "won the prize"

print("choose correct character of the word '",lottery,"' to win the lottery")
inputs = input(" ").lower()

if inputs == "o" or inputs == "h" or inputs == "e" or inputs == "z":
    print("congratulation,you win the lottery")
else:
    print("sorry, You didn't win the lottery")