from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5)

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value
        return total

    @classmethod
    def run(cls):
        rounds = 1
        wins = 0
        loses = 0
        c = 0
        while True:
            runner = cls()
            print("Round {}\n".format(rounds))

            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            try:
                guess = int(guess)
            except ValueError:
                print("That's not an interger! Try again...")
                quit()

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                wins += 1
                c += 1
                rounds += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                c = 0
                loses += 1
                rounds += 1
            print("Wins: {} Loses {}".format(wins, loses))

            if c == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                break

            prompt = input("Would you like to play again?[Y/n]: ")

            if prompt == 'y' or prompt == '':
                continue
            else:
                i_just_throw_an_exception()
