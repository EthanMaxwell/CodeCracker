import random
import tkinter as tk
from tkinter import font as tkFont

def startUserInterface(words, starting_letters, all_letters):
    def on_validate(P):
        # P is the proposed text to be inserted
        if len(P) == 0 or P[-1].upper() in all_letters:
            return True
        else:
            return False
            
    def bold_non_numbers(text_widget):
        text_widget.tag_configure("bold", font=("Courier", 25, "bold"))

        start_index = "1.0"
        while True:
            start_index = text_widget.search(r'\D', start_index, tk.END, regexp=True)
            if not start_index:
                break

            end_index = text_widget.index(f"{start_index}+1c")
            text_widget.tag_add("bold", start_index, end_index)

            start_index = end_index
    
    def on_entry_change(*args):
        for var in entry_vars:
            char = var.get()
            if len(char) == 0:
                continue
            
            if len(char) > 1 or char.islower():
                var.set(char[-1].upper())
    
        entries_text = ""
        for word in random_words:
            for i in range(len(word)):
                num = random_letters.index(word[i])
                enter = entry_vars[num].get()
                if enter == "":
                    entries_text += str(num + 1).zfill(2) + " "
                else:
                    entries_text += enter[0].upper() + " "
            entries_text += "\n\n"
        entries_text = entries_text.rstrip('\n')
        
        text_widget.config(state=tk.NORMAL)  # Enable editing temporarily
        text_widget.delete(1.0, tk.END)  # Clear existing text
        text_widget.insert(tk.END, entries_text)
        bold_non_numbers(text_widget)
        text_widget.config(state=tk.DISABLED)  # Disable editing again
        
        for label in bottom_labels.values():
            label.config(font=("Courier", 20, "bold"))
            
        for entry_var in entry_vars:
            enter = entry_var.get()
            if len(enter) > 0:
                bottom_labels[enter].config(font=("Courier", 20))
        
    
    def move_focus(event):
        current_widget = app.focus_get()
        current_index = entry_widgets.index(current_widget)
        num_rows = (len(entry_widgets) + 1) // 2

        if event.keysym == 'Down':
            next_index = (current_index + 1) % len(entry_widgets)
        elif event.keysym == 'Up':
            next_index = (current_index - 1 + len(entry_widgets)) % len(entry_widgets)
        elif event.keysym == 'Left':
            next_index = (current_index - num_rows + len(entry_widgets)) % len(entry_widgets)
        elif event.keysym == 'Right':
            next_index = (current_index + num_rows) % len(entry_widgets)
        else:
            return

        entry_widgets[next_index].focus_set()

    def create_interface(num_boxes, word_num):
        # Calculate the number of rows based on the total number of entry widgets
        num_rows = (num_boxes + 1) // 2

        # Create the main application window
        app = tk.Tk()
        app.title("Random Word Game")
        num_font = tkFont.Font(family="Courier", size=12)
        side_font = tkFont.Font(family="Courier", size=20)

        # Create entry widgets on the left side with labels, in two columns
        entry_vars = [tk.StringVar() for _ in range(num_boxes)]
        entry_widgets = []

        for i in range(num_boxes):
            label = tk.Label(app, text=f"{i + 1}.", font=side_font)
            label.grid(row=i % num_rows, column=i // num_rows * 2, padx=(5, 0), pady=5, sticky="e")
            
            validate_cmd = app.register(on_validate)
            entry = tk.Entry(app, textvariable=entry_vars[i], width=1, font=side_font, validate="key", validatecommand=(validate_cmd, "%P"))
            entry.grid(row=i % num_rows, column=i // num_rows * 2 + 1, pady=5)
            entry_widgets.append(entry)

            # Add a callback to be executed whenever the entry text changes
            entry_vars[i].trace_add('write', on_entry_change)

        # Create a read-only text widget on the right side
        text_widget = tk.Text(app, wrap=tk.WORD, width=75, height=word_num * 3, state=tk.DISABLED, font=num_font)
        text_widget.grid(row=0, column=num_boxes // num_rows * 2 + 1, rowspan=num_rows, columnspan=num_boxes, padx=10, pady=10)

        # Create a row of labels along the bottom
        letters_sorted = list(all_letters)
        letters_sorted.sort()
        bottom_labels = {}
        for i in range(num_boxes):
            bottom_label = tk.Label(app, text=letters_sorted[i])
            bottom_label.grid(row=num_rows + 1, column=num_boxes // num_rows * 2 + 1 + i , pady=5, sticky="e")
            bottom_labels[letters_sorted[i]] = bottom_label


        # Bind arrow keys to move focus
        for entry_widget in entry_widgets:
            entry_widget.bind("<Right>", move_focus)
            entry_widget.bind("<Left>", move_focus)
            entry_widget.bind("<Up>", move_focus)
            entry_widget.bind("<Down>", move_focus)

        return app, entry_vars, text_widget, entry_widgets, bottom_labels

    char_num = len(all_letters)
    random_letters = random.sample(list(all_letters), len(all_letters))
    random_words = random.sample(words, len(words))

    app, entry_vars, text_widget, entry_widgets, bottom_labels = create_interface(char_num, len(words))
    
    # Fill starting letters
    for letter in starting_letters:
        entry_vars[random_letters.index(letter)].set(letter)
    
    on_entry_change()

    # Start the main event loop
    app.mainloop()