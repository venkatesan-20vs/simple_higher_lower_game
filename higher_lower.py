import random
from game_data  import data

def compare(user_guess, a_follower, b_follower):
    if a_follower > b_follower:
        return user_guess == "a"
    else:
        return user_guess == "b"

score =  0
game_continue = True
data_a = random.choice(data)

while game_continue:
    data_b = random.choice(data)
    if data_a == data_b:
        data_b = random.choice(data)

    print(f"Compare A: {data_a['name']},is {data_a['description']},from {data_a['country']}")
    print("Vs")
    print(f"Against B: {data_b['name']},is {data_b['description']},from {data_b['country']}")

    choice = input("Who has more followers? Type 'A' or 'B':").lower()

    print("\n"*2)

    a_follower_count = data_a['follower_count']
    b_follower_count = data_b['follower_count']

    is_correct = compare(choice,a_follower_count,b_follower_count)

    if is_correct:
        score = score + 1
        print("You got the correct answer!")
        if b_follower_count > a_follower_count:
            data_a = data_b

    else:
        print(f"You got the wrong answer! and Your final score is {score}")
        game_continue = False
