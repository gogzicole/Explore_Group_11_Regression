import pandas_profiling 
import numpy as np
import pandas as pd
import random
needed_columns = ["time","Seville_wind_speed","Seville_rain_1h","Seville_rain_3h","Seville_humidity","Seville_clouds_all","Seville_pressure","Seville_weather_id","Seville_temp_max","Seville_temp_min","Seville_temp"]
accDf=pd.read_csv("df_train.csv",usecols=needed_columns)
accDf2=pd.read_csv("df_test.csv",usecols=needed_columns)

profile = accDf.profile_report(title="Seville Train Profile")
profile.to_file(output_file="seville_train_profile.html")
accDf=pd.read_csv("df_train.csv")

profile = accDf2.profile_report(title="Seville Text Profile")
profile.to_file(output_file="seville_test_profile.html")