# author: Charles Suresh
# date: 2020-11-27

"""Cleans, pre-processes splits the Abalone Data Set (from http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data).
Writes the training and test data to separate csv files.

Usage: src/data_wrangling/pre_process_abalone_data.py --input=<input> --out_dir=<out_dir>

Options:
--input=<input>       Path (including filename) to raw data (csv file)
--out_dir=<out_dir>   Path to directory where the processed data should be written
"""

from docopt import docopt
import os
import pandas as pd
from sklearn.model_selection import train_test_split

opt = docopt(__doc__)

def main(input, out_dir):
    # original dataset
    abalone = pd.read_csv(input)
    
    # add columns' titles to the dataframe
    abalone.columns = [
        "Sex",
        "Length",
        "Diameter",
        "Height",
        "Whole Weight",
        "Shucked Weight",
        "Viscera Weight",
        "Shell Weight",
        "Rings",
    ]
    
    # transform the columm `Rings` to `Age` by adding 1.5 (according to the dataset description file)
    abalone["Age"] = abalone["Rings"] + 1.5
    abalone = abalone.drop(columns = "Rings")

    # split the dataset to train set and test set
    train_df, test_df = train_test_split(abalone, test_size = 0.2, random_state = 123)
    
    if not os.path.exists(out_dir):
      os.makedirs(out_dir)
    
    train_df.to_csv(out_dir + '/training.csv')
    test_df.to_csv(out_dir + '/test.csv')

if __name__ == "__main__":
    main(opt["--input"], opt["--out_dir"])
    
