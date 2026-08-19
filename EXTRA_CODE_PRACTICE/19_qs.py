# Write a program that keeps asking the user to enter a password until they enter the correct one.

password = input("Enter your password : ")

while True :
    correct_password = input("Enter The Password Again : ")
    match password :
        # case correct_password :
        #     print("You enter correct password")
        #     break

        # Python doesn’t treat correct_password as a variable to compare.
        # Instead, it treats it as a capture pattern, meaning:
        # “Whatever value password has, bind it to a new variable called correct_password.”
        # That means this case always matches, and since it always matches, the _ case below it is unreachable, so Python throws the error:
        # SyntaxError: name capture 'correct_password' makes remaining patterns unreachable
        case p if p==correct_password :
            print("You enter correct password")
            break
        case _ :
            print("Wrong password | Enter again")
# you can also use if-else statement