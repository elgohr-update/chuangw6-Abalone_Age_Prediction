# Abalone Age Prediction
  - author: Huanhuan Li, Chuang Wang, Charles Suresh (UBC MDS program)
## Introduction
In this project, we are going to estimate abalone's age from physical measurements. Abalone is a kind of shellfish that lives in cold water. It has great health benefits based on the fact of low fat and high protein. The nutritional value in different ages is different, as well as economic value. Therefore, telling the age of abalone is an important question for scientists, fish farmers, and customers. The traditional way to determine the age of abalone is from the number of rings. Counting the rings is a time-consuming task since it requires a tedious process involving cutting the shell, staining it, and counting the rings under the microscope. Thus, we consider using other easily obtained measures to predict the age. 

The dataset used in this project comes from an original study "The Population Biology of Abalone (_Haliotis_ species) in Tasmania. I. Blacklip Abalone (_H. rubra_) from the North Coast and Islands of Bass Strait", created by Warwick J Nash, Tracy L Sellers, Simon R Talbot, Andrew J Cawthorn and Wes B Ford (1994). It was sourced from the UCI Machine Learning Repository and can be found [here](http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/). Each row in the data set represents an abalone, including the physical measurements(Sex, Length, Diameter, Height, Whole weight, etc.) and the number of rings, which gives the age in years by adding 1.5. The missing values in the original study have been removed and the range of continuous values has been scaled. Please find the detailed information [here](http://archive.ics.uci.edu/ml/datasets/Abalone?pagewanted=all).

We plan to build a predictive model to answer the question we propose above. Before building the predictive model, to make the target more understandable, we will convert our target "rings" to "age" by adding 1.5. We will split the data into a training set and a test set (split 80%:20%). The data set is clean as the missing values have been removed and the continuous values have been scaled. The features and target variable are all continuous, thus the exploratory data analysis will focus on the distribution of the features and the correlations between the features. Please find the detailed EDA [heare](https://github.com/UBC-MDS/Abalone_Age_Prediction/blob/main/src/abalone_eda.ipynb)

Given that all the features and target are continuous, firstly we plan to explore Ridge model, which is a regularized linear regression model. Ridge model can avoid predicting extremely large numbers because the normal age of abalone is smaller than 50. We will apply hyperparameter optimization to choose the best hyperparameter alpha via cross-validation. The prediction will be evaluated by comparing different metrics(r2, MSE, etc.). Another regressor that could potentially perform well is RandomForestRegressor. We can also carry out hyperparameter optimization and choose the best hyperparameter. At last, we will choose the best model.

We will apply the best model we selected to the test data set. We will evaluate the performance of the test data set in different metrics. The metrics and interpretation will be reported in our final report.


## Usage

To replicate the analysis, clone this GitHub repository, install the [dependencies](#dependencies) listed below, and run `run.sh` from the root directory of this project.

## Dependencies

Please refer to `env-abalone.yml` under the root directory of this project. 
## License
MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# References

<div id="refs" class="references">

<div id="ref-Dua2019">

- Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

- Data comes from an original (non-machine-learning) study:
Warwick J Nash, Tracy L Sellers, Simon R Talbot, Andrew J Cawthorn and Wes B Ford (1994)
"The Population Biology of Abalone (_Haliotis_ species) in Tasmania. I. Blacklip Abalone (_H. rubra_) from the North Coast and Islands of Bass Strait",
Sea Fisheries Division, Technical Report No. 48 (ISSN 1034-3288)

- Sam Waugh (1995) "Extending and benchmarking Cascade-Correlation", PhD thesis, Computer Science Department, University of Tasmania.
[Web Link]

- David Clark, Zoltan Schreter, Anthony Adams "A Quantitative Comparison of Dystal and Backpropagation", submitted to the Australian Conference on Neural Networks (ACNN'96).

</div>

</div>