#guess Game
secret_number  = 8
Guess_limit =3
Guess_count =0
while Guess_count < Guess_limit:
    
    user_value =int(input("Enter the number"))
    if user_value == secret_number:
        print ("WON")
        break
    else:
        print("incorrect, try again")
    Guess_count =Guess_count+1
