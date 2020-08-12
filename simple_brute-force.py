from random import *
import time

print("This tools is fully legal , just a simple expression for brute force attacks , tools work !")
time.sleep(5)
while True:
    user_pass = input("Enter your password : ")

    password = ['0', '1', '2', '3', '4', '5', '6', '7', '8','9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
                'w', 'x', 'y', 'z',]

    guess = ""


    while (guess != user_pass):
        guess = ""
        for letter in range(len(user_pass)):
            guess_letter = password[randint(0, 25)]
            guess = str(guess_letter) + str(guess)
        print(guess)
        
    print("Your password is",guess)