import tkinter as tk

# --- FUNCTIONS ---
def add_value(value):
    current_text = display_var.get()
    display_var.set(current_text + str(value))

def clear_display():
    display_var.set("")

def delete_last():
    display_var.set(display_var.get()[:-1])

def calculate_result():
    try:
        expression = display_var.get()

        # Convert % to /100
        expression = expression.replace("%", "/100")

        result = eval(expression)

        # Remove .0 if integer
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        display_var.set(str(result))

    except:
        display_var.set("Error")

# --- WINDOW ---
app = tk.Tk()
app.title("Calculator")
app.geometry("320x500")
app.configure(bg="#0d0d0d")

display_var = tk.StringVar()

# --- DISPLAY ---
display = tk.Entry(
    app,
    textvariable=display_var,
    font=("Arial", 28),
    bg="#0d0d0d",
    fg="white",
    bd=0,
    justify="right",
    insertbackground="white"
)
display.pack(fill="both", ipadx=10, ipady=25, padx=10, pady=10)

# --- FRAME ---
button_frame = tk.Frame(app, bg="#0d0d0d")
button_frame.pack(expand=True, fill="both")

# --- BUTTON CREATOR ---
def create_button(text, row, col, command, bg="#1a1a1a", fg="white"):
    button = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 16),
        bg=bg,
        fg=fg,
        bd=0,
        activebackground="#333333",
        command=command
    )
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# --- GRID ---
for i in range(6):
    button_frame.rowconfigure(i, weight=1)
for j in range(4):
    button_frame.columnconfigure(j, weight=1)

# --- BUTTONS ---
create_button("C", 0, 0, clear_display, fg="red")
create_button("%", 0, 1, lambda: add_value("%"), fg="#00ff99")
create_button("⌫", 0, 2, delete_last, fg="#00ff99")
create_button("÷", 0, 3, lambda: add_value("/"), fg="#00ff99")

create_button("7", 1, 0, lambda: add_value("7"))
create_button("8", 1, 1, lambda: add_value("8"))
create_button("9", 1, 2, lambda: add_value("9"))
create_button("×", 1, 3, lambda: add_value("*"), fg="#00ff99")

create_button("4", 2, 0, lambda: add_value("4"))
create_button("5", 2, 1, lambda: add_value("5"))
create_button("6", 2, 2, lambda: add_value("6"))
create_button("-", 2, 3, lambda: add_value("-"), fg="#00ff99")

create_button("1", 3, 0, lambda: add_value("1"))
create_button("2", 3, 1, lambda: add_value("2"))
create_button("3", 3, 2, lambda: add_value("3"))
create_button("+", 3, 3, lambda: add_value("+"), fg="#00ff99")

create_button("0", 4, 0, lambda: add_value("0"))
create_button(".", 4, 1, lambda: add_value("."))

# Equal button
equal_button = tk.Button(
    button_frame,
    text="=",
    font=("Arial", 16),
    bg="#00cc66",
    fg="white",
    bd=0,
    command=calculate_result
)
equal_button.grid(row=4, column=2, columnspan=2, sticky="nsew", padx=5, pady=5)

app.mainloop()