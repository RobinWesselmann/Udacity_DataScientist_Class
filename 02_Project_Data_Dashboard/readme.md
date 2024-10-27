<img src="../data/img/e-auto-ladestation-101.jpg" style="width:50%;height=50%"/>
<hr>

# Setup a webapp with Flask for a Data Dashboard
This project is part of the Data Scientist Nanodegree Program.

### Table of Contents
1. [Project Motivation](#motivation)
2. [File Description](#files)
3. [Results](#results)
4. [Licensing, Authors](#licensing)

## Project Motivation <a name="motivation"></a>

The present project is a part of the Nano-degree program of Udacity. The task is to setup a data dashboard via Flask and present the results of a chosen data analysis to the user.
The focus is though on the implementation with flask / bootstrap. 
Concerning the data analysis, I chose a dataset of the german government to get insights from the current situation of the setup of charging points for electric vehicles. I wanted to adress the following (simple) questions:
1) in which "Bundesland" (regional department) are provided how many charging stations?
2) Which city is the most advanced one concerning charging stations?
3) Which "Betreiber" (responsible company) are the top 5 provider?

## File Description <a name="files"></a>
**notebooks/EDA.ipynb**: Notebook with the project's data analysis </br>
**data/Gebietsfläche.csv**: Surface of the different regional departments in Germany in km². </br>
**data/Ladesaeulenregister.csv**: Dataset from the Bundesnetzagentur (German Government institution) concerning charging points with multiple informations. Each records represents a charging point. </br>
**data/img/**: Image data present in the notebook / readme. </br>

## Results <a name="results"></a>
The findings can be found in the notebook

## Licensing, Authors <a name="licensing"></a>
The credit of the data must be given to the German Government. The data is available [here](https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/E-Mobilitaet/Ladesaeulenkarte/start.html) 