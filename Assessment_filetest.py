import random

# sets incorrect and correct to 1 to avoid a divide by 0 error (must be placed before def code)
correct = 0
incorrect = 0


def operators():
    op = random.randint(1, 3)
    if op == 1:
        oper = "-"
    elif op == 2:
        oper = "+"
    elif op == 3:
        oper = "*"
    return oper


# string checker for instructions and stats
def string_checker(question, valid_ans):
    error = f"Please enter a valid option from the following list: {valid_ans}"
    while True:
        user_response = input(question).lower()

        for item in valid_ans:
            # check if input is on the list
            if item == user_response:
                return item

            # Check if input is the same as the first letter of an item on the list
            elif user_response == item[0]:
                return item

        print(error)


# asks the user about how many rounds they want
def int_checker(question):
    while True:
        error = "Please enter an integer that is 5 or higher"

        to_check = input(question)

        # Check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # Checks if integer is greater than or equal to 5
            if response < 5:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# def test_checker(question, valid_ans):
#     error = f"Please enter a valid option from the following list: {valid_ans}"
#     while True:
#         user_response = input(question).lower()
#
#         for item in valid_ans:
#             # check if input is on the list
#             if item == user_response:
#                 return item
#
#             # Check if input is the same as the first letter of an item on the list
#             elif user_response == item[0]:
#                 return item
#
#         print(error)


# game mode list
mult_add_etc = ["multiplication", "addition", "subtraction", "hardmode"]
# asks users what game mode they want
test_check = string_checker("Do you want to do multiplication, addition, subtraction, or hard mode?", mult_add_etc)
# subtraction quiz
if test_check == "subtraction":

    # defines the numbers used in the questions
    def rand_num():
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        ans = a - b
        return a, b, ans


    # creates a ys/no list for stats and instructions
    yes_no = ["yes", "no"]

    # prints title
    print("Subtraction Quiz")

    # asks users if they want to see they instructions and gives them the instructions if they say yes
    want_instructions = string_checker("Would you like to read the instructions?", yes_no)
    if want_instructions == "yes":
        print('''
        This is a subtraction quiz. it will test you on subtracting numbers from 1-100. 
        When asked please answer the subtraction question provided.
        Afterwards you may see your statistics.
        ''')
    elif want_instructions == "no":
        print()

    # sets rounds to 0 at start of program. Sets mode to regular
    mode = "regular"
    rounds_played = 0

    # Ask user for number of rounds / infinite mode
    num_rounds = int_checker("How many rounds would you like? Push enter for infinite mode")
    if num_rounds == "infinite":
        mode = "infinite"
        num_rounds = 5

    while rounds_played < num_rounds:

        # Rounds headings and question code
        # code for when the number of rounds is infinite
        if mode == "infinite":
            rounds_heading = f"\n000 Concluding Round {rounds_played + 1} (Infinite Mode) 000"
            a, b, ans, = rand_num()
            ans = str(ans)
            print(f"What is {a} - {b}")
            user_ans = input("Your answer: ")

            if user_ans == ans:
                correct += 1
                print("Correct")
            elif user_ans == "xxx":
                break
            else:
                incorrect += 1
                print("Your answer was either invalid or incorrect")
        # code for when the number of rounds is finite
        else:
            rounds_heading = f"\n💿💿💿 Concluding Round {rounds_played + 1} of {num_rounds}💿💿💿"
            a, b, ans, = rand_num()
            ans = str(ans)
            print(f"What is {a} - {b}")
            user_ans = input("Your answer: ")

            if user_ans == ans:
                print("Correct")
            elif user_ans == "xxx":
                break
            else:
                print("Your answer was either invalid or incorrect")
        print(rounds_heading)
        print()

        rounds_played += 1

        # Increase num_rounds for infinite mode
        if mode == "infinite":
            num_rounds += 1

    # calculates stats
    percent_won = correct / rounds_played * 100
    percent_lost = incorrect / rounds_played * 100

    # asks user if they want top see their stats
    want_stats = string_checker("Do you want to see your stats?", yes_no)
    # provides stats if user answers yes
    if want_stats == "yes":
        print(f"You won {percent_won}%. You lost {percent_lost}%.")

# addition quiz
if test_check == "addition":

    # defines the numbers used in the questions
    def rand_num():
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        ans = a + b
        return a, b, ans


    # creates a ys/no list for stats and instructions
    yes_no = ["yes", "no"]

    # prints title
    print("Addition Quiz")

    # asks users if they want to see they instructions and gives them the instructions if they say yes
    want_instructions = string_checker("Would you like to read the instructions?", yes_no)
    if want_instructions == "yes":
        print('''
           This is an addition quiz. it will test you on adding numbers from 1-100. 
           When asked please answer the addition question provided.
           Afterwards you may see your statistics.
           ''')
    elif want_instructions == "no":
        print()

    # sets rounds to 0 at start of program. Sets mode to regular
    mode = "regular"
    rounds_played = 0

    # Ask user for number of rounds / infinite mode
    num_rounds = int_checker("How many rounds would you like? Push enter for infinite mode")
    if num_rounds == "infinite":
        mode = "infinite"
        num_rounds = 5

    while rounds_played < num_rounds:

        # Rounds headings and question code
        # code for when the number of rounds is infinite
        if mode == "infinite":
            rounds_heading = f"\n000 Concluding Round {rounds_played + 1} (Infinite Mode) 000"
            a, b, ans, = rand_num()
            ans = str(ans)
            print(f"What is {a} + {b}")
            user_ans = input("Your answer: ")

            if user_ans == ans:
                correct += 1
                print("Correct")
            elif user_ans == "xxx":
                break
            else:
                incorrect += 1
                print("Your answer was either invalid or incorrect")
        # code for when the number of rounds is finite
        else:
            rounds_heading = f"\n💿💿💿 Concluding Round {rounds_played + 1} of {num_rounds}💿💿💿"
            a, b, ans, = rand_num()
            ans = str(ans)
            print(f"What is {a} * {b}")
            user_ans = input("Your answer: ")

            if user_ans == ans:
                print("Correct")
            elif user_ans == "xxx":
                break
            else:
                print("Your answer was either invalid or incorrect")
        print(rounds_heading)
        print()

        rounds_played += 1

        # Increase num_rounds for infinite mode
        if mode == "infinite":
            num_rounds += 1

    # calculates stats
    percent_won = correct / rounds_played * 100
    percent_lost = incorrect / rounds_played * 100

    # asks user if they want top see their stats
    want_stats = string_checker("Do you want to see your stats?", yes_no)
    # provides stats if user answers yes
    if want_stats == "yes":
        print(f"You won {percent_won}%. You lost {percent_lost}%.")

# multiplication quiz
if test_check == "multiplication":

    # defines the numbers used in the questions
    def rand_num():
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        ans = a * b
        return a, b, ans


    # creates a ys/no list for stats and instructions
    yes_no = ["yes", "no"]

    # prints title
    print("Multiplication Quiz")

    # asks users if they want to see they instructions and gives them the instructions if they say yes
    want_instructions = string_checker("Would you like to read the instructions?", yes_no)
    if want_instructions == "yes":
        print('''
        This is a multiplication quiz. it will test you on your 1-12 times tables. 
        When asked please answer the multiplication question provided.
        Afterwards you may see your statistics.
        ''')
    elif want_instructions == "no":
        print()

    # sets rounds to 0 at start of program. Sets mode to regular
    mode = "regular"
    rounds_played = 0

    # Ask user for number of rounds / infinite mode
    num_rounds = int_checker("How many rounds would you like? Push enter for infinite mode")
    if num_rounds == "infinite":
        mode = "infinite"
        num_rounds = 5

    while rounds_played < num_rounds:

        # Rounds headings and question code
        # code for when the number of rounds is infinite
        if mode == "infinite":
            rounds_heading = f"\n000 Concluding Round {rounds_played + 1} (Infinite Mode) 000"
            a, b, ans, = rand_num()
            ans = str(ans)
            print(f"What is {a} * {b}")
            user_ans = input("Your answer: ")

            if user_ans == ans:
                correct += 1
                print("Correct")
            elif user_ans == "xxx":
                break
            else:
                incorrect += 1
                print("Your answer was either invalid or incorrect")
        # code for when the number of rounds is finite
        else:
            rounds_heading = f"\n💿💿💿 Concluding Round {rounds_played + 1} of {num_rounds}💿💿💿"
            a, b, ans, = rand_num()
            ans = str(ans)
            print(f"What is {a} * {b}")
            user_ans = input("Your answer: ")

            if user_ans == ans:
                print("Correct")
            elif user_ans == "xxx":
                break
            else:
                print("Your answer was either invalid or incorrect")
        print(rounds_heading)
        print()

        rounds_played += 1

        # Increase num_rounds for infinite mode
        if mode == "infinite":
            num_rounds += 1

    # calculates stats
    percent_won = correct / rounds_played * 100
    percent_lost = incorrect / rounds_played * 100

    # asks user if they want top see their stats
    want_stats = string_checker("Do you want to see your stats?", yes_no)
    # provides stats if user answers yes
    if want_stats == "yes":
        print(f"You won {percent_won}%. You lost {percent_lost}%.")

if test_check == "hardmode":

    # defines the numbers used in the questions
    def rand_hardmode():

        operator = random.choice(['+', '*', '-'])
        if operator == "+":
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            ans = a + b
        elif operator == "-":
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            ans = a - b
        elif operator == "*":
            a = random.randint(1, 12)
            b = random.randint(1, 12)
            ans = a * b
        return a, b, ans, operator


    # creates a ys/no list for stats and instructions
    yes_no = ["yes", "no"]

    # prints title
    print("Hard Quiz")
    # asks users if they want to see they instructions and gives them the instructions if they say yes
    want_instructions = string_checker("Would you like to read the instructions?", yes_no)
    if want_instructions == "yes":
        print('''
        This is a hard quiz. it will test you general arithmetic. 
        When asked please answer the arithmetic question provided.
        Afterwards you may see your statistics.
        ''')
    elif want_instructions == "no":
        print()

    # sets rounds to 0 at start of program. Sets mode to regular
    mode = "regular"
    rounds_played = 0

    # Ask user for number of rounds / infinite mode
    num_rounds = int_checker("How many rounds would you like? Push enter for infinite mode")
    if num_rounds == "infinite":
        mode = "infinite"
        num_rounds = 5

    while rounds_played < num_rounds:

        # Rounds headings and question code
        # code for when the number of rounds is infinite
        if mode == "infinite":
            rounds_heading = f"\n000 Concluding Round {rounds_played + 1} (Infinite Mode) 000"
            a, b, ans, operator = rand_hardmode()
            ans = str(ans)
            print(f"What is {a} {operator} {b}")
            user_ans = input("Your answer: ")

            if user_ans == ans:
                correct += 1
                print("Correct")
            elif user_ans == "xxx":
                break
            else:
                incorrect += 1
                print("Your answer was either invalid or incorrect")
        # code for when the number of rounds is finite
        else:
            rounds_heading = f"\n💿💿💿 Concluding Round {rounds_played + 1} of {num_rounds}💿💿💿"
            a, b, ans, operator = rand_hardmode()
            ans = str(ans)
            print(ans)
            print(f"What is {a} {operator} {b}")
            user_ans = input("Your answer: ")

            if user_ans == ans:
                print("Correct")
            elif user_ans == "xxx":
                break
            else:
                print("Your answer was either invalid or incorrect")
        print(rounds_heading)
        print()

        rounds_played += 1

        # Increase num_rounds for infinite mode
        if mode == "infinite":
            num_rounds += 1

    # calculates stats
    percent_won = correct / rounds_played * 100
    percent_lost = incorrect / rounds_played * 100

    # asks user if they want top see their stats
    want_stats = string_checker("Do you want to see your stats?", yes_no)
    # provides stats if user answers yes
    if want_stats == "yes":
        print(f"You won {percent_won}%. You lost {percent_lost}%.")
