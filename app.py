import tkinter as tk

class LiveCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Live Character Counter Tool")
        self.root.geometry("500x400")

        # Text box
        self.text_box = tk.Text(root, wrap="word", font=("Arial", 14))
        self.text_box.pack(padx=10, pady=10, fill="both", expand=True)
        self.text_box.bind("<KeyRelease>", self.update_counts)

        # Labels
        self.char_label = tk.Label(root, text="Characters: 0", font=("Arial", 12))
        self.char_label.pack(anchor="w", padx=10)

        self.word_label = tk.Label(root, text="Words: 0", font=("Arial", 12))
        self.word_label.pack(anchor="w", padx=10)

        self.sentence_label = tk.Label(root, text="Sentences: 0", font=("Arial", 12))
        self.sentence_label.pack(anchor="w", padx=10)

    def update_counts(self, event=None):
        text = self.text_box.get("1.0", tk.END).strip()
        char_count = len(text)
        word_count = len(text.split()) if text else 0
        sentence_count = text.count('.') + text.count('!') + text.count('?')

        self.char_label.config(text=f"Characters: {char_count}")
        self.word_label.config(text=f"Words: {word_count}")
        self.sentence_label.config(text=f"Sentences: {sentence_count}")


if __name__ == "__main__":
    root = tk.Tk()
    app = LiveCounterApp(root)
    root.mainloop()

