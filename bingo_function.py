# import and global variable
import random

MAX_NUMBER = 50
MIN_NUMBER = 1
max_guess_counts = 5


# generate a random number
def generate_random_num():
    return random.randint(MIN_NUMBER, MAX_NUMBER)


# get a input
def get_user_input():
    print(f"Your number should be between {MIN_NUMBER}, {MAX_NUMBER}")
    while True:
        try:
            user_input = int(input("Enter  Your Number: "))

        except ValueError:
            print("Error: Enter a valid number")
        else:
            return user_input


# cheak gussed number
def check_gussed_number(user_input, random_num):
    return user_input == random_num


# main runner
def main():
    global max_guess_counts

    random_num = generate_random_num()
    print(f" random number is :{random_num}")
    while max_guess_counts > 0:
        user_input = get_user_input()
        if check_gussed_number(user_input, random_num):
            print("Your have gessed right")
            break
        max_guess_counts -= 1
        print(f" guesses left: {max_guess_counts}")
    else:
        print("you couldn't guess the number , and Game Over")


if __name__ == "__main__":
    main()
