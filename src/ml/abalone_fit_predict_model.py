# author: Chuang Wang
# date: 2020-11-28

"""
Fits a Ridge model on the pre-processed training data from the UCI Abalone Data Set 
(from https://archive.ics.uci.edu/ml/datasets/abalone).
Saves the model as a sav file.
Usage: src/ML/abalone_fit_predict_model.py --train=<train> --out_dir=<out_dir>
  
Options:
--train=<train>     Path (including filename) to training data (csv file)
--out_dir=<out_dir> Path to directory where the serialized model should be written
"""

from docopt import docopt
from sklearn.linear_model import Ridge
from sklearn.model_selection import RandomizedSearchCV
from sklearn.compose import make_column_transformer
from sklearn.pipeline import FeatureUnion, Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

opt = docopt(__doc__)


def main(input_file, out_dir):
    # find the best Ridge model and the hyperparameter tuning result
    best_ridge, result_df = find_best_model(input_file)

    # write the serialized best model into a sav file
    pickle.dump(best_ridge, open(out_dir + "/ridge_pipe.sav", "wb"))

    # save the hyperparameter tuning plot
    plot_save(result_df, out_dir + "/hyperparam_tuning.png")


def find_best_model(input_file):
    raw = pd.read_csv(input_file)
    train_df = preprocess(raw)
    train_df = train_df[train_df["Height"] < 0.6]
    X_train, y_train = train_df.drop(columns=["Age"]), train_df["Age"]
    ridge_pipe = get_pipeline()
    return hyperparam_tuning(ridge_pipe, X_train, y_train)


def plot_save(result_df, out_dir):
    result_df.plot(kind="line", y="mean_test_score")
    plt.xlabel("Hyperparameter Alpha")
    plt.ylabel("Mean Test Score")
    plt.savefig(out_dir)


def hyperparam_tuning(pipe, X_train, y_train):
    param_dist = {"ridge__alpha": 2.0 ** np.arange(-5, 5, 1)}
    random_search = RandomizedSearchCV(
        pipe, param_distributions=param_dist, n_jobs=-1, n_iter=10, cv=5, scoring="r2",
    )
    random_search.fit(X_train, y_train)
    best_ridge = random_search.best_estimator_
    result_df = (
        pd.DataFrame(random_search.cv_results_)[
            ["param_ridge__alpha", "mean_test_score", "rank_test_score",]
        ]
        .set_index("param_ridge__alpha")
        .sort_index()
    )
    return best_ridge, result_df


def preprocess(raw):
    raw.columns = [
        "Sex",
        "Length",
        "Diameter",
        "Height",
        "Whole Weight",
        "Shucked Weight",
        "Viscera Weight",
        "Shell Weight",
        "Age",
    ]
    raw["Age"] = raw["Age"] + 1.5
    return raw


def get_pipeline():
    categorical_features = ["Sex"]
    numerical_features = [
        "Length",
        "Diameter",
        "Height",
        "Whole Weight",
        "Shucked Weight",
        "Viscera Weight",
        "Shell Weight",
    ]
    preprocessor = make_column_transformer(
        (StandardScaler(), numerical_features), (OneHotEncoder(), categorical_features)
    )

    return make_pipeline(preprocessor, Ridge())


if __name__ == "__main__":
    main(opt["--train"], opt["--out_dir"])

