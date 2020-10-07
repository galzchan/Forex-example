import tkinter as tk

from tkinter import ttk

from forex_python.converter import CurrencyCodes

from forex_python.converter import CurrencyRates

cc = CurrencyCodes()
c = CurrencyRates()

def onclick(event):
    if value.get() == 1:
        amount_result = float("{:.2f}".format(c.convert('THB', 'USD', float(input_amount.get()))))
        print(amount_result)
        label_input_result.configure(text=input_amount.get()+cc.get_symbol('THB'))
        label_output_result.configure(text=str(amount_result) + cc.get_symbol('USD'))
    elif value.get() == 2:
        amount_result = float("{:.2f}".format(c.convert('THB', 'JPY', float(input_amount.get()))))
        print(amount_result)
        label_input_result.configure(text=input_amount.get()+cc.get_symbol('THB'))
        label_output_result.configure(text=str(amount_result) + cc.get_symbol('JPY'))
    elif value.get() == 3:
        amount_result = float("{:.2f}".format(c.convert('THB', 'KRW', float(input_amount.get()))))
        print(amount_result)
        label_input_result.configure(text=input_amount.get()+cc.get_symbol('THB'))
        label_output_result.configure(text=str(amount_result) + cc.get_symbol('KRW'))
    else:
        amount_result = float("{:.2f}".format(c.convert('THB', 'EUR', float(input_amount.get()))))
        print(amount_result)
        label_input_result.configure(text=input_amount.get()+cc.get_symbol('THB'))
        label_output_result.configure(text=str(amount_result) + cc.get_symbol('EUR'))


main_window = tk.Tk()
value = tk.IntVar()

label_amount = tk.Label(main_window, text="จำนวนเงิน", bg = "yellow",font = ("Helvetica",20))
label_amount.grid(row=0, column=0)

input_amount = tk.Entry(main_window,font = ("Helvetica",20))
input_amount.grid(row=0, column=1)

label_unit = tk.Label(main_window, text="บาท",bg = "yellow",font = ("Helvetica",20))
label_unit.grid(row=0, column=2)

radio_usd = tk.Radiobutton(main_window, text="USD" + "(" + cc.get_symbol('USD') + ")", variable=value, value=1, justify=tk.LEFT,font = ("Helvetica",20))
radio_jpy = tk.Radiobutton(main_window, text="JPY" + "(" + cc.get_symbol('JPY') + ")", variable=value, value=2, justify=tk.LEFT,font = ("Helvetica",20))
radio_krw = tk.Radiobutton(main_window, text="KRW" + "(" + cc.get_symbol('KRW') + ")", variable=value, value=3, justify=tk.LEFT,font = ("Helvetica",20))
radio_eur = tk.Radiobutton(main_window, text="EUR" + "(" + cc.get_symbol('EUR') + ")", variable=value, value=4, justify=tk.LEFT,font = ("Helvetica",20))

radio_usd.grid(row=1, column=1)
radio_jpy.grid(row=2, column=1)
radio_krw.grid(row=3, column=1)
radio_eur.grid(row=4, column=1)

calc_btn = tk.Button(main_window, text="calculate",font = ("Helvetica",20))
calc_btn.bind("<Button-1>", onclick)
calc_btn.grid(row=5, column=1)

label_input_result = tk.Label(main_window, text="",font = ("Helvetica",20))
label_equal_sign = tk.Label(main_window, text="=",font = ("Helvetica",20))
label_output_result = tk.Label(main_window, text="",font = ("Helvetica",20))

label_input_result.grid(row=7, column=0)
label_equal_sign.grid(row=7, column=1)
label_output_result.grid(row=7, column=2)

main_window.mainloop()

