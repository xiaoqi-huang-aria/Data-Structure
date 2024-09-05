class Question:
    def __init__(self, question, answer1, answer2, answer3, answer4, correct_answer):
        self._question = question
        self._answers = [answer1, answer2, answer3, answer4]
        self._correct_answer = correct_answer
    
    def get_question(self):
        return self._question
    
    def get_answers(self):
        return self._answers
    
    def get_correct_answer(self):
        return self._correct_answer
    
    def set_question(self, question):
        self._question = question
    
    def set_answers(self, answers):
        self._answers = answers
      
    
    def set_correct_answer(self, correct_answer):
        self._correct_answer = correct_answer

questions = [
    Question("What is the capital of France?", "Berlin", "London", "Paris", "Rome", 3),
    Question("Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2),
    Question("What is the largest ocean on Earth?", "Atlantic", "Indian", "Arctic", "Pacific", 4),
    Question("Who wrote 'Romeo and Juliet'?", "Charles Dickens", "Jane Austen", "William Shakespeare", "Mark Twain", 3),
    Question("What is the smallest prime number?", "0", "1", "2", "3", 3),
    Question("What is the chemical symbol for water?", "H2O", "O2", "CO2", "NaCl", 1),
    Question("How many continents are there?", "5", "6", "7", "8", 3),
    Question("What year did the Titanic sink?", "1910", "1912", "1914", "1916", 2),
    Question("What is the longest river in the world?", "Amazon", "Nile", "Yangtze", "Mississippi", 2),
    Question("Which element has the atomic number 1?", "Helium", "Oxygen", "Hydrogen", "Nitrogen", 3)]

def ask_question(question):
    print(question.get_question())
    answers = question.get_answers()
    for i, answer in enumerate(answers, 1):
        print(f"{i}. {answer}")
    while True:
        try:
            user_answer = int(input("Your answer (1-4): "))
            if 1 <= user_answer <= 4:
                return user_answer == question.get_correct_answer()
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

def main():
    player1_score = 0
    player2_score = 0

    print("Welcome to the Trivia Game!")
    print("Player 1 will start.")
    
    for i in range(10):
        if i % 2 == 0:
            print(f"\nPlayer 1's turn. Question {i // 2 + 1}:")
            if ask_question(questions[i]):
                print("Correct!")
                player1_score += 1
            else:
                print("Incorrect!")
        else:
            print(f"\nPlayer 2's turn. Question {(i // 2) + 1}:")
            if ask_question(questions[i]):
                print("Correct!")
                player2_score += 1
            else:
                print("Incorrect!")

    print("\nGame Over!")
    print(f"Player 1 scored: {player1_score}")
    print(f"Player 2 scored: {player2_score}")

    if player1_score > player2_score:
        print("Player 1 wins!")
    elif player2_score > player1_score:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()

