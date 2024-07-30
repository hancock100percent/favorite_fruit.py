# 5-7 Favorite Fruit: Make a list of your favorite fruits, and when write a
# series of independent if statements that check for certain fruits in your
# list.

# Make a list of your three favorite fruits and call it favorite_fruits.

# Write five if statements.  Each should check whether a certain kind of fruit
# is in your list.  If the fruit is in your list, the if block should print a
# statement, such as You really like bananas!

favorite_fruits = [
    'banana',
    'apple',
    'orange'
]
messages = [
    'wassup!!!',
]
print(favorite_fruits)

def guessing_game():
    print("check if you are on the list")
    print("hint it is a fruit")

guessing_game()

while True:
    try:
        guess = (input("Enter a type of fruit: "))

        if guess in favorite_fruits:
            msg = f"You got it, {messages[0]}!"
            print(msg)
        else:
            print("nope")
    except ValueError:
        print("Invalid input! WTF?")

    break

# # Define a list of items
# my_list = ['apple', 'banana', 'cherry', 'date']

# # Get user input
# user_input = input("Enter an item to check if it's in the list: ")

# # Check if the input is in the list
# if user_input in my_list:
#     print(f"{user_input} is in the list!")
# else:
#     print(f"{user_input} is not in the list.")

# # while true:
# # if yes:
# #     print("listed")
# # if no:
# #     print("not listed")
