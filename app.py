import pandas as pd
from pandas import DataFrame
from tableone import TableOne, load_dataset
import matplotlib.pyplot as plt

#file was too big to upload, used API to load in data instead 
data = pd.read_csv('https://health.data.ny.gov/resource/gnzp-ekau.csv')
data