# run_all.sh 
# Chuang Wang, Nov 2020
# 
# description
# 
# Usage: bash run_all.sh



# train ML model and plot hyperparameter tuning result
python src/ml/abalone_fit_predict_model.py --train=data/raw/abalone.csv --out_dir=results/ml_model