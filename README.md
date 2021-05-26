# Sentiment Analysis on Swiss Newspapers
## Bachelor thesis 

* Degree course: **BSC Computer Science**
* Author:  **Giorgio Bakhiet Derias** 
* Tutor: **Prof. Dr. Mascha Kurpicz-Briki**
* Expert: **Andreas Dürsteler**
* Date: **Juni 18, 202**


## Abstract

Today’s newspapers have the power to shape one’s entire perspective on the world.  For that reason, itis very important to be able to differentiate between newspapers that keep one in a rather pessimisticstate of being, or newspapers that offer a more optimistic outlook on the world.  The idea is to create,train, adjust and improve a model so that it is fit to analyze various Swiss newspapers and todetermine which papers are written with the most negative and positive attitude.

## Getting Started
Jupyter notebooks are to be opened in this order:
- Model.ipynb
- SentimentAnalysisNewspaper.ipynb
- Dashboard.ipynb

Each jupyter notebook has its own **requirements** file:
- requirementsModel.txt
- requirementsNewspaper.txt
- requirementsDashboard.txt

### Prerequisites
Change the file destinations in Jupyter files to suit your system.

## Model Notebook
This notebook is for creating a model for the German language.
For this notebook, the datasets to be used is:
```
filmstarts.tsv
```
The model will be saved in the folder:
```
modelsave
```
## SentimentAnalysisNewspaper Notebook
This notebook uses the previously trained model for the purpose of making predictions on the newspaper dataset.
With this notebook it is also possible to do data analysis thanks to the plot functions.
For this notebook, the datasets to be used is in folder:
```
./database_newspaper/total/
```
This notebook will export a cleaned and predicted csv file in the main folder:
```
news_concat.csv
```
## Dashboard Notebook
This notebook does not import the model, but only to create the plots. The usefulness of this notebook is in the lightness, in fact without having to load the model and make the forecasts will be faster and you can view the dashboard thanks to the voila library.
For this notebook you will need to import the file with the forecasts, which will be located in the main folder:
```
news_concat.csv
```

