# run_all.sh 
# Chuang Wang, Nov 2020
# 
# description
# 
# Usage: bash run_all.sh

# download the raw data froom UCI website
python src/data_wrangling/download_data.py --url=https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data --out_file_path=data/raw/abalone.csv

# preprocess the data and split it into train and test set 
python src/data_wrangling/pre_process_abalone_data.py --input=data/raw/abalone.csv --out_dir=data/processed

# run EDA process
python src/eda/abalone_eda.py --train=data/processed/training.csv --out_dir=results/eda

# train ML model and plot hyperparameter tuning result
python src/ml/abalone_fit_predict_model.py --train=data/processed/training.csv --out_dir=results/ml_model