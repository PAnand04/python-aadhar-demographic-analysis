import pandas as pd # type: ignore
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

df = pd.read_csv("demographic_merged_clean.csv")

#Load outputs
state_demo = pd.read_csv("state_demographic_summary.csv")
child_top = pd.read_csv("state_child_top10.csv")
adult_top = pd.read_csv("state_adult_top10.csv")
child_bottom = pd.read_csv("state_child_bottom10.csv")
adult_bottom = pd.read_csv("state_adult_bottom10.csv")

colors = ["#d315a3", "#5D97CE", "#72df86"]

#1.Top-10 Child-Heavy States
plt.figure(figsize=(10,5))
bars = plt.bar(
    child_top["state_"].iloc[:10],
    child_top["child_ratio_%"].iloc[:10],
    color=colors * 4
)

plt.xticks(rotation=45, ha="right")
plt.title("Top 10 Child-Dominant States")
plt.xlabel("State")
plt.ylabel("Child Population (%)")

for bar in bars:
    h = bar.get_height()
    plt.text(bar.get_x()+bar.get_width()/2, h, f"{h:.1f}%",
             ha="center", va="bottom", fontsize=9)

plt.tight_layout()
plt.show()

#2.Top-10 Adult-Heavy States
plt.figure(figsize=(10,5))
bars = plt.bar(
    adult_top["state_"].iloc[:10],
    adult_top["adult_ratio_%"].iloc[:10],
    color=colors * 4
)

plt.xticks(rotation=45, ha="right")
plt.title("Top 10 Adult-Dominant States")
plt.xlabel("State")
plt.ylabel("Adult Population (%)")

for bar in bars:
    h = bar.get_height()
    plt.text(bar.get_x()+bar.get_width()/2, h, f"{h:.1f}%",
             ha="center", va="bottom", fontsize=9)

plt.tight_layout()
plt.show()


#3.National Demographic Composition
total_children = state_demo["child_population"].sum()
total_adults = state_demo["adult_population"].sum()

labels = ["Children (5–17)", "Adults (17+)"]
sizes = [total_children, total_adults]
colors = ["#d315a3", "#5D97CE"]

plt.figure(figsize=(6,6))
plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct="%1.1f%%",
    startangle=90
)


plt.title("National Demographic Composition (Aadhaar)")
plt.tight_layout()
plt.show()

#4.Overall State Demographic Structure
state_demo = state_demo.sort_values(by="child_ratio_%", ascending=False)

x = np.arange(len(state_demo))
width = 0.4

plt.figure(figsize=(14,6))

plt.bar(
    x - width/2,
    state_demo["child_ratio_%"],
    width,
    label="Children (5–17)",
    color="#72df86"
)

plt.bar(
    x + width/2,
    state_demo["adult_ratio_%"],
    width,
    label="Adults (17+)",
    color="#d315a3"
)

plt.xticks(x, state_demo["state_"], rotation=45, ha="right")
plt.title("Overall State Demographic Structure: Child vs Adult Ratio")
plt.xlabel("State")
plt.ylabel("Population Share (%)")
plt.legend()
plt.tight_layout()
plt.show()

#5.National Child Population Share Over Time
df["date"] = pd.to_datetime(
    df["date"],
    format="mixed",
    dayfirst=True,
    errors="coerce"
)

df = df[df["date"].notna()]

daily_demo = (
    df.groupby("date")[["demo_age_5_17", "demo_age_17_"]]
      .sum()
      .reset_index()
)

daily_demo["total_population"] = (
    daily_demo["demo_age_5_17"] + daily_demo["demo_age_17_"]
)

daily_demo["child_ratio_%"] = (
    daily_demo["demo_age_5_17"] / daily_demo["total_population"]
) * 100

plt.figure(figsize=(12,5))
plt.plot(
    daily_demo["date"],
    daily_demo["child_ratio_%"],
    marker="o",
    linewidth=2
)

plt.title("National Child Population Share Over Time")
plt.xlabel("Date")
plt.ylabel("Child Population (%)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
