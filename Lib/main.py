import random

USER_COUNT = 0
COMPUTER_COUNT = 0

def get_user_choice():
    choices = ["камінь", "ножиці", "папір"]
    while True:
        user_choice = input("Виберіть: камінь, ножиці чи папір: ").lower()
        if user_choice in choices:
            return user_choice
        print("Неправильний ввід")

def get_computer_choice():
    return random.choice(["камінь", "ножиці", "папір"])

def get_winner(user, computer):
    global USER_COUNT, COMPUTER_COUNT
    outcomes = {"камінь": "ножиці", "ножиці": "папір", "папір": "камінь"}

    if user == computer:
        return "Нічия!"
    elif outcomes[user] == computer:
        USER_COUNT += 1
        return "Ви виграли!"
    COMPUTER_COUNT += 1
    return "Комп'ютер виграв!"

def play_game():
    global USER_COUNT, COMPUTER_COUNT
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"Ви вибрали: {user_choice}\nКомп'ютер вибрав: {computer_choice}")
        print(get_winner(user_choice, computer_choice))

        print(f"Рахунок: Ви {USER_COUNT} - {COMPUTER_COUNT} Комп'ютер")

        end = input("Закінчити гру так/ні?: ")
        if end.lower() == "так":
            print(f"Гра завершена!\nФінальний рахунок: Ви {USER_COUNT} - {COMPUTER_COUNT} Комп'ютер")
            return


if __name__ == "__main__":
    play_game()
