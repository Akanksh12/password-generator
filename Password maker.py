import tkinter as tk
from tkinter import *
from random import randint
from pyperclip import copy  # all of imports
from pyautogui import alert

# data lists
allstuff = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ', '\t', '\n', '\r', '\x0b', '\x0c']

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
UPPERCASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
punctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
               ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']


# create window
win = tk.Tk()
win.title('Password generator')

# intvars to check if user has checked boxes
lowercasevar = IntVar()
UPPERCASEvar = IntVar()
digitsvar = IntVar()
punctuationvar = IntVar()
password_lengthvar = StringVar()

# non-label widgets
password_length = Entry(win, textvariable=password_lengthvar)
password_length.grid(column=1, row=0, padx=10)
lowercase_check = Checkbutton(
    win, variable=lowercasevar)
lowercase_check.deselect()
lowercase_check.grid(column=1, row=1, padx=10)

UPPERCASE_check = Checkbutton(
    win, variable=UPPERCASEvar)
UPPERCASE_check.deselect()
UPPERCASE_check.grid(column=1, row=2, padx=10)
digits_check = Checkbutton(win, variable=digitsvar,
                           )
digits_check.deselect()
digits_check.grid(
    column=1, row=3, padx=10)
punctuation_check = Checkbutton(
    win, variable=punctuationvar)
punctuation_check.deselect()
punctuation_check.grid(column=1, row=4, padx=10)

# labels

password_label = Label(win, text='Length of your password:').grid(
    column=0, row=0, padx=10)

lowercase_label = Label(win, text='Lowercase letters').grid(
    column=0, row=1, padx=10)

UPPERCASE_label = Label(win, text='Uppercase letters').grid(
    column=0, row=2, padx=10)

digits_label = Label(win, text='Digits').grid(
    column=0, row=3, padx=10)

punctuation_label = Label(win, text='Punctuation').grid(
    column=0, row=4, padx=10)

# definitions


def generate_with_all():
    if lowercase and UPPERCASEvar and digitsvar and punctuationvar == 0:
        alert('select any options or use the generate with all button')

    to_use = []
    if lowercasevar.get() == 1:
        to_use = to_use + lowercase

    if UPPERCASEvar.get() == 1:
        to_use = to_use + UPPERCASE
    if digitsvar.get() == 1:
        to_use = to_use + digits
    if punctuationvar.get() == 1:
        to_use = to_use + punctuation
    try:
        times = int(password_lengthvar.get())
    except:
        alert('Please provide a whole number for password length(not 0)')
        return
    result = ''

    for i in range(times):
        try:
            r = randint(1, len(allstuff))
        except:
            pass
        result += allstuff[r-1]
    try:
        copy(result)
    except:
        alert('Password too big to copy to clipboard')
    alert(f'Password generated with result: {result}')


def generate():
    if lowercase and UPPERCASEvar and digitsvar and punctuationvar == 0:
        alert('select any options or use the generate with all button')

    to_use = []
    if lowercasevar.get() == 1:
        to_use = to_use + lowercase

    if UPPERCASEvar.get() == 1:
        to_use = to_use + UPPERCASE
    if digitsvar.get() == 1:
        to_use = to_use + digits
    if punctuationvar.get() == 1:
        to_use = to_use + punctuation
    try:
        times = int(password_lengthvar.get())
    except:
        alert('Please provide a whole number for password length(not 0)')
        return
    result = ''

    for i in range(times):
        try:
            r = randint(1, len(to_use))
        except:
            alert('select any options or use the generate with all button')
            return
        result += to_use[r-1]
    try:
        copy(result)
    except:
        alert('Password is too big to copy to clipboard')
    alert(f'Password generated with result: {result}')

# buttons


generate_button = Button(win, text='Generate now', command=generate).grid(
    column=0, row=5, padx=10)
generate_with_all_button = Button(win, text='Generate now with every character', command=generate_with_all, ).grid(
    column=1, row=5, padx=10)

win.mainloop()
