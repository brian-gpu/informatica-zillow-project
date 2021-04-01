import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib as plt
import logging

plt.rc('figure', figsize=(30,16))

def setup_sns(logger=logging):
    try:
        sns.set(rc={'axes.facecolor':'white', 'figure.facecolor':'white'})
        sns.despine()
    except Exception as e:
        logging.info(f'Could not setup seaborn defaults {e}')

def setup_labels(ax, title, x_label, y_label, logger=logging):
    try:
        ax.set_title(title, size=16)
        ax.set_xlabel(x_label, color='gray')
        ax.set_ylabel(y_label, color='gray')
    except Exception as e:
        logging.info(f'Could not set axis labels {e}')

def setup_grid(ax, axis, logger=logging):
    try:
        ax.tick_params(labelcolor='gray', axis=axis)
        ax.grid(color='gray', axis=axis, linestyle='dashed', linewidth=.5)
    except Exception as e:
        logging.info(f'Could not set axis grid defaults {e}')


def sort_data(data, sort_by='', asc=None, logger=logging):
    if(asc != None):
        try:
            data = data.sort_values(by=sort_by, ascending=asc)
        except Exception as e:
            logging.info(f'Could not sort data {e}')

    return data

def create_barplot(data, title, x_label, y_label, asc=None, logger=logging):
    ax = None
    
    data = sort_data(data, sort_by='data', asc=asc)

    try:
        ax = sns.barplot(x='data', y='label', data=data)
    except Exception as e:
        logging.info(f'Could not create barplot {e}')

    setup_labels(ax, title, x_label, y_label, logger)
    setup_grid(ax, 'x', logger)

    return ax

def create_stackplot(data, title, x_label, y_label, logger=logging):
    ax = None

    try:
        ax = data.set_index('Area').T.plot(kind='bar', stacked=True, color=sns.color_palette('Paired'))
    except Exception as e:
        logging.info(f'Could not create stackpot {e}')

    setup_labels(ax, title, x_label, y_label, logger)
    setup_grid(ax, 'y', logger)

    return ax

def create_lineplot(data, title, x_label, y_label, logger=logging):
    ax = None
    
    try:
        ax = data.set_index('Area').T.plot(kind='line', linewidth=1, marker='o', color=sns.color_palette('bright'))
    except Exception as e:
        logging.info(f'Could not create lineplot {e}')

    setup_labels(ax, title, x_label, y_label, logger)
    setup_grid(ax, 'y', logger)

    return ax

def save_plot(plot, destination='plot.png', logger=logging):
    setup_sns(logger)

    try:
        image = plot.get_figure()
    except Exception as e:
        logging.info(f'Could not retrieve figure {e}')
    
    try:
        image.savefig(destination, bbox_inches='tight')
    except Exception as e:
        logging.info(f'Could not save image {e}')


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