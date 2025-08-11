from tkinter import *
from tkinter import messagebox

class MyGUI():
    def __init__(self, game):
        self.game = game
        self.root = Tk()
        self.root.title("English word quiz")
        self.root.config(bg="#222222")

        # center
        self.width = 600
        self.height = 500
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - self.width) // 2
        y = (screen_height - self.height) // 2
        self.root.geometry(f"{self.width}x{self.height}+{x}+{y}")

        # add with close esc
        self.root.bind('<Escape>', self.close_game)

        # title
        self.lbl_title = Label(self.root, text="English Word Quiz Game", font=("Times", 20, "roman bold"),
                               background="#F5F5DC", padx=20, pady=10)
        self.lbl_title.place(relx=0.5, rely=0.08, anchor="center")

        # Creator label
        maker_label = Label(self.root, text="Created by Berk", bg="#F5F5DC", fg="#555555",
                            font=("Helvetica", 8, "italic bold",))
        maker_label.place(relx=1.0, rely=1.0, anchor="se")

        # Label for the game round
        self.lbl_game_round = Label(self.root, text="Game Round:", font=("Helvetica", 20, "italic bold"), padx=20,
                                    pady=10, bg="#27A3F5", fg="white")
        self.place_lbl_game_round = {'relx': 0.5, 'rely': 0.45, 'anchor': 'center'}
        self.lbl_game_round.place_forget()

        # Entry for the game round
        self.entry_game_round = Entry(self.root, font=("Helvetica", 15, "roman bold"), width=20)
        self.place_entry_game_round = {'relx': 0.5, 'rely': 0.55, 'anchor': 'center'}
        self.entry_game_round.place_forget()

    def initialize_game_gui(self):

        # grid config
        for i in range(4):
            self.root.columnconfigure(i, minsize=80, weight=1)
        for i in range(12):
            self.root.rowconfigure(i, minsize=40, weight=1)

        # Column titles
        self.lbl_english = Label(self.root, text="English", font=("Helvetica", 15, "bold"), padx=50, pady=10,
                                 bg="#333333", fg="#FFD700")
        self.lbl_english.grid(row=4, column=1, padx=10, pady=10)
        self.lbl_english.grid_remove()

        self.lbl_turkish = Label(self.root, text="Türkçe", font=("Helvetica", 15, "bold"), padx=50, pady=10,
                                 bg="#333333", fg="#E32424")
        self.lbl_turkish.grid(row=4, column=2, padx=10, pady=10)
        self.lbl_turkish.grid_remove()

        # English word label
        self.lbl_english_word = Label(self.root, text="word", font=("Helvetica", 10, "roman bold"), padx=50)
        self.lbl_english_word.grid(row=5, column=1, padx=10, pady=10)
        self.lbl_english_word.grid_remove()

        # Entry for Turkish word
        self.entry_turkish_word = Entry(self.root, font=("Helvetica", 10, "roman bold"), width=20)
        self.entry_turkish_word.grid(row=5, column=2, padx=10, pady=10)
        self.entry_turkish_word.bind("<Return>", self.on_word_enter_pressed)
        self.entry_turkish_word.grid_remove()

        # Button for start the game
        self.btn_start_game = Button(self.root, text="START", font=("Helvetica", 25, "italic bold"), padx=20,pady=3,
                                     bg="#27A3F5", fg="white", command=self.start_round_input, activeforeground="#27A3F5")
        self.btn_start_game.place(relx=0.5, rely=0.5, anchor='center')

        # Feedback label
        self.lbl_feedback = Label(self.root, text="LETSGO!", font=("Helvetica", 20, "bold"), padx=10, pady=10)
        self.place_lbl_feedback = {'relx': 0.5, 'rely': 0.7, 'anchor': 'center'}
        self.lbl_feedback.place_forget()

        # score label
        self.lbl_total_correct = Label(self.root, text="", font=("Helvetica", 17, "roman bold"), padx=15, pady=12,
                                       fg="white", bg="#84ED6B")
        self.lbl_total_correct.grid(row=4, column=1, padx=10, pady=10, sticky="w")
        self.lbl_total_correct.grid_remove()

        self.lbl_total_wrong = Label(self.root, text="", font=("Helvetica", 17, "roman bold"), padx=15, pady=12,
                                     bg="#F44336", fg="white")
        self.lbl_total_wrong.grid(row=4, column=2, padx=10, pady=10, sticky="e")
        self.lbl_total_wrong.grid_remove()

        # Button to replay
        self.btn_replay = Button(self.root, text="PLAY AGAİN", font=("Helvetica", 20, "italic bold"), padx=10, pady=3,
                                 bg="#27A3F5", fg="white", command=self.start_round_input, activeforeground="#27A3F5")
        self.btn_replay.place_forget()




    def show_word(self, word):
        self.lbl_english_word.config(text=word)
        self.entry_turkish_word.delete(0, END)
        self.entry_turkish_word.focus()

    def on_word_enter_pressed(self, event=None):
        user_answer = self.entry_turkish_word.get()
        is_correct = self.game.check_answer(user_answer)
        self.entry_turkish_word.config(state="disabled")
        if is_correct:
            self.lbl_feedback.config(text="CORRECT!", bg="#4CAF50", fg="white")
            self.entry_turkish_word.config(disabledbackground="#84ED6B", disabledforeground="#555555")
            self.lbl_english_word.config(bg="#84ED6B", fg="#555555")
            self.lbl_feedback.place(**self.place_lbl_feedback)
            self.root.after(1000, self.reset_interface)
        else:
            self.lbl_feedback.config(text=f"WRONG! The correct word was: {self.game.correct_word}", bg="#F44336",
                                     fg="white")
            self.entry_turkish_word.config(disabledbackground="#D62D2D", disabledforeground="white")
            self.lbl_english_word.config(bg="#D62D2D", fg="white")
            self.lbl_feedback.place(**self.place_lbl_feedback)
            self.root.after(2500, self.reset_interface)
    def start_round_input(self):
        self.lbl_game_round.place_forget()
        self.entry_game_round.place_forget()
        self.entry_turkish_word.config(state="normal")
        self.lbl_total_correct.grid_remove()
        self.lbl_total_wrong.grid_remove()
        self.btn_replay.place_forget()
        self.game.total_wrong = 0
        self.game.total_correct = 0
        self.game.current_index = 0
        self.btn_start_game.place_forget()
        self.entry_game_round.place(**self.place_entry_game_round)
        self.entry_game_round.delete(0, END)
        self.entry_game_round.focus()
        self.entry_game_round.bind("<Return>", self.on_round_enter_pressed)
        self.lbl_game_round.place(**self.place_lbl_game_round)

    def on_round_enter_pressed(self, event=None):
        input_text = self.entry_game_round.get()

        if not input_text.strip():
            messagebox.showerror("Error", "Please enter a number!")
            self.entry_game_round.delete(0, END)
            self.entry_game_round.focus()
            return

        try:
            round_count = int(input_text)
            if not 1 <= round_count <= 20:
                messagebox.showerror("Error", "Round count must be between 1-20!")
                self.entry_game_round.delete(0, END)
                self.entry_game_round.focus()
                return

            self.lbl_game_round.place_forget()
            self.entry_game_round.place_forget()
            self.game_area()
            self.game.game_start(round_count)

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")
            self.entry_game_round.delete(0, END)
            self.entry_game_round.focus()
    def reset_interface(self):
        self.entry_turkish_word.config(state="normal", background="white")
        self.entry_turkish_word.delete(0, END)
        self.entry_turkish_word.focus()
        self.lbl_english_word.config(bg="white", fg="black")
        self.lbl_feedback.place_forget()
        self.game.current_index += 1
        self.game.ask_words()

    def game_area(self):
        self.lbl_feedback.config(font=("Helvetica", 20, "bold"), padx=10, pady=10)
        self.lbl_english.grid()
        self.lbl_turkish.grid()
        self.lbl_english_word.grid()
        self.btn_start_game.place_forget()
        self.entry_turkish_word.grid()
        self.entry_turkish_word.focus()

    def blink_label(self, label, count=10, interval=50):
        self.base_font_game_over = ("Helvetica", 30, "italic bold")
        if count == 0:
            label.config(text="GAME OVER!", bg="#27A3F5", fg="white",
                                                 font=self.base_font_game_over, padx=20, pady=10)
            return
        if count % 2 == 0:
            label.config(text="GAME OVER!", fg="#27A3F5", bg="white",
                                                 font=self.base_font_game_over, padx=20, pady=10)
        else:
            label.config(text="GAME OVER!", fg="white", bg="#27A3F5",
                                                 font=self.base_font_game_over, padx=20, pady=10)
        next_interval = interval + 70
        self.root.after(interval, lambda: self.blink_label(label, count - 1, next_interval))

    def show_score_label(self):
        self.entry_turkish_word.config(state="disabled")
        self.lbl_feedback.config(font=("Helvetica", 20, "bold"),padx=10, pady=10)
        self.lbl_feedback.place_forget()
        self.lbl_feedback.place_forget()
        self.lbl_total_correct.grid()
        self.lbl_total_wrong.grid()
        self.lbl_total_correct.config(text=f"Total Correct : {self.game.total_correct}")
        self.lbl_total_wrong.config(text=f"Total Wrong : {self.game.total_wrong}")
        self.btn_replay.place(relx=0.5, rely=0.55, anchor='center')
        self.entry_turkish_word.config(state="normal", background="white")
        self.entry_turkish_word.delete(0, END)
        self.entry_turkish_word.focus()
        self.lbl_english_word.config(bg="white", fg="black")

    def run_root(self):
        self.root.mainloop()

    def close_game(self, event=None):
        self.root.destroy()