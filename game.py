from word_manager import WordManager

class Game():
    def __init__(self, game_screen):
        self.word_manager = WordManager()
        self.game_screen = game_screen
        self.selected_words = []
        self.current_index = 0
        self.correct_word = ""
        self.total_correct = 0
        self.total_wrong = 0
        self.score = 0
        self.round_count = 0

        if game_screen:
            game_screen.game = self

    def ask_words(self):
        if self.current_index < len(self.selected_words):
            word = self.selected_words[self.current_index]
            self.game_screen.show_word(word)
            self.correct_word = self.word_manager.words[word]
        else:
            self.game_screen.lbl_feedback.config(text="GAME OVER!", bg="#27A3F5", fg="white",
                                             font=("Helvetica", 30, "italic bold"), padx=20, pady=10)
            self.game_screen.entry_turkish_word.config(state="disabled")
            self.game_screen.entry_turkish_word.grid_remove()
            self.game_screen.lbl_turkish.grid_remove()
            self.game_screen.lbl_english.grid_remove()
            self.game_screen.lbl_english_word.grid_remove()
            self.current_index = 0
            self.game_screen.lbl_feedback.place(relx=0.5, rely=0.5, anchor="center")
            self.game_screen.blink_label(self.game_screen.lbl_feedback)
            self.game_screen.root.after(2000, self.game_screen.show_score_label)

    def check_answer(self, user_answer):
        if user_answer.strip().lower() == self.correct_word.lower():
            self.total_correct += 1
            return True
        else:
            self.total_wrong += 1
            return False

    def game_start(self, round_count):
        self.round_count = round_count
        self.game_screen.game_area()
        self.selected_words = self.word_manager.select_word(self.round_count)
        self.ask_words()