import pandas as pd # type: ignore

files=["api_data_aadhar_demographic_0_500000.csv",
       "api_data_aadhar_demographic_500000_1000000.csv",
       "api_data_aadhar_demographic_1000000_1500000.csv",
       "api_data_aadhar_demographic_1500000_2000000.csv",
       "api_data_aadhar_demographic_2000000_2071700.csv"]

df =pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

#Create a cleaned version of the 'state' column lowered and stripped of whitespace
df["state_"] = df["state"].str.lower().str.strip()
#print(sorted(df["state_"].unique()))  #Print the sorted list of unique cleaned state names

#Dictionary mapping incorrect state names to correct ones or None for invalid entries
fix_map = {
    "orissa": "odisha",
    "pondicherry": "puducherry",
    "chhatisgarh": "chhattisgarh",

    "west bangal": "west bengal",
    "westbengal": "west bengal",
    "west  bengal": "west bengal",
    "west bengli": "west bengal",

    "jammu & kashmir": "jammu and kashmir",

    "andaman & nicobar islands": "andaman and nicobar islands",

    "dadra & nagar haveli": "dadra and nagar haveli and daman and diu",
    "daman and diu": "dadra and nagar haveli and daman and diu",
    "daman & diu": "dadra and nagar haveli and daman and diu",
    "dadra and nagar haveli": "dadra and nagar haveli and daman and diu",

    "100000": None  #means invalid entry
}

#Apply the corrections to the cleaned state names
df["state_"] = df["state_"].replace(fix_map)

#Authoritative whitelist (28 States + 8 UTs = 36)
valid_states_uts = {
    "andaman and nicobar islands",
    "andhra pradesh",
    "arunachal pradesh",
    "assam",
    "bihar",
    "chandigarh",
    "chhattisgarh",
    "dadra and nagar haveli and daman and diu",
    "delhi",
    "goa",
    "gujarat",
    "haryana",
    "himachal pradesh",
    "jharkhand",
    "karnataka",
    "kerala",
    "ladakh",
    "lakshadweep",
    "madhya pradesh",
    "maharashtra",
    "manipur",
    "meghalaya",
    "mizoram",
    "nagaland",
    "odisha",
    "puducherry",
    "punjab",
    "rajasthan",
    "sikkim",
    "tamil nadu",
    "telangana",
    "tripura",
    "uttar pradesh",
    "uttarakhand",
    "west bengal",
    "jammu and kashmir",
}

#Enforce validity by keeping only valid state names
df["state_"] = df["state_"].where(
    df["state_"].isin(valid_states_uts)
)

#Drop invalid rows (cities, regions, garbage values)
df = df.dropna(subset=["state_"])

#Final verification
print("Final States & UTs:", df["state_"].nunique())
print(sorted(df["state_"].unique()))

df.to_csv("demographic_merged_clean.csv", index=False)
print("Saved demographic_merged_clean.csv")