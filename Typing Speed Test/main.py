import tkinter as tk
import random
import time

class SpeedTypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed  Test")
        self.root.geometry("800x400")

        self.word_list = ["python", "programming", "django", "coding", "developer", ]
        self.current_word = ""
        self.user_input = tk.StringVar()
        self.total_words_typed = 0
        self.total_time_taken = 0
        self.time_start = 0

        self.create_widgets()

    def create_widgets(self):
        # Display word label
        self.word_label = tk.Label(self.root, text="", font=('Helvetica', 18))
        self.word_label.pack(pady=20)

        # User input entry
        self.entry = tk.Entry(self.root, textvariable=self.user_input, font=('Helvetica', 16))
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', self.check_word)

        # Start button
        start_button = tk.Button(self.root, text="Start Typing Test", command=self.start_typing_test,background="#355E3B")
        start_button.pack(pady=10)

        # Show Result button
        result_button = tk.Button(self.root, text="Show Result", command=self.show_result, background="#FFEA00")
        result_button.pack(pady=10)

        # Timer label
        self.timer_label = tk.Label(self.root, text="", font=('Helvetica', 14))
        self.timer_label.pack(pady=10)

        # Result label
        self.result_label = tk.Label(self.root, text="", font=('Helvetica', 14))
        self.result_label.pack(pady=10)

    def start_typing_test(self):
        self.current_word = random.choice(self.word_list)
        self.word_label.config(text=self.current_word)
        self.user_input.set("")
        self.entry.focus_set()
        self.time_start = time.time()
        self.root.after(10000, self.show_result)  # Set timer to 10s
        self.update_timer()

    def update_timer(self):
        current_time = int(time.time() - self.time_start)
        remaining_time = max(0, 10 - current_time)
        self.timer_label.config(text=f"Time Left: {remaining_time} seconds")
        if remaining_time > 0:
            self.root.after(1000, self.update_timer)

    def check_word(self, event):
        user_input = self.user_input.get()
        if user_input == self.current_word:
            time_end = time.time()
            elapsed_time = time_end - self.time_start
            words_per_minute = int((len(self.current_word) / elapsed_time) * 60)

            self.total_words_typed += 1
            self.total_time_taken += elapsed_time

            result_text = f"Correct! Your speed: {words_per_minute} WPM"
            self.result_label.config(text=result_text)
        else:
            self.result_label.config(text="Incorrect. Try again.")

    def show_result(self):
        if self.total_words_typed > 0:
            average_speed = int((self.total_words_typed / self.total_time_taken) * 60)
            overall_result = f"Overall Average Speed: {average_speed} WPM"
            self.result_label.config(text=overall_result)
        else:
            self.result_label.config(text="No results yet. Complete a typing test.")

if __name__ == "__main__":
    root = tk.Tk()
    typing_test = SpeedTypingTest(root)
    root.mainloop()
