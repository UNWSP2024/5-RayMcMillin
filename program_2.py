# Ray McMillin, Addition Code, 2/21/2025

import random

def math_quiz():
    
    number1 = random.randint(1, 999)
    number2 = random.randint(1, 999)
    
    user_answer = int(input(f"What is {number1} + {number2}? "))
    
    correct_answer = number1 + number2
    
    if user_answer == correct_answer:
        print("Congratulations! That's correct!")
    else:
        print(f"Not quite, the correct answer is {correct_answer}.")

def main():
   
    math_quiz()

if __name__ == "__main__":
    main()
