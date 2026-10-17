import pandas as pd
import numpy as np
import datetime as dt

def load_data():  
  cu=pd.read_csv(r'Data\customers.csv')
  order=pd.read_csv(r'Data\orders.csv')
  product=pd.read_csv(r'Data\products.csv')
  return cu,order,product


def cleaning(cu,order,product):
    order=order.fillna(0)
    order=order.fillna(0)
    return cu,order,product


