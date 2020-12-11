Predicting abalone age from physical measurements
================
Huanhuan Li, Chuang Wang, Charles Suresh </br>
2020/11/28 (updated: 2020-12-11)

-   [Summary](#summary)
-   [Methods](#methods)
    -   [Data](#data)
    -   [Analysis](#analysis)
-   [Results & Discussion](#results-discussion)
-   [Results & Discussion](#results-discussion-1)
-   [Further improvement](#further-improvement)
-   [Reference](#reference)

# Summary

To predict abalone’s age from physical measurements, we build a
regression model using a popular type of regularized linear regression
model Ridge. The model can use physical measurements (Sex, Length,
Diameter, Height, Whole weight, etc.) to predict the age of abalone. Our
final Ridge model can predict age in a decent accuracy on an unseen test
data set, with a R-squared score of 0.52 and a mean absolute percentage
error (MAPE) of 13.71. However, considering the potential economic
losses to the stakeholders (Cook and Gordon 2010), we recommend further
improvement before it is put into the industry.

# Methods

## Data

The dataset used in this project comes from an original study “The
Population Biology of Abalone (*Haliotis* species) in Tasmania. I.
Blacklip Abalone (*H. rubra*) from the North Coast and Islands of Bass
Strait,” created by Warwick J Nash, Tracy L Sellers, Simon R Talbot,
Andrew J Cawthorn and Wes B Ford (1994). It was sourced from the UCI
Machine Learning Repository (Dua and Graff 2017) and can be found
[here](http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/).
Each row in the data set represents an abalone, including the physical
measurements (Sex, Length, Diameter, Height, Whole weight, etc.) and the
number of rings, which gives the age in years by adding 1.5. The missing
values in the original study have been removed and the range of
continuous values has been scaled. Please find the detailed information
[here](http://archive.ics.uci.edu/ml/datasets/Abalone?pagewanted=all).

## Analysis

The Ridge model was used to build a regression model to predict abalone
age based on the physical measures, which involve 1 categorical feature
(“Sex”), and 7 numerical features (“Length,” “Diameter,” “Height,”
“Whole weight,” “Shucked weight,” “Viscera weight,” and “Shell weight”).
All features are contained in the original data set. The predicting
target “age” is converted from the “rings” in the original data set by
adding 1.5. Before fitting the model, we exclude 1 outlier with
extremely large height, and apply a standard scale transformation on
numerical features. The model parameter *a**l**p**h**a* was chosen using
a randomized search on hyperparameters in 5-fold cross-validation, with
R-squared score as the evaluation metric.

The Python programming languages (Van Rossum and Drake 2009) and the
following Python packages were used to perform the analysis: Docopt
(Keleshev 2014), Pandas (McKinney and others 2010), Seaborn (Waskom et
al. 2017), Scikit-learn (Pedregosa et al. 2011), Numpy (Oliphant 2006),
Pickle (Van Rossum 2020), Matplotlib (Hunter 2007). The R language
programming languages (R Core Team 2019), Knitr (Xie 2014), and
Reticulate (Allaire et al. 2017) were used to generate this report. The
code used to perform the analysis and create this report can be found
here: <https://github.com/UBC-MDS/Abalone_Age_Prediction>.

# Results & Discussion

To determine which features are useful to predict the target, we explore
all columns in the train data set. From the correlation heat map below,
we can see that the shell weight is the feature that is most correlated
to the target Age because the correlation value is the largest among all
features. All numerical features have a positive relationship with each
other.

<div class="figure">

<img src="../results/eda/corr_plot.png" alt="Figure 1. Correlation of All Abalone Numerical Column." width="100%" />
<p class="caption">
Figure 1. Correlation of All Abalone Numerical Column.
</p>

</div>

To examine the correlation between the target Age and numerical
features, we take a further step to plot the histogram plot below. We
can see that the target Age is positively correlated with all the
numerical features. From the distributions, we can see that all feature
values are not normally distributed. There are some outliers for the
Height value, but we will exclude outliers from the training dataset
before building models. The feature “Whole Weight” distributes from 0 to
2.5, which is a wider range than other features. Other features
distribute from 0 to around 1. Thus, we are going to standardize the
numerical values before fitting the model.

<div class="figure">

<img src="../results/eda/all_vs_age_dist.png" alt="Figure 2. Correlation of Abalone Age with Numerical Features." width="100%" />
<p class="caption">
Figure 2. Correlation of Abalone Age with Numerical Features.
</p>

</div>

Then we explore the age distribution conditioning by different Sex. The
number of instances of Infants, Males and Females are pretty close to
each other. The mean, median, 25% Quartile and 75% Quartile of Age for
Infants are all lower than that for Males and Females. This categorical
feature is relationship indicator of age.

<div class="figure">

<img src="../results/eda/sex_vs_age_violin.png" alt="Figure 3. Correlation of Abalone Age with Sex." width="50%" />
<p class="caption">
Figure 3. Correlation of Abalone Age with Sex.
</p>

</div>

In summary, after exploring the data, we can clearly see that all
features have a relationship with the target. Thus, we are going to use
all features as the model input.

# Results & Discussion

We chose to use Ridge model to solve the regression problem. To find the
best hyperparameter, we randomly search within the defined search space
of “alpha” using 5-fold cross-validation. The evaluation metric used in
the cross-validation is R-squared score, which indicates the variation
in the response variable around its mean. The best mean validate score
is 0.54 where ‘alpha’ equals 1.

<div class="figure">

<img src="../results/ml_model/hyperparam_tuning.png" alt="Figure 4. Results from 5-fold cross validation to choose alpha. R-squared was used as the metric as alpha was varied." width="50%" />
<p class="caption">
Figure 4. Results from 5-fold cross validation to choose alpha.
R-squared was used as the metric as alpha was varied.
</p>

</div>

The final prediction model has a R-squared score of 0.52 and a mean
absolute percentage error (MAPE) of 13.71. Our R-squared score is not
good enough compare to the perfect R-squared score of 1, which means our
prediction has a relatively large variation in the response variable
around its mean. Considering the MAPE score, the model has around 13.71%
errors on the age prediction. In terms of MAPE score, the model performs
good based on the test data. However, this model is not good enough to
implement in industry or other fields.

|       | mape\_error | r\_squared\_score |
|:------|------------:|------------------:|
| Ridge |    13.71356 |         0.5193807 |

Table 1. Model Performance on Test Data

# Further improvement

We consider that the physical measurements might not be linearly
increased by age. The true underlying relationship is more complex than
a linear relationship considering multiple features. We suggest the
following methods to enhance the model performance for further
improvement. First, we could treat the age prediction as a
classification problem by binning the age into several age classes.
Second, we could further investigate the collinear features (features
that are highly correlated with one another (Kiers and Smilde 2007)), or
the outliers in each feature. We could also apply other feature
engineering techniques, such as polynomial regression or feature
interaction, to find a better fit. Last, for the reason of the collinear
relationship between features, we may reduce features using feature
selection methods to simplify the model.

# Reference

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-reticulate" class="csl-entry">

Allaire, JJ, Kevin Ushey, Yuan Tang, and Dirk Eddelbuettel. 2017.
*Reticulate: R Interface to Python*.
<https://github.com/rstudio/reticulate>.

</div>

<div id="ref-abalone" class="csl-entry">

Cook, Peter A., and H. Roy Gordon. 2010. “<span class="nocase">World
Abalone Supply, Markets, and Pricing</span>.” *Journal of Shellfish
Research* 29 (3): 569–71. <https://doi.org/10.2983/035.029.0303>.

</div>

<div id="ref-Dua2019" class="csl-entry">

Dua, Dheeru, and Casey Graff. 2017. “UCI Machine Learning Repository.”
University of California, Irvine, School of Information; Computer
Sciences. <http://archive.ics.uci.edu/ml>.

</div>

<div id="ref-hunter2007matplotlib" class="csl-entry">

Hunter, John D. 2007. “Matplotlib: A 2d Graphics Environment.”
*Computing in Science & Engineering* 9 (3): 90–95.

</div>

<div id="ref-docoptpython" class="csl-entry">

Keleshev, Vladimir. 2014. *Docopt: Command-Line Interface Description
Language*. <https://github.com/docopt/docopt>.

</div>

<div id="ref-kiers2007comparison" class="csl-entry">

Kiers, Henk AL, and Age K Smilde. 2007. “A Comparison of Various Methods
for Multivariate Regression with Highly Collinear Variables.”
*Statistical Methods and Applications* 16 (2): 193–228.

</div>

<div id="ref-pandas" class="csl-entry">

McKinney, Wes, and others. 2010. “Data Structures for Statistical
Computing in Python.” In *Proceedings of the 9th Python in Science
Conference*, 445:51–56. Austin, TX.

</div>

<div id="ref-numpy" class="csl-entry">

Oliphant, Travis E. 2006. *A Guide to NumPy*. Vol. 1. Trelgol Publishing
USA.

</div>

<div id="ref-sklearn" class="csl-entry">

Pedregosa, Fabian, Gaël Varoquaux, Alexandre Gramfort, Vincent Michel,
Bertrand Thirion, Olivier Grisel, Mathieu Blondel, et al. 2011.
“Scikit-Learn: Machine Learning in Python.” *Journal of Machine Learning
Research* 12 (Oct): 2825–30.

</div>

<div id="ref-R" class="csl-entry">

R Core Team. 2019. *R: A Language and Environment for Statistical
Computing*. Vienna, Austria: R Foundation for Statistical Computing.
<https://www.R-project.org/>.

</div>

<div id="ref-pickle" class="csl-entry">

Van Rossum, Guido. 2020. *The Python Library Reference, Release 3.8.2*.
Python Software Foundation.

</div>

<div id="ref-Python" class="csl-entry">

Van Rossum, Guido, and Fred L. Drake. 2009. *Python 3 Reference Manual*.
Scotts Valley, CA: CreateSpace.

</div>

<div id="ref-seaborn" class="csl-entry">

Waskom, Michael, Olga Botvinnik, Drew O’Kane, Paul Hobson, Saulius
Lukauskas, David C Gemperline, Tom Augspurger, et al. 2017.
*Mwaskom/Seaborn: V0.8.1 (september 2017)* (version v0.8.1). Zenodo.
<https://doi.org/10.5281/zenodo.883859>.

</div>

<div id="ref-knitr" class="csl-entry">

Xie, Yihui. 2014. “Knitr: A Comprehensive Tool for Reproducible Research
in R.” In *Implementing Reproducible Computational Research*, edited by
Victoria Stodden, Friedrich Leisch, and Roger D. Peng. Chapman;
Hall/CRC. <http://www.crcpress.com/product/isbn/9781466561595>.

</div>

</div>
