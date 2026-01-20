import pandas as pd # type: ignore


#Load cleaned & merged file
df = pd.read_csv("demographic_merged_clean.csv")

print(df.columns)

#Create Total Population Column (Demographic Schema)
df["total_population"] = (
    df["demo_age_5_17"] +
    df["demo_age_17_"]
)

#State-wise Demographic Aggregation
state_demo = (
    df.groupby("state_")[["total_population", "demo_age_5_17", "demo_age_17_"]]
      .sum()
      .reset_index()
)

print(state_demo)

state_demo["child_population"] = state_demo["demo_age_5_17"]
state_demo["adult_population"] = state_demo["demo_age_17_"]

state_demo["total_population"] = (
    state_demo["child_population"] + state_demo["adult_population"]
)

#Ratios
state_demo["child_ratio_%"] = (
    state_demo["child_population"] / state_demo["total_population"]
) * 100

state_demo["adult_ratio_%"] = (
    state_demo["adult_population"] / state_demo["total_population"]
) * 100

#Child-Dominant Ranking
child_rank = state_demo.sort_values(
    by="child_ratio_%",
    ascending=False
).reset_index(drop=True)

child_rank["Child_Rank"] = range(1, len(child_rank) + 1)

print("\n Top 10 Child-Dominant States:")
print(
    child_rank[["Child_Rank", "state_", "child_ratio_%"]]
    .head(10)
    .to_string(index=False)
)

#Adult-Dominant Ranking
adult_rank = state_demo.sort_values(
    by="adult_ratio_%",
    ascending=False
).reset_index(drop=True)

adult_rank["Adult_Rank"] = range(1, len(adult_rank) + 1)

print("\n Top 10 Adult-Dominant States:")
print(
    adult_rank[["Adult_Rank", "state_", "adult_ratio_%"]]
    .head(10)
    .to_string(index=False)
)

#Save Outputs
state_demo.to_csv("state_demographic_summary.csv", index=False)

child_rank.to_csv("state_child_top10.csv", index=False)
adult_rank.to_csv("state_adult_top10.csv", index=False)
