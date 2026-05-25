# import the modules we need
import pandas as pd
import datetime
import os
import numpy as np
import uptide
import pytz
import math
from scipy import stats
import matplotlib.dates as mdates
import argparse


def read_tidal_data(filename):
    tide_Data = pd.read_csv("C:Onedrive/Documents/Code/data", header= None)
    tide_Data['Date'] = pd.to_datetime(dict(year=tide_Data[0], month=tide_Data[1], day=tide_Data[2], hour=tide_Data[3], minute=tide_Data[4], seconds= tide_Data[5]))
    # col0 is year, col 1 is month, col 2 is day col 3 is hour col 4 is minute, col 5 is seconds 
    tide_Data= tide_Data.drop([0,1,2,3,4,5], axis=1)
    tide_Data= tide_Data.rename(columns={6: "tide"})
    tide_Data= tide_Data.set_index('Date')
    tide_Data= tide_Data.mask(tide_Data['Tide']< -300)
    return tide_Data
     
