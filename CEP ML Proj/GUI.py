from Data import *
from Algorithm import *

import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import statsmodels.api as sm
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# tkinter GUI
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 500, height = 300)
canvas1.pack()

# with sklearn
Intercept_result = ('Intercept: ', regr.intercept_)
label_Intercept = tk.Label(root, text=Intercept_result, justify = 'center')
canvas1.create_window(260, 220, window=label_Intercept)

# with sklearn
Coefficients_result  = ('Coefficients: ', regr.coef_)
label_Coefficients = tk.Label(root, text=Coefficients_result, justify = 'center')
canvas1.create_window(260, 240, window=label_Coefficients)

# New_Interest_Rate label and input box
label1 = tk.Label(root, text='Type Past Failures: ')
canvas1.create_window(100, 100, window=label1)

entry1 = tk.Entry (root) # create 1st entry box
canvas1.create_window(270, 100, window=entry1)

# New_Unemployment_Rate label and input box
label2 = tk.Label(root, text=' Type Studytime in hours: ')
canvas1.create_window(120, 120, window=label2)

entry2 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(270, 120, window=entry2)

def values():
    global New_failure #our 1st input variable
    New_failure = float(entry1.get())

    global New_studytime #our 2nd input variable
    New_studytime = float(entry2.get())

    Prediction_result  = ('Predicted Grade: ', regr.predict([[New_failure ,New_studytime]]))
    label_Prediction = tk.Label(root, text= Prediction_result, bg='orange')
    canvas1.create_window(260, 280, window=label_Prediction)

button1 = tk.Button (root, text='Predict your Grade!',command=values, bg='orange') # button to call the 'values' command above
canvas1.create_window(270, 150, window=button1)

#plot 1st scatter
figure3 = plt.Figure(figsize=(5,4), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df['failures'].astype(float),df['G_ave'].astype(float), color = 'r')
scatter3 = FigureCanvasTkAgg(figure3, root)
scatter3.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
ax3.legend(['Grades'])
ax3.set_xlabel('failures')
ax3.set_title('Failures Vs. Grades')

#plot 2nd scatter
figure4 = plt.Figure(figsize=(5,4), dpi=100)
ax4 = figure4.add_subplot(111)
ax4.scatter(df['studytime'].astype(float),df['G_ave'].astype(float), color = 'g')
scatter4 = FigureCanvasTkAgg(figure4, root)
scatter4.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
ax4.legend(['Grades'])
ax4.set_xlabel('studytime')
ax4.set_title('Studytime Vs. Grades')

root.mainloop()
