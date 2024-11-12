import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# Read the Csv file and then drop the columns given in the question 
df1 = pd.read_csv('power-laws-forecasting-energy-consumption-holidays.csv', delimiter=';')
df2 = pd.read_csv('power-laws-forecasting-energy-consumption-metadata.csv', delimiter=';')
df3 = pd.read_csv('power-laws-forecasting-energy-consumption-submission-forecast-period.csv', delimiter=';')

