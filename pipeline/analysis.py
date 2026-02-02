import pandas as pd # type: ignore

#Load the CSV file into a DataFrame
df=pd.read_csv("api_data_aadhar_demographic_1000000_1500000.csv")  

#Display the first few records and unique states
print(df.head())
print(df["state"].unique())
