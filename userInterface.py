import random
import tkinter as tk

def startUserInterface(words, starting_letters, all_letters):
    def on_entry_change(*args):
        # Get text from the first 20 entry widgets and update the text widget
        entries_text = '\n'.join(words)
        text_widget.config(state=tk.NORMAL)  # Enable editing temporarily
        text_widget.delete(1.0, tk.END)  # Clear existing text
        text_widget.insert(tk.END, entries_text)
        text_widget.config(state=tk.DISABLED)  # Disable editing again
        
    def create_interface(num_boxes):
        # Calculate the number of rows based on the total number of entry widgets
        num_rows = (num_boxes + 1) // 2

        # Create the main application window
        app = tk.Tk()
        app.title(f"GUI with {num_boxes} Numbered Text Boxes")

        # Create entry widgets on the left side with labels, in two columns
        entry_vars = [tk.StringVar() for _ in range(num_boxes)]
        for i in range(num_boxes):
            label = tk.Label(app, text=f"{i + 1}.")
            label.grid(row=i % num_rows, column=i // num_rows * 2, padx=(5, 0), pady=5, sticky="e")

            entry = tk.Entry(app, textvariable=entry_vars[i], width=2)
            entry.grid(row=i % num_rows, column=i // num_rows * 2 + 1, pady=5)

            # Add a callback to be executed whenever the entry text changes
            entry_vars[i].trace_add('write', on_entry_change)

        # Create a read-only text widget on the right side
        text_widget = tk.Text(app, wrap=tk.WORD, width=40, height=20, state=tk.DISABLED)
        text_widget.grid(row=0, column=num_boxes // num_rows * 2 + 1, rowspan=num_rows, padx=10, pady=10)

        return app, entry_vars, text_widget


    char_num = len(all_letters)
    random_letters = random.sample(list(all_letters), len(all_letters))
    random_words = random.sample(words, len(words))

    app, entry_vars, text_widget = create_interface(char_num)
    on_entry_change()

    # Start the main event loop
    app.mainloop()
