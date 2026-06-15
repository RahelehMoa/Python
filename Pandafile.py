#/////////////////////////Create Data Fram in Panda/////////////////////////
import pandas as pd

#df = {'Name': ['luca', 'Emma', 'Gianula','Sara'],
   # 'Age':[35,30,28,34],  
    #  'Gender':['Male','Famale','Male','Famale']}

#print(df)

#data_f = pd.DataFrame(df)
##print(data_f)

#/////////////////////////////Read Excel File////////////////////////////////

df_csv = pd.read_csv("L1_Energy_V1.0.0.csv")
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

df_csv_copy = df_csv.copy()
df_csv_copy.columns = ["Region","Point","Place","ID","Item","TimeItems","ValueItem","DayItem"]
print(df_csv_copy)

#print = (df_csv_copy.info())

#WAY 1
#df_write = df_csv_copy.to_csv(r"C:\Users\User1\Desktop\pythonNew\newfile.csv")
#print(df_write)
#WAY 2
#df_csv_copy.to_csv(r"C:\Users\User1\Desktop\pythonNew\newfile2.csv")
#WAY 3
#df_csv_copy.to_csv(r"newfile3.csv")