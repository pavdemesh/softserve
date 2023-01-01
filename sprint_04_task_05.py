class Gallows:

    def __init__(self):
        self.words = []
        self.game_over = False

    def restart(self):
        self.words = []
        self.game_over = False
        print("restarted!")

    def play(self, word):
        if not self.game_over:
            # if empty list - just add the word and print the list
            if not self.words:
                self.words.append(word)
                print(self.words)
            # check rules 1 and 2
            elif word not in self.words and (word[0] == self.words[-1][-1]):
                self.words.append(word)
                print(self.words)
            else:
                print("game over")
                self.game_over = True


game = Gallows()
game.play("echo")
game.play("order")
game.play("romo")
game.play("order")
print(game.words)

game.restart()
game.play("order")

