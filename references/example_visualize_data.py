import pandas as pd
import matplotlib as plt
from visualize_data import create_barplot, create_lineplot, create_stackplot, save_plot

# ----------Example Usage----------
# Set the figure size
plt.rc('figure', figsize=(30,16))

# Set dataframe and labels
x_label = 'Sales'
y_label = 'Homes'
title = 'Number of Home Sales'
data = pd.read_csv("./data1.csv")

# Barplot
plot = create_barplot(data, title, x_label, y_label, False)
save_plot(plot, 'barplot.png')

# Set dataframe and labels
x_label = 'Homes'
y_label = 'Sales'
title = 'Number of Home Sales'
data = pd.read_csv("./data2.csv")

# Stackplot
plot = create_stackplot(data, title, x_label, y_label)
save_plot(plot, 'stackplot.png')

# Lineplot
plot = create_lineplot(data, title, x_label, y_label)
save_plot(plot, 'lineplot.png')