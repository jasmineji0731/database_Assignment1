import pandas as pd

#local filename:
filepath = "supplement_impact_data.csv"

df = pd.read_csv(filepath)

# whole dataset
# print(df)

# first 2 rows
print(df.head(2))

# first row
print(df.iloc[0])

# slice rows 10-19
print(df.iloc[10:20])

# column names
print(df.columns)

# first 10 values of one column
print(df["Supplement"].head(10))

# 3 columns (prints the first 10 rows of each column)
print(df[["Age", "Gender", "Supplement"]].head(10))


# Question 1: What are the age, gender, weeks, and weights of the first 10 people who use Creatine Monohydrate?
creatine_data = df.loc[
    df["Supplement"] == "Creatine Monohydrate",
    ["Age", "Gender", "Weeks", "Initial_WT", "Final_WT"]
]
print(creatine_data.head(10))

# Question 2: How many people use each type of supplement?
supplement_counts = df["Supplement"].value_counts()
print(supplement_counts)

# Question 3: What are the primary benefits reported by people who use both supplements?
both_benefit_counts = df.loc[
    df["Supplement"] == "Both", "Primary_Benefit"
].value_counts()
print(both_benefit_counts)
