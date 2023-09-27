import tkinter as tk

def button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)

button_labels = [
    "1", "2", "3", "/",
    "4", "5", "6", "*",
    "7", "8", "9", "-",
    "0", ".", "=", "+",
    "C"
]

row, col = 2, 0
buttons = {}  # Dictionary to store buttons

for label in button_labels:
    button = tk.Button(root, text=label, padx=20, pady=20, font=("Arial", 15))
    button.grid(row=row, column=col)
    col += 1

    if col > 3:
        col = 0
        row += 1

    button.bind("<Button-1>", button_click)

root.mainloop()
