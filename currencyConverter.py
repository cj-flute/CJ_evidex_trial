from tkinter import *

class CurrencyConverter:
    def __init__(self):
        window = Tk()
        window.title("Currency Converter")
        window.configure(bg="yellow")
        Label(window, font="Helvetica 12 bold", bg="yellow", text="Amount to convert").grid(row=1, column=1, sticky=w)
        Label(window, font="Helvetica 12 bold", bg="yellow", text="Conversion Rate").grid(row=2, column=1, sticky=w)
        Label(window, font="Helvetica 12 bold", bg="yellow", text="Converted Amount").grid(row=3, column=1, sticky=w)
        self.amounttoConvertVar = StringVar()
        Entry(window, textvariable = self.amounttoConvertVar, justify = RIGHT).grid(row=1, column=2)
        self.conversionRateVar = StringVar()
        Entryd(window, textvariable = self.conversionRateVar, justify = RIGHT).grid(row=2, column=2)
        