<img src="./data/img/arvato.png">
<hr>

# Capstone Project Arvato-Bertelsmann Customer Segmentation
This Project is part of the Data Scientist Nanodegree Program.

### Table of Contents
1. [Project Motivation](#motivation)
2. [File Description](#files)
3. [Libraries used](#Libraries_used)
3. [Project Summary](#project_summary)
5. [Licensing, Authors](#licensing)

## Project Motivation <a name="motivation"></a>

The Arvato-Group is one of total 8 business units in the Bertelsmann Group which is a worldwide operating service company head-quarted in Germany.<br>
The main operating field of Avarto are logistics- and supply chain services and solutions, financial services as well as the operation of IT Systems. Concerning the general figures to get a grasp of the company, the company employs a staff around 77.342 persons (2020) and generates a sales volume of 5.56 Mrd. EUR per a (2024).

The present project can be localized in the financial services branch of Arvato (Arvato Financial Solutions) and is part of the Udacity Data Scientist Nanodegree Program.<br><br>
<span style="color: green;">**One client of Arvato Financial Solutions, a Mail-Order Company selling organic products, wants to be advised concerning a more efficient way to acquire new clients.<br>
In essence, the company wants their acquisition marketing campaings instead of reaching out to everyone (costly), target more precisely those persons which show the highest probability to turn into new customers.**</span>
<br><br>
<span style="text-decoration: underline;">The project spans two main tasks:</span>
1) Customer Segmentation: An Analysis of the existing customer database dataset is carried out and on this basis a general recommandation of which people in Germany are most likely to be new customers of the company is generated. <br><br>
2) Modelling Campaign-Responses: Using the results of 1) to build a machine learning model that predicts whether or not an individual will respond to the respective campaign.

## File Description <a name="files"></a>
**data/img**: images for the readme & Notebooks</br>
**data/customer_segmentation/Udacity_AZDIAS_052018.csv**: Demographic dataset of Germany provided for the customer segmentation task</br>
**data/customer_segmentation/Udacity_CUSTOMERS_052018.csv**: Dataset (nearly the same structure as Azdias dataset) containing customer data of the client provided for the customer segmentation task</br>
**data/description/DIAS Attributes - Values 2017.xlsx**: Descriptive dataset provided for the customer segmentation task</br>
**data/description/DIAS Information Levels - Attributes 2017.xlsx**: Descriptive dataset provided for the customer segmentation task</br>
**data/modeling/Udacity_MAILOUT_052018_TEST.csv**: Test dataset provided for the supervised learning task</br>
**data/modeling/Udacity_MAILOUT_052018_TRAIN.csv**: Train dataset provided for the supervised learning task</br>
**data/concept.xlsx**: Excel notes for general concept to showcase the solution path for the tasks</br>

## Libraries used <a name="Libraries_used"></a>
The following libraries were used:
* numpy
* pandas 
* os
* re
* matplotlib
* seaborn
* scipy
* sklearn
* xgboost
* imblearn
* warnings

## Project Summary<a name="project_summary"></a>
The project was made up of two parts:

**Unsupervised Learning:**

The general goal of this section is to find relevant customer cluster for the client, a mail-order company. </br>
The chosen instrument to achieve this clustering is the K-Means Clustering algorithm. In order to avoid the curse of dimensionality a PCA is performed before the clustering step to reduce the number of features (around 350). The goal was to keep 80% of the information and the number of features could be reduced from 350 to 151 features. 
The K-Means algorithm has been performed on this reduced dataset in a range from k=3 to k=29 cluster-centroids and the optimal "k" has been chosen by using the elbow-method. 
The steps have been documented and the relevant topics explained along the analysis.

**Supervised Learning:**

In the supervised learning part a standardized preprocessing pipeline has been established and four different models (logistic regression, RandomForest, Adaboost, XGBoost) as well as a naive classifier have been tested for the experimentation. </br>
Due to the fact that the dataset shows a quite strong imbalance concerning the target variable, the "ROC_AUC" metric has been chosen. 
In a first step all 4 (or 5) models have been trained within the pipeline and the XGBoost performed best (0.73). 
Hence the XGBoost model as best performing model has been refined in a hyperparameter tuning phase to improve the performance of the model even further. For this task, GridSearchCV was used to find the best hyperparameter combination and it was possible to improve the performance to a ROC_AUC of 0.76.

As the test set is provided without any correct y values and the kaggle competition doesn't allow anymore for any submission the model tuning / testing has been performed via Crossvalidation on the train set.

**Metrics** 

For the unsupervised part of the project, an optimal "k" for the K-Means clustering model had to be found. The elbow method was used to determine this optimal k.</br>
For the supervised part of the project, the performance of the respective models had to be evaluated / compared. Due to the fact that the dataset shows a severe target class imbalance, some metrics such as accuracy would have been an adequate metric for performance evaluation. The ROC_AUC Score takes Recall and the False Positive Rate over several thresholds into account and is therefore a good metric to evaluate a model's ability to distinguish between classes. In addition to that, precision was another metric which has been discussed due to its ability to evaluate the model's performance from another angle.

**Results**

**Unsupervised Learning**
The unsupervised learning part aimed to identify valuable cluster of individuals for the company. 
There were two significantly overrepresented cluster: Cluster 7 and 12. 
* the cluster 7 seems to embody individuals of advanced age (~ > 70 years old), living with around 2 persons in a rural area (around 20-30 km from the next city) without children, but earning a high income focusing concerning the financial perspective to be prepared for the future. Moreover the individuals belonging to this cluster are average religious, average family persons, average cultural minded, less critical minded, average material minded and average rational minded

* the cluster 12 seems to embody individuals of mid age (~ 55), living with around 4 persons in a very rural area (around 30-50 km from the next city) without children, earning a high income focusing on owning an own house. The individuals belonging to this cluster have a low affinity to religion, a low affinity to family, an average to high affinity to critical thinking, a low affinity cultural topics, an average affinity to materialism and not really rational minded

**Supervised Learning**

In the first part of the section, the four models have been tested concerning their performance on the task at hand:

<table>
  <tr>
    <th>Model</th>
    <th>CV Mean Roc-Auc</th>
  </tr>
  <tr>
    <td>Naive Classifier</td>
    <td>0.49</td>
  </tr>
  <tr>
    <td>RandomForest Classifier</td>
    <td>0.71</td>
  </tr>
  <tr>
    <td>Logistic Regression</td>
    <td>0.59</td>
  </tr>
  <tr>
    <td>AdaBoostClassifier</td>
    <td>0.68</td>
  </tr>
  <tr>
    <td>XGBoostClassifier</td>
    <td>0.73</td>
  </tr>
</table>

Following these scores, XGBoostClassifier was chosen for further hyperparameter training and the optimal parameter combination resulted in:</br>

{'model__colsample_bytree': 1.0,
 'model__learning_rate': 0.01,
 'model__max_depth': 5,
 'model__n_estimators': 200,
 'model__subsample': 0.6,
 'model__tree_method': 'gpu_hist'}

The following averaged CV Scores have been reached:
<table>
  <tr>
    <th>Metric</th>
    <th>Value</th>
  </tr>
  <tr>
    <td>Precision</td>
    <td>0.52</td>
  </tr>
  <tr>
    <td>Recall</td>
    <td>0.76</td>
  </tr>
  <tr>
    <td>ROC AUC Score</td>
    <td>0.76</td>
  </tr>
</table>

## Licensing, Authors <a name="licensing"></a>
The credit for the data goes to Udacity & Arvato Financial Solutions.