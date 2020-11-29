# run_all.sh 
# -------------------
# Author: Chuang Wang
# -------------------
# Date: Nov 28 2020
# -------------------


# Purpose:
# ------------
# This driver script runs all the scripts (.py files) and the final report 
# (.Rmd) file from downloading raw data, preprocessing data, EDA, training and
# testing machine learning model, and finally generating report.
# 
# Usage:
# -------------------
# bash run_all.sh

# 1. download the raw data froom UCI website
python src/data_wrangling/download_data.py --url=https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data --out_file_path=data/raw/abalone.csv

# 2. preprocess the data and split it into train and test set 
python src/data_wrangling/pre_process_abalone_data.py --input=data/raw/abalone.csv --out_dir=data/processed

# 3. run EDA process
python src/eda/abalone_eda.py --train=data/processed/training.csv --out_dir=results/eda

# 4. train the ML model and plot hyperparameter tuning result
python src/ml/abalone_fit_predict_model.py --train=data/processed/training.csv --out_dir=results/ml_model

# 5. test the ML model on the test dataset and store the scores
python src/ml/abalone_test_result.py --test=data/processed/test.csv --out_dir=results/ml_model

# 6. knit final report
Rscript -e "rmarkdown::render('doc/abalone_age_predict_report.Rmd', 'all', quiet=TRUE)"
