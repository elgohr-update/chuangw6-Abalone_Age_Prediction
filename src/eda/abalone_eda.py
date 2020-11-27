# author: Charles Suresh
# date: 2020-11-27

"""Creates eda plots for the pre-processed training data from the Abalone Data Set (from http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data)
Saves the plots as a png file.

Usage: src/eda/abalone_eda.py --train=<train> --out_dir=<out_dir>

Options:
--train=<train>     Path (including filename) to training data
--out_dir=<out_dir> Path to directory where the plots should be saved
"""

from docopt import docopt
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

opt = docopt(__doc__)

def main(train, out_dir):
  
    train_data = pd.read_csv(train, index_col = 0)
    
    # add units to column titles
    train_data.columns = [
        "Sex",
        "Length (mm)",
        "Diameter (mm)",
        "Height (mm)",
        "Whole Weight (g)",
        "Shucked Weight (g)",
        "Viscera Weight (g)",
        "Shell Weight (g)",
        "Age (Years)",
    ]
    
    if not os.path.exists(out_dir):
      os.makedirs(out_dir)
    
    # Violin PLot of Age conditioned on 'sex'
    fig1, ax1 = plt.subplots()
    sns.violinplot(y="Sex", x="Age (Years)", data=train_data, inner="quartile", ax=ax1)
    fig1.savefig(out_dir + '/sex_vs_age_violin.png', dpi = 200)
    plt.close(fig1)
    
    # Histogram of Numerical Features
    sns.set(rc={"figure.figsize": (30, 12)}, font_scale=1.25)
    fig2, ax2 = plt.subplots(nrows=2, ncols=4)
    plt.subplots_adjust(left=0.04, right=0.975, top=0.95, bottom=0.075)
    sns.set_theme(style="whitegrid")
    sns.histplot(train_data, x="Length (mm)", kde=True, bins=15, ax=ax2[0, 0])
    sns.histplot(train_data, x="Diameter (mm)", kde=True, bins=15, ax=ax2[0, 1])
    sns.histplot(train_data, x="Height (mm)", kde=True, bins=20, ax=ax2[0, 2])
    sns.histplot(train_data, x="Whole Weight (g)", kde=True, bins=15, ax=ax2[0, 3])
    sns.histplot(train_data, x="Shucked Weight (g)", kde=True, bins=15, ax=ax2[1, 0])
    sns.histplot(train_data, x="Viscera Weight (g)", kde=True, bins=15, ax=ax2[1, 1])
    sns.histplot(train_data, x="Shell Weight (g)", kde=True, bins=15, ax=ax2[1, 2])
    fig2.delaxes(ax2[1, 3])
    plt.savefig(out_dir + '/all_vs_age_dist.png', dpi = 65)
    plt.close(fig2)
    
    # Correlation Plot
    sns.set(rc={"figure.figsize": (15, 10)}, font_scale=1.25)
    fig3, ax3 = plt.subplots()
    plt.subplots_adjust(left=0.15, right=1, top=0.95, bottom=0.2)
    num_data = train_data[list(train_data.columns)[1:]]
    sns.heatmap(
        num_data.corr(),
        annot=True,
        annot_kws={"fontsize": 15},
        vmin=-1,
        vmax=1,
        cmap="Spectral",
        linewidths=1,
        ax=ax3
    )
    plt.savefig(out_dir + '/corr_plot.png', dpi = 200)
    plt.close(fig3)

if __name__ == "__main__":
    main(opt["--train"], opt["--out_dir"])
