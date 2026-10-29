# ---------- Import libraries ----------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ---------- Load data ----------
df = pd.read_csv("Zomato data .csv")
print(df.head())

# ---------- Clean the rate column ----------
def rate(value):
    value = str(value).split("/")
    value = value[0]
    return float(value)

df["rate"] = df["rate"].apply(rate)
print(df)

# ---------- Data understanding ----------
print(df.info())
print(df.isnull().sum())
print("Total null values:", df.isnull().sum().sum())
print("Total duplicate values:", df.duplicated().sum())

# ---------- Change datatype of rate ----------
df["rate"] = df["rate"].astype(float)
print(df.info())

# ---------- Q1: Restaurant type with most orders ----------
sns.countplot(x=df["listed_in(type)"])
plt.xlabel("types of restaurant")
plt.ylabel("Count of Orders")
plt.show()

# ---------- Q2: Votes per restaurant type ----------
every_restaurant_vote = df.groupby("listed_in(type)")["votes"].sum()
print(every_restaurant_vote)
plt.plot(every_restaurant_vote, c="Red", marker="o")
plt.xlabel("Types Of Restaurants")
plt.ylabel("Votes")
plt.show()

# ---------- Q3: Majority rating ----------
Majority_rating = df["rate"].value_counts(bins=5)
print("Majority Rating Range:", Majority_rating)

plt.hist(df["rate"], bins=5)
plt.title("Rating distribution")
plt.show()

# ---------- Q4: Average couple spending ----------
average_couple_spending = df["approx_cost(for two people)"].mean()
print("Average Couple Spending:", average_couple_spending)

sns.histplot(df["approx_cost(for two people)"], bins=20)
plt.show()

# ---------- Q5: Online vs offline rating ----------
rating_comparison = df.groupby("online_order")["rate"].mean()
print(rating_comparison)
print("No means: Offline orders, Yes means: Online orders")

sns.boxplot(x=df["online_order"], y=df["rate"], data=df)
plt.show()

# ---------- Q6: Offline orders by restaurant type ----------
pivot_table = df.pivot_table(index="listed_in(type)", columns="online_order", aggfunc="size")
print(pivot_table)

sns.heatmap(pivot_table)
plt.title("customer behaviour")
plt.show()
