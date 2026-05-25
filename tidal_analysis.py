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
import glob


def read_tidal_data (filename):
    file_list= glob.glob(f"{filename}/*")
    all_chunks=[]
    for filename in file_list:
        tide_Data['Date'] = pd.to_datetime(dict(year=tide_Data[0], month=tide_Data[1], day=tide_Data[2], hour=tide_Data[3], minute=tide_Data[4], seconds= tide_Data[5]))
        # col0 is year, col 1 is month, col 2 is day col 3 is hour col 4 is minute, col 5 is seconds 
        tide_Data= tide_Data.drop([0,1,2,3,4,5], axis=1)
        all_chunks.append(tide_Data)
        combined_data= pd,concat(all_chunks, ignore_index=True)
        return combined_data

def extract_single_year_remove_mean(year, data):
    year_string_start= str(year)+"0101"
    year_string_end= str(year)+"1231"
    year_data= data.loc[year_string_start: year_string_end["tide"]]
    # remove mean to osillate around 0
    mmm= np.mean(year_data['tide'])
    year_data['tide']-= mmm
    return year_data

def extract_section_remove_mean(start, end, data):
    #start and end times
    year_data= data.loc[start:end].copy()
    #subtracting the mean
    year_mean= year_data['tide'].mean()
    year_data['tide']-= year_mean
    return year_data

def join_data(data1, data2):
    #makes for easy comparison between sites and can skip blank times
    joined= pd.merge(data1,data2,left_index= True, right_index= True, suffixes= ('_site1','_site2'))
    return joined

def sea_level_rise(data):
    df= pd.read_csv("data")
    result=sea_level_rise(df)
    print(result)
    return

def tidal_analysis(data, constituents, start_datetime):
    #water level figures
    my_data= ["data"]
    #tidal components
    my_constituents= ["M2", "S2"]
    #starting time of data 
    my_start_time=datetime.datetime(2000,1,1,0,0)
    return

def get_longest_contiguous_data(data):
    is_valid=data['tide'].notna()
    group_ids= (~is_valid).cumsum()
    longest_block_index=is_valid[is_valid].groupby(group_ids)
    blocks=is_valid.groupby(group_ids)
    best_block_id= max(blocks, key=lambda x: x[1].sum())[0]
    longest_zone= data[group_ids==best_block_id].dropna()
    return longest_zone

    def main(args_list=None):
        parser = argparse.ArgumentParser(
                     prog="UK Tidal analysis",
                     description="Calculate tidal constiuents and RSL from tide gauge data",
                     )

    parser.add_argument("directory",
                    help="the directory containing txt files with data")
    parser.add_argument('-v', '--verbose',
                    action='store_true',
                    default=False,
                    help="Print progress")

    args = parser.parse_args(args_list)
    dirname = args.directory
    verbose = args.verbose

    print("Add your code here to do things!")
    
if verbose:
    print(f"---starting tidal analysis")
    print(f"loading raw data folders from the directory")
    import os
    aberdeen_path= os,path.join(dirname, "aberdeen")
    dover_path= os.path.join(dirname,"dover")
    whitby_path= os.path.join(dirname,"whitby") 
    if verbose: print("filtering data gaps" )
    aberdeen = get_longest_contiguous_data(aberdeen_raw)
    dover    = get_longest_contiguous_data(dover_raw)
    whitby   = get_longest_contiguous_data(whitby_raw)
    return aberdeen,dover,whitby

if __name__ == '__main__':
    main()
    