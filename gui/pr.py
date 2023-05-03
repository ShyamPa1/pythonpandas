import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
id=[1,2,3,4,5,6,7,8,9,10]
value=[10,20,30,40,50,60,70,80,90,100]
d={"id":id,"value":value}
# Load data from CSV file using pandas
data = pd.DataFrame(d)

# Create a list of column names for the user to select
columns = list(data.columns)

# Create a tkinter GUI
root = Tk()

# Create a drop-down menu for column selection
variable = StringVar(root)
variable.set(columns[0])  # default value
dropdown = OptionMenu(root, variable, *columns)
dropdown.pack()

# Create entry fields for filters
filter1 = Entry(root)
filter2 = Entry(root)
filter1.pack()
filter2.pack()

# Create a button to update the chart
def update_chart():
    col = variable.get()
    val1 = filter1.get()
    val2 = filter2.get()
    filtered_data = data[(data[col] > int(val1)) & (data[col] < int(val2))]
    plt.plot(filtered_data[col])
    plt.show()

button = Button(root, text="Update Chart", command=update_chart)
button.pack()

root.mainloop()
