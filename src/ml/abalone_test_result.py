# author: Chuang Wang
# date: 2020-11-28

"""
Assesses model's accuracy on a test data set.
Usage: src/ml/abalone_test_result.py --test=<test> --out_dir=<out_dir>

Options:
--test=<test>          Path (including filename) to test data (csv file)
--out_dir=<out_dir>    Path to directory where the test result should be saved
"""

from docopt import docopt
from sklearn.linear_model import Ridge
from sklearn.model_selection import RandomizedSearchCV, cross_validate
from sklearn.compose import make_column_transformer
from sklearn.pipeline import FeatureUnion, Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import make_scorer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

opt = docopt(__doc__)


def main(test, out_dir):
    test_df = pd.read_csv(test)
    loaded_model = pickle.load(open("results/ml_model/best_predict_model.sav", "rb"))
    result = test_model(loaded_model, test_df)
    print(result)


def test_model(loaded_model, test_df):
    scores = {"ML model": "Ridge"}
    X_test, y_test = test_df.drop(columns=["Age"]), test_df["Age"]
    scores["mape_score"] = [mape(y_test, loaded_model.predict(X_test))]
    scores["r_squared_score"] = [loaded_model.score(X_test, y_test)]
    return pd.DataFrame(scores).set_index("ML model")


def mape(true, pred):
    return 100.0 * np.mean(np.abs((pred - true) / true))


if __name__ == "__main__":
    main(opt["--test"], opt["--out_dir"])

