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
    """Runs all helper functions to save a violin plot, a histogram
    plot and a correlation plot in the output directory

    Parameters
    ----------
    train : string
        the path (including file name) to the training data

    out_dir : string
        the output directory
    """
    train_data = pd.read_csv(train, index_col=0)

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
    violin_plot(train_data, out_dir)

    # Histogram of Numerical Features
    histogram_plot(train_data, out_dir)

    # Correlation Plot
    correlation_plot(train_data, out_dir)


def violin_plot(train_data, out_dir):
    """Plots a violin plot for the "Age (Years)" column conditioned
    on "Sex" and saves it in the output directory

    Parameters
    ----------
    train_data : pandas dataframe
        A dataframe containing  "Age (Years)" column of numeric type and
        "Sex" column of String type

    out_dir : string
        the output directory

    Returns
    -------
    None

    Examples
    --------
    >>> violin_plot(df, 'src/eda')
    """
    fig, ax = plt.subplots()
    sns.violinplot(y="Sex", x="Age (Years)", data=train_data, inner="quartile")
    ax.set_yticklabels(["Infant", "Male", "Female"])
    fig.savefig(out_dir + "/sex_vs_age_violin.png", dpi=200)
    plt.close(fig)


def histogram_plot(train_data, out_dir):
    """Plots a histogrom of all numeric features and saves it
    in the output directory

    Parameters
    ----------
    train_data : pandas dataframe
        A dataframe containing numeric columns
    
    out_dir : string
        the output directory

    Returns
    -------
    None

    Examples
    --------
    >>> histogram_plot(df, 'src/eda')
    """

    sns.set(rc={"figure.figsize": (30, 20)}, font_scale=1.8)
    fig, axs = plt.subplots(nrows=3, ncols=3)
    plt.subplots_adjust(left=0.04, right=0.975, top=0.95, bottom=0.075)
    sns.set_theme(style="whitegrid")

    for i, column in enumerate(train_data.drop(columns=["Sex"]).columns):
        sns.histplot(train_data[column], kde=True, bins=15, ax=axs[(i // 3, i % 3)])

    fig.delaxes(axs[2, 2])
    plt.savefig(out_dir + "/all_vs_age_dist.png", dpi=90)
    plt.close(fig)


def correlation_plot(train_data, out_dir):
    """Plots a correlation plot of all numeric features and
     saves it in the output directory

    Parameters
    ----------
    train_data : pandas dataframe
        A dataframe containing atleast two numeric columns

    out_dir : string
        the output directory

    Returns
    -------
    None

    Examples
    --------
    >>> correlation_plot(df, 'src/eda')
    """
    sns.set(rc={"figure.figsize": (15, 10)}, font_scale=1.25)
    fig, ax = plt.subplots()
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
    )
    plt.savefig(out_dir + "/corr_plot.png", dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    main(opt["--train"], opt["--out_dir"])
