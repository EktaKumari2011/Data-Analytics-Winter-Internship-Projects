class FrogLeapGame:
    def __init__(self):
        self.positions = ['G', 'G', 'G', '-', 'B', 'B', 'B']

    def display_game(self):
        print("[ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ]")
        print(self.positions)

    def get_user_input(self):
        return input("Press 'q' to quit, else enter the position of the piece: ")

    def is_valid_move(self, selected_pos):
        if selected_pos < 0 or selected_pos > 6:
            print("Invalid move. Position should be between 0 and 6.")
            return False

        if self.positions[selected_pos] == '-':
            print("Invalid move. Empty leaf selected.")
            return False

        if selected_pos == self.positions.index('-'):
            print("Invalid move. Cannot move the empty leaf.")
            return False

        return True

    def make_move(self, selected_pos, pos2):
        self.positions[selected_pos], self.positions[pos2] = self.positions[pos2], self.positions[selected_pos]

    def check_winning_condition(self):
        return self.positions == ['B', 'B', 'B', '-', 'G', 'G', 'G']

    def play_game(self):
        while True:
            self.display_game()

            user_input = self.get_user_input()

            if user_input.lower() == 'q':
                print("You Lose")
                break

            try:
                selected_pos = int(user_input)

                if not self.is_valid_move(selected_pos):
                    continue

                pos2 = self.positions.index('-')

                if self.positions[selected_pos] == 'G':
                    if selected_pos + 1 <= 6 and self.positions[selected_pos + 1] == '-':
                        pos2 = selected_pos + 1
                    elif selected_pos + 2 <= 6 and self.positions[selected_pos + 2] == '-' and self.positions[selected_pos + 1] == 'B':
                        pos2 = selected_pos + 2
                    else:
                        print("Invalid Move")
                        continue
                elif self.positions[selected_pos] == 'B':
                    if selected_pos - 1 >= 0 and self.positions[selected_pos - 1] == '-':
                        pos2 = selected_pos - 1
                    elif selected_pos - 2 >= 0 and self.positions[selected_pos - 2] == '-' and self.positions[selected_pos - 1] == 'G':
                        pos2 = selected_pos - 2
                    else:
                        print("Invalid Move")
                        continue

                self.make_move(selected_pos, pos2)
                self.display_game()

                if self.check_winning_condition():
                    print("You Win!")
                    break

            except ValueError:
                print("Invalid input. Please enter a number or 'q' to quit.")


if __name__ == "__main__":
    game = FrogLeapGame()
    game.play_game()
