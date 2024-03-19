# Assignment header
"""
Austin Maxwell
February 24, 2024
Spring 2024 - Data 51100 - Section 002
Programming Assignment #6
"""

# Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# Initialize variables needed for algorithm
pums_data = r'/Users/austinmaxwell/ss13hil.csv'
pums_fig = r'/Users/austinmaxwell/pums.png'
pie_chart_labels = ["English only", 'Spanish',
                    "Other Indo-European",
                    "Asian and Pacific Island languages",
                    'Other']
tax_dict = {1:0, 2:1, 3:50, 4:100, 5:150, 6:200,7:350, 8:300, 9:350, 10:400,
            11:450, 12:500, 13:550, 14:600, 15:650, 16:700, 17:750, 18:800,
            19:850, 20:900, 21:950, 22:1000, 23:1100, 24:1200, 25:1300,
            26:1400, 27:1500, 28:1600, 29:1700, 30:1800, 31:1900, 32:2000,
            33:2100, 34:2200, 35:2300, 36:2400, 37:2500, 38:2600, 39:2700,
            40:2800, 41:2900, 42:3000, 43:3100, 44:3200, 45:3300, 46:3400,
            47:3500, 48:3600, 49:3700, 50:3800, 51:3900, 52:4000, 53:4100,
            54:4200, 55:4300, 56:4400, 57:4500, 58:4600, 59:4700, 60:4800,
            61:4900, 62:5000, 63:5500, 64:6000, 65:7000, 66:8000, 67:9000,
            68:10000}

# Load the ss13hil.csv file into DataFrame
pums_df = pd.read_csv(pums_data)

# Create a figure with 2x2 subplots
fig, axis = plt.subplots(2, 2, figsize=(20.5,15))
fig.suptitle("Sample Output", fontsize=20, fontweight= 'bold', y=0.93)

## Create and populate Pie Chart Subplot (Upper Left)
top_left = axis[0,0]
top_left.pie(pums_df['HHL'].value_counts(), radius=1.2, startangle=243)
top_left.set_title("Household Languages", fontsize='x-large')
top_left.set_ylabel('HHL', labelpad=50, fontsize='large')
top_left.legend(labels=pie_chart_labels,
                 loc="upper left",
                 bbox_to_anchor=(-0.3,1,1,0.005),
                 fontsize='large')

## Create and populate Histogram Subplot (Upper Right)
top_right = axis[0,1]
top_right.hist(pums_df['HINCP'],
               density=True,
               bins=np.logspace(1,7,num=100,base=10),
               alpha=0.45,
               color='green')
sns.kdeplot(pums_df['HINCP'],
            ax=axis[0,1],
            color='black',
            linestyle='--',
            linewidth=3,
            )
top_right.grid(True)
top_right.set_title("Distribution of Household Income", fontsize='x-large')
top_right.set_xlabel("Household Income($)- Log Scaled", fontsize='large')
top_right.set_ylabel('Density', fontsize='large')
top_right.set_xscale('log')
top_right.yaxis.set_major_formatter(plt.FormatStrFormatter('%.6f'))


## Create and populate Bar Chart Subplot (Lower Left)
bottom_left = axis[1,0]
bar_chart_df = pums_df['WGTP'].groupby(pums_df['VEH'].dropna()).sum()/1000
bottom_left.bar(bar_chart_df.index,
              height=bar_chart_df,
              color='red')
bottom_left.set_title("Vehicles Available for Households", fontsize='x-large')
bottom_left.set_xlabel("# of Vehicles", fontsize='large')
bottom_left.set_ylabel('Thousands of Households', fontsize='large')

## Create and populate Scatterplot Subplot (Lower Right)
bottom_right = axis[1,1]
test = bottom_right.scatter(pums_df['VALP'],
                  pums_df['TAXP'].replace(tax_dict),
                  s=pums_df['WGTP'],
                  c=pums_df['MRGP'],
                  marker='o',
                  cmap='seismic',
                  alpha=0.175)
fig.colorbar(test,
             label="First Mortgage Payment (Monthly $)",
             orientation='vertical',
             ax=bottom_right)
bottom_right.set_title("Property Taxes vs Property Values", fontsize='x-large')
bottom_right.set_xlabel("Property Value($)", fontsize='large')
bottom_right.set_ylabel("Taxes($)", fontsize='large')
bottom_right.set_xlim(0,1200000)
bottom_right.set_ylim(0,11000)
bottom_right.ticklabel_format(axis='both', style='plain')

# Output the visualizations to a png file
plt.savefig(pums_fig, orientation='landscape')
