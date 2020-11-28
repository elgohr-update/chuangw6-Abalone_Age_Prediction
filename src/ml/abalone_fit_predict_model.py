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
    """run all helper functions to find the best model and get the 
    hyperparameter tuning result

    Parameters
    ----------
    input_file : string
        the path (including file name) to the training dataset
    out_dir : string
        the path to store the results
    """
    best_ridge, result_df = find_best_model(input_file)

    # write the serialized best model into a sav file
    pickle.dump(best_ridge, open(out_dir + "/best_predict_model.sav", "wb"))

    # save the hyperparameter tuning plot
    plot_save(result_df, out_dir + "/hyperparam_tuning.png")


def find_best_model(input_file):
    """find the best model `Ridge` which is a machine learning (ML) linear 
    regression model 

    Parameters
    ----------
    input_file : string
        the path (including file name) to the training dataset 

    Returns
    -------
    best_ridge, result_df : tuple
        a tuple that contains the best ridge model object and the tuning 
        result dataframe
    """
    train_df = pd.read_csv(input_file)
    train_df = train_df[train_df["Height"] < 0.6]
    X_train, y_train = train_df.drop(columns=["Age"]), train_df["Age"]

    # construct a ML pipeline
    pipe = get_pipeline()

    # tune the hyperparameter alpha using RandomizedSearchCV
    param_dist = {"ridge__alpha": 2.0 ** np.arange(-10, 10, 1)}
    random_search = RandomizedSearchCV(
        pipe,
        param_distributions=param_dist,
        n_jobs=-1,
        n_iter=10,
        cv=5,
        scoring="r2",
        random_state=2020,
    )
    random_search.fit(X_train, y_train)
    best_ridge = random_search.best_estimator_
    result_df = (
        pd.DataFrame(random_search.cv_results_)[
            ["param_ridge__alpha", "mean_test_score", "rank_test_score",]
        ]
        .set_index("rank_test_score")
        .sort_index()
    )
    return best_ridge, result_df


def get_pipeline():
    """construct a ML pipeline which contains preprocessors for different 
    features and a ML model

    Returns
    -------
    sklearn.pipeline.Pipeline
        ML pipeline
    """
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


def plot_save(result_df, out_dir):
    """plot the hyperparameter result and save it in the result folder

    Parameters
    ----------
    result_df : pandas.core.frame.DataFrame
        a dataframe containing the hyperparameter result
    out_dir : string
        the path to store the results
    """
    result_df.plot(kind="line", y="mean_test_score")
    best_alpha = result_df.loc[1, "param_ridge__alpha"]
    best_score = result_df.loc[1, "mean_test_score"]
    plt.xlabel("Hyperparameter Alpha")
    plt.ylabel("Mean Test Score")
    plt.annotate(
        f"Best R^2 score: {best_score:.2f} where 'alpha' = {best_alpha:.1f}",
        xy=(best_alpha, best_score),
        xytext=(30, 50),
        va="top",
        xycoords="data",
        textcoords="offset points",
        bbox=dict(boxstyle="round4,pad=.5", fc="0.9"),
        arrowprops=dict(
            arrowstyle="->", connectionstyle="angle,angleA=0,angleB=80,rad=20"
        ),
    )
    plt.plot(best_alpha, best_score, "g*", color="red")
    plt.savefig(out_dir)


if __name__ == "__main__":
    main(opt["--train"], opt["--out_dir"])

