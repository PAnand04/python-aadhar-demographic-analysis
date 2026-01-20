import pandas as pd # type: ignore

files=["api_data_aadhar_demographic_0_500000.csv",
       "api_data_aadhar_demographic_500000_1000000.csv",
       "api_data_aadhar_demographic_1000000_1500000.csv",
       "api_data_aadhar_demographic_1500000_2000000.csv",
       "api_data_aadhar_demographic_2000000_2071700.csv"]

#Concatenate/link all CSV files into a single DataFrame
df =pd.concat([pd.read_csv(f) for f in files], ignore_index=True)  
#Print the total number of records
print("Total Records:", len(df))  
#Print the number of unique states
print("Unique States:", df["state"].nunique())  
#Print the list of unique states
print(df["state"].unique())  
