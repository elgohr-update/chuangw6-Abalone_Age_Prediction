# Makefile
# -------------------
# Author: Chuang Wang
# -------------------
# Date: Dec 5 2020
# -------------------


# Purpose:
# ------------
# This driver script runs all the scripts (.py files) and the final report 
# (.Rmd) file from downloading raw data, preprocessing data, EDA, training and
# testing machine learning model, and finally generating report.
# 
# Usage:
# -------------------
# make all

all : doc/abalone_age_predict_report.html doc/abalone_age_predict_report.md

# 1. download the raw data froom UCI website
data/raw/abalone.csv : src/data_wrangling/download_data.py
	if [ ! -d "data/" ]; then mkdir data; fi
	if [ ! -d "data/raw/" ]; then mkdir data/raw; fi
	python src/data_wrangling/download_data.py --url=https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data --out_file_path=data/raw/abalone.csv

# 2. preprocess the data and split it into train and test set 
data/processed/test.csv data/processed/training.csv : src/data_wrangling/pre_process_abalone_data.py data/raw/abalone.csv
	if [ ! -d "data/processed/" ]; then mkdir data/processed; fi
	python src/data_wrangling/pre_process_abalone_data.py --input=data/raw/abalone.csv --out_dir=data/processed

# 3. run EDA process
results/eda/all_vs_age_dist.png results/eda/corr_plot.png results/eda/sex_vs_age_violin.png : src/eda/abalone_eda.py data/processed/training.csv
	if [ ! -d "results/" ]; then mkdir results; fi
	if [ ! -d "results/eda/" ]; then mkdir results/eda; fi
	python src/eda/abalone_eda.py --train=data/processed/training.csv --out_dir=results/eda

# 4. train the ML model and plot hyperparameter tuning result
results/ml_model/best_predict_model.sav results/ml_model/hyperparam_tuning.png : src/ml/abalone_fit_predict_model.py data/processed/training.csv 
	if [ ! -d "results/ml_model/" ]; then mkdir results/ml_model; fi
	python src/ml/abalone_fit_predict_model.py --train=data/processed/training.csv --out_dir=results/ml_model

# 5. test the ML model on the test dataset and store the scores
results/ml_model/best_model_quality.sav : src/ml/abalone_test_result.py data/processed/test.csv results/ml_model/best_predict_model.sav
	python src/ml/abalone_test_result.py --test=data/processed/test.csv --out_dir=results/ml_model

# 6. knit final report
doc/abalone_age_predict_report.html doc/abalone_age_predict_report.md : doc/abalone_age_predict_report.Rmd results/ml_model/best_model_quality.sav results/ml_model/hyperparam_tuning.png results/eda/all_vs_age_dist.png results/eda/corr_plot.png results/eda/sex_vs_age_violin.png
	Rscript -e "rmarkdown::render('doc/abalone_age_predict_report.Rmd', 'all', quiet=TRUE)"


clean :
	rm -rf data/raw/abalone.csv
	rm -rf data/processed/test.csv data/processed/training.csv
	rm -rf results/eda/all_vs_age_dist.png results/eda/corr_plot.png results/eda/sex_vs_age_violin.png
	rm -rf results/ml_model/best_predict_model.sav results/ml_model/best_model_quality.sav results/ml_model/hyperparam_tuning.png 
	rm -rf doc/abalone_age_predict_report.html doc/abalone_age_predict_report.md