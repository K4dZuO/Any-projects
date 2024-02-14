import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
picture_path = r"C:\Users\ersch\Downloads\calc.png"
photo = tk.PhotoImage(file=picture_path)
win.iconphoto(False, photo)
win.geometry(f"240x270+100+200")
win.resizable(False, False)
win.config(background='#1f5b3e')
win.title('Hand-made Calculator')

# cache operation

cache_digit = None
cache_operation = None


# binding
def press_key(event):
    char = event.char
    if char.isdigit():
        add_digit(char)
    elif char in '/*+-':
        add_operation(char)
    elif char == '\r':
        calculate()
    elif char == '\x08':
        clean_the_output()

win.bind('<Key>', press_key)


# functions part

def add_digit(sign):
    value = output.get()
    if value in ('0', 'Error'):
        output.delete(0, tk.END)
    output.insert(tk.END, sign)


def clean_the_output():
    global cache_operation, cache_digit
    cache_digit = None
    cache_operation = None
    output.delete(0, tk.END)
    output.insert(0, '0')


def add_operation(operation):
    value = output.get()
    if value[-1] in '+-*/':  # защита от двух посл. операций
        ind = len(value) - 1
        output.delete(ind, tk.END)
    if '+' in value[:-1] or '-' in value[1:-1] or '*' in value[:-1] or '/' in value[:-1]:
        calculate()
    output.insert(tk.END, operation)

def make_operation(string_value):
    global cache_operation, cache_digit

    if '+' in string_value[1:]:
        s1, s2 = map(int, string_value.rsplit('+'))
        operation = '+'
    elif '-' in string_value[1:]:
        s1, s2 = map(int, string_value.rsplit('-', maxsplit=1))
        operation = '-'
    elif '*' in string_value[1:]:
        s1, s2 = map(int, string_value.rsplit('*'))
        operation = '*'
    elif '/' in string_value[1:]:
        s1, s2 = map(int, string_value.rsplit('/'))
        operation = '/'

    try:
        if operation == '+':
            res = s1 + s2
            cache_operation = '+'
        elif operation == '-':
            res = s1 - s2
            cache_operation = '-'
        elif operation == '*':
            res = s1 * s2
            cache_operation = '*'
        elif operation == '/':
            res = s1 / s2
            cache_operation = '/'

        cache_digit = s2
    except (NameError or ValueError):
        messagebox.showinfo('Error!', 'You can serve only by natural numbers and operations!.')
        res = "Error"
    except ZeroDivisionError:
        messagebox.showinfo('Error!', 'Division by zero is unsupported operation!')
        res = "Error"
    except:
        messagebox.showinfo('Error!', 'Something is gone wrong.')
        res = "Error"

    return res

def calculate():
    global cache_operation, cache_digit

    res = None
    flag_error = False
    value = output.get()

    if value[-1] in '+/*': # если запись вида "15*"
        value += value[0:-1]
    elif value[-1] == '-':
        if value[0] == '-':
            value = 2*value[:-1]
        else:
            value = value + value[0:-1]

    if value[0] == '-':
        if value[1:].isdigit(): # если запись вида "-15" # -1
            if cache_operation == None:
                res = int(value)
            else:
                res = make_operation(f"{value} {cache_operation} {cache_digit}")
    else:
        if value.isdigit(): # если запись вида "15" # -1
            if cache_operation == None:
                res = int(value)
            else:
                res = make_operation(f"{value} {cache_operation} {cache_digit}")


    if res == None:
        res = make_operation(value)

    if res == 'Error':
        output.delete(0, tk.END)
        output.insert(0, 'Error')
        cache_digit = None
        cache_operation = None
        flag_error = True

    if not flag_error:
        output.delete(0, tk.END)
        if res%1 == 0:
            res = int(res)
        output.insert(0, res)



def add_digit_button(digit):
    return tk.Button(win, text=digit, command=lambda: add_digit(digit), font=('Libertine', 14, 'normal'),
                     relief=tk.RAISED, bd=4)


def add_operation_button(operation):
    return tk.Button(win, text=operation, command=lambda: add_operation(operation), fg='red',
                     font=('Libertine', 14, 'normal'),
                     relief=tk.RAISED, bd=4)


def make_calc_button(operation):
    return tk.Button(win, text=operation, command=calculate, fg='blue', font=('Libertine', 14, 'normal'),
                     relief=tk.RAISED, bd=4)


def make_delete_button(operation):
    return tk.Button(win, text=operation, command=clean_the_output, fg='blue',
                     font=('Libertine', 14, 'normal'), relief=tk.RAISED, bd=4)


# Content part


output = tk.Entry(win, justify=tk.RIGHT, font=('Libertine', 12, 'normal'))
output.insert(0, '0')
output.grid(row=0, column=0, columnspan=4, stick='wens', padx=5, pady=5)

add_digit_button('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
add_digit_button('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
add_digit_button('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
add_digit_button('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
add_digit_button('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
add_digit_button('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
add_digit_button('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
add_digit_button('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
add_digit_button('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
add_digit_button('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

add_operation_button('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
add_operation_button('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
add_operation_button('*').grid(row=3, column=3, stick='wens', padx=5, pady=5)
add_operation_button('/').grid(row=4, column=3, stick='wens', padx=5, pady=5)

make_calc_button('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)

make_delete_button('C').grid(row=4, column=1, stick='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(0, minsize=30)
win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()
