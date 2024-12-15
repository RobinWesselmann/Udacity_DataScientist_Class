<img src="../data/img/starbucks_logo.png">
<hr>

# Project A/B Testing at Starbucks
This Project is part of the Data Scientist Nanodegree Program.

### Table of Contents
1. [Project Motivation](#motivation)
2. [File Description](#files)
3. [Licensing, Authors](#licensing)

## Project Motivation <a name="motivation"></a>

The project takes up a take-home assignment provided by Starbucks for their job candidates. 
The data for this exercise consists of about 120,000 data points split in a 2:1 ratio among training and test files. In the experiment simulated by the data, an advertising promotion was tested to see if it would bring more customers to purchase a specific product priced at $10. Since it costs the company 0.15 to send out each promotion, it would be best to limit that promotion only to those that are most receptive to the promotion. Each data point includes one column indicating whether or not an individual was sent a promotion for the product, and one column indicating whether or not that individual eventually purchased that product. Each individual also has seven additional features associated with them, which are provided abstractly as V1-V7.

The goal of this challenge is to use the training data to understand what patterns in V1-V7 to indicate that a promotion should be provided to a user. In essence, we want to come up with an robust optimization strategy to maximize the Incremental Response Rate (IRR) and the Net Incremental Revenue (NIR).

The leading research questions for this project are: 
1) Do promotion offers increase revenue increment (IRR) significantly?
2) How is it possible to maximize the Incremental Response Rate (IRR) and the Net Incremental Revenue (NIR)?

Hence, we want in the first place know if there's really a significant impact of promotions on the IRR and in a second step build a model which predicts if a customer purchases the product dependant on the features `v1 to v7`. We'll choose the model with the best score in terms of IRR & NIR which can be used by Starbucks to optimize their promotion sent outs.

## File Description <a name="files"></a>
**data/img**: images for the readme & Notebook</br>
**data/-**: train data and test data</br>
**/src/Starbucks.ipynb**: working file to adress the leading research question of the project</br>
**/src/test_result.py**: file of Udacity to test some questions of the Starbucks.ipynb file</br>

## Licensing, Authors <a name="licensing"></a>
The credit for the data goes to Udacity & Starbucks.