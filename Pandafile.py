#/////////////////////////Create Data Fram in Panda/////////////////////////
#import pandas as pd

#df = {'Name': ['luca', 'Emma', 'Gianula','Sara'],
   # 'Age':[35,30,28,34],  
    #  'Gender':['Male','Famale','Male','Famale']}

#print(df)

#data_f = pd.DataFrame(df)
##print(data_f)

#/////////////////////////////Read Excel File////////////////////////////////

#df_csv = pd.read_csv("L1_Energy_V1.0.0.csv")
#print(df_csv.tail(10))

#print(df_csv.dtypes)

#print = (df_csv.info())

#dfC = df_csv[["parameter","Daily"]]
#print(dfC.tail(20))

#dfC2 = df_csv["area"]
#print(dfC2.tail(5))

#df_drop = df_csv.drop(columns=["time"])
#print(df_drop)

#df_drop2 = df_csv.drop(columns=["time","value"])
#print(df_drop2)

#df_rename = df_csv.rename(columns={"partition":"place", "installation":"ID"})
#print(df_rename)

#print = (df_rename.info())

#df_csv_copy = df_csv.copy()
#df_csv_copy.columns = ["Region","Point","Place","ID","Item","TimeItems","ValueItem","DayItem"]
#print(df_csv_copy)

#print = (df_csv_copy.info())

#WAY 1
#df_write = df_csv_copy.to_csv(r"C:\Users\User1\Desktop\pythonNew\newfile.csv")
#print(df_write)
#WAY 2
#df_csv_copy.to_csv(r"C:\Users\User1\Desktop\pythonNew\newfile2.csv")
#WAY 3
#df_csv_copy.to_csv(r"newfile3.csv")

#///////////////////////////////////////////////////////////////////////////////
#/////////////////////////////LOC/ILOC/////////////////////////////////////////
# Filter where in SQL = loc and iloc in python
# in Loc we define int and string but in iloc we define int.

#df_filter = df_csv.loc[1970,"value"]
#print(df_filter)     # Answer = 37.545

#df_filter2 = df_csv.iloc[1975 , 6]
#print(df_filter2)      # Answer = 0

#df_filter_indx = df_csv.set_index("installation")
#df_filter_indx1 = df_filter_indx.loc["db_20200723080331_5739058599","partition"]
#print(df_filter_indx1) 

#df_filter_indx = df_csv.set_index("installation")
#df_filter_indx3 = df_filter_indx.iloc[10,3]
#print(df_filter_indx3) 

#df_filter_r = df_csv.loc[5]
#print(df_filter_r)

#df_filter_row = df_csv.iloc[5]
#print(df_filter_row)   #the same result with above, df_filter_r

#df_filter4 = df_csv.loc[0:4, ["area","parameter"]]
#print(df_filter4)

# Result is until index 4 , 0:5 ;and columns is 0 , 1 before2,  0:2
#df_filter5 = df_csv.iloc[0:5, 0:2]
#print(df_filter5)

#df_filter6 = df_csv["area"].loc[1960:1965]
#print(df_filter6)

#df_filter7 = df_csv["area"].iloc[1960:1967]  #Result is one before 1967
#print(df_filter7)

#/////////////////////////////Create Columns/////////////////////////////////////////
#ALTER and Update or Replace values in SQL 

#df_columns = df_csv.copy()
#df_columns["Test"] = "New Value"
#print(df_columns)

#df_columns["Test"] = "New Update"  #Above Column is Updated.
#print(df_columns)

#df_columns["Numeric"] = [X for X in range(len(df_columns))]
#print(df_columns)

#create New Column and Replace Values
#df_csv.loc[df_csv["value"] == 0 ,"Value2"] = "100"
#print(df_csv)
#df_csv.loc[df_csv["value"] > 1 ,"Value2"] = "200"
#print(df_csv)

#Sum two columns are int:
#df_total = df_csv.copy()
#df_total["totalvalue"] = df_total["value"] + df_total ["Value2"]
#print(df_total)

#Write Sentences with values or concatenate and sum several columns:
#df_total2 = df_csv.copy()
#df_total2["value"] = df_total2["value"].astype("str")
#df_total2["NewColumn"] = df_total2["value"] + "|" + df_total2 ["endpoint"] + ": Result"
#print(df_total2)

#Replace Values. becerful that "int" change "string" with replace automaticlly
#df_rep = df_csv.copy()
#df_rep = df_rep.replace("C","B")
#print(df_rep)
#df_rep ["endpoint"] = df_rep["endpoint"].replace("C-EM" , "B-EM")
#df_rep ["value"] = df_rep["value"].replace(0 , "New Value is enter")
#print(df_rep)

#Sort or Orderby in SQL:
#df_sort= df_csv.sort_values("area")     #sort by Allefbatically
#print(df_sort)

#df_sort2= df_csv.sort_values("area" , ascending=False)   #defult is True.
#print(df_sort2)       #false is reverse.

#df_sort3= df_csv.sort_values(["area" , "value" , "time" ], ascending= [False,True,True])
#print(df_sort3)

#//////////////////////////////INDEX//////////////////////////////
#df_inx = df_csv["area"].loc[1940]
#print(df_inx)

#df_inx2 = df_csv["time"].loc[1940]
#print(df_inx2)

#when you sort the columns so index is changed for reset index from 0 there is :
#df_dr = df_csv.reset_index(drop="index")
#print(df_dr)

#/////////////////////////////Date Time/////////////////////////////////

import datetime as dt
import pandas as pd

df_csv_time =pd.read_csv("L1_Humidity_V1.0.0.csv")
print(df_csv_time.tail(10))

df_csv_time2 = df_csv_time[["area" , "Daily" , "time"]]
#print(df_csv_time2)

df_types = df_csv_time2.dtypes   #show Data Types 
#print (df_types)

#////////////////////////Convert Str to Datetime////////////////////////////////////////
df_csv_time2["Daily"] = pd.to_datetime(df_csv_time2["Daily"], errors='coerce', dayfirst=True)
#print(df_csv_time2)

df_csv_time2["time"] = pd.to_datetime(df_csv_time2["time"])
#print(df_csv_time2)

#///////////////////////////Seperate Day | Month | year in Datetime////////////////////////
df_csv_time2["TotalDaies"] = df_csv_time2["time"].dt.day
df_csv_time2["month"] = df_csv_time2["time"].dt.month
df_csv_time2["year"] = df_csv_time2["time"].dt.year
#print(df_csv_time2)

#////////////////////////Manipulation in Datatime//////////////////////////

df_csv_time2 ["DataShift"] = df_csv_time2["Daily"] + dt.timedelta (days= 25)
#print(df_csv_time2)

df_csv_time2 ["DateOffset"] = df_csv_time2["Daily"] + pd.DateOffset(months= 1)
#print(df_csv_time2)

del df_csv_time2["TotalDaies"];  #whole delete Column 
#print(df_csv_time2)


del df_csv_time2["month"];
#print(df_csv_time2)

df_csv_time_dif = df_csv_time2.loc[(df_csv_time2["Daily"] >= " 2021-01-15") & 
                                   (df_csv_time2["Daily"] < "2021-02-10")]
#print(df_csv_time_dif)


#///////////////////////////Generic Functions///////////////////////////////////
#one column
#df_fun = df_csv_time["ValueHumi"].min()
#df_fun = df_csv_time["ValueHumi"].max()
#df_fun = df_csv_time["ValueHumi"].mean()
#df_fun = df_csv_time["ValueHumi"].sum()
#print(df_fun)

#two columns and more
#df_fun = df_csv_time[["ValueHumi","installation"]].max()
#print(df_fun)

#all columns
#df_fun = df_csv_time.max()
#print(df_fun)

#df_fun = df_csv_time["ValueHumi"].value_counts()
#print(df_fun)

#df_fun = df_csv_time["ValueHumi"].value_counts(normalize=True)
#print(df_fun)

#df_fun = df_csv_time["ValueHumi"].value_counts(bins= 5)
#print(df_fun)

#df_fun = df_csv_time["ValueHumi"].value_counts(normalize=True , dropna=False)
#print(df_fun)

#df_des = df_csv_time.describe()
#print(df_des)

#df_des = df_csv_time.describe(percentiles= [0.10 , 0.90] , include= "all")
#print(df_des)
# Describe one column
#df_des = df_csv_time["ValueHumi"].describe()
#print(df_des)
#///////////////////////////////////Sample//////////////////////////////////////

