import tkinter
import math

tk = tkinter.Tk() 
tk.title("Scientific Calculator")
tk.geometry("450x400")
tk.configure(bg="#222") 

def format_expression(expression):
    expression = expression.replace("÷", "/").replace("×", "*").replace("xʸ", "**").replace("%", "/100")
    expression = expression.replace("π", "math.pi").replace("e", "math.e")

    math_functions = {
        "ln": "math.log",
        "lg": "math.log10",
        "√x": "math.sqrt",
        "sin⁻¹": "math.asin",
        "cos⁻¹": "math.acos",
        "tan⁻¹": "math.atan"
    }

    for func, math_func in math_functions.items():
        index = expression.find(func)
        while index != -1:
            i = index + len(func)
            num_start = i

            while i < len(expression) and (expression[i].isdigit() or expression[i] == "."):
                i += 1

            if i > num_start: 
                expression = expression[:index] + f"{math_func}({expression[num_start:i]})" + expression[i:]
            
            index = expression.find(func, index + 1)  # Find next occurrence

    return expression

# Functionality for button clicks
def on_click(event):
    text = event.widget.cget("text")
    if text == "AC":
        entry.delete(0, tkinter.END)
    elif text == "⌫":
        entry.delete(len(entry.get()) - 1, tkinter.END)
    elif text == "=":
        try:
            expression = format_expression(entry.get())  # Process expression manually
            result = eval(expression, {"math": math})
            entry.delete(0, tkinter.END)
            entry.insert(tkinter.END, result)
        except Exception:
            entry.delete(0, tkinter.END)
            entry.insert(tkinter.END, "Error")
    else:
        entry.insert(tkinter.END, text)

entry = tkinter.Entry(
    tk, font=("Arial", 20), justify="right", bd=10, relief=tkinter.FLAT,
    bg="#333", fg="white", insertbackground="white", highlightthickness=2, highlightbackground="#555"
)
entry.pack(padx=10, pady=10)

# Adding buttons
buttons = [
    ["sin⁻¹", "cos⁻¹", "tan⁻¹", "(", ")"],
    ["xʸ", "lg", "ln", "⌫", "AC"],
    ["√x", "7", "8", "9", "-"],
    ["e", "4", "5", "6", "+"],
    ["%", "1", "2", "3", "÷"],
    ["π", "0", ".", "="]
]

btn_frame = tkinter.Frame(tk, bg="#222")
btn_frame.pack()

# Button styles
btn_bg = "#444"  
btn_fg = "white"  
btn_font = ("Arial", 14,"bold")
btn_padx, btn_pady = 5, 5  

for r, row in enumerate(buttons):
    for c, label in enumerate(row):
        btn_color = "orange" if label == "=" else btn_bg  
        
        btn = tkinter.Button(
            btn_frame, text=label, width=4, height=1, font=btn_font,
            bg=btn_color, fg=btn_fg, relief="flat", borderwidth=0,  
            highlightthickness=0, padx=5, pady=5 
        )
        
        btn.grid(row=r, column=c, padx=5, pady=5)
        btn.bind("<Button-1>", on_click)

tk.mainloop()
