# Supplement Impact Dataset — Three Data Questions

## Why I Chose This Dataset
I chose the Supplement Impact dataset because it contains information about supplement use and different outcomes such as weight, strength gain, and primary benefit. Each row represents one participant, and the columns describe characteristics such as age, gender, supplement, number of weeks, initial weight, final weight, and strength gain. I thought this dataset would be useful because it has both numerical and categorical information,
so it can be explored using simple Pandas filtering and counting. It also makes it possible to ask questions about different supplement groups and the benefits reported by participants.


# Question: What are the age, gender, weeks, and weights of the first 10 people who use Creatine Monohydrate?

#creatine_data = df.loc[df["Supplement"] == "Creatine Monohydrate", ["Age", "Gender", "Weeks", "Initial_WT", "Final_WT"]]
#print(creatine_data.head(10))

#output:
 Age     Gender  Weeks  Initial_WT  Final_WT
  64       Male      5        79.1      81.2
  65     Female     11        76.0      76.8
  40       Male     22        51.7      54.2
  58 Non-Binary     12        58.9      60.6
  58 Non-Binary     23        93.2      94.3
  61       Male     19        84.0      84.5
  58 Non-Binary     20        86.8      88.2
  27 Non-Binary     23        88.5      90.0
  24 Non-Binary      7        80.5      82.9
  19 Non-Binary     16        91.6      93.8

Why the data structure supports this question:

This works because the dataset is tabular, with each row representing one participant.
The Supplement column contains a categorical label, so we can filter the rows where the
supplement is Creatine Monohydrate. The other columns contain the information we want to
look at for those participants.


# Question: How many people use each type of supplement?

#supplement_counts = df["Supplement"].value_counts()
#print(supplement_counts)

#output:
Supplement
Both                    344
Mass Gainer             339
Creatine Monohydrate    317

Why the data structure supports this question:

This works because Supplement is a categorical column with a value for each participant.
Since each row represents one participant, counting the frequency of each supplement category gives the number of participants in each group.


# Question: What are the primary benefits reported by people who use both supplements?

#both_benefit_counts = df.loc[df["Supplement"] == "Both", "Primary_Benefit"].value_counts()
#print(both_benefit_counts)

#output:
Primary_Benefit
Cognitive Support    79
Weight Gain          74
Bone Density         69
Strength Gain        66
Muscle Recovery      56

Why the data structure supports this question:

This dataset allows us to filter one column and summarize another column.
We can select participants whose Supplement value is "Both" and then count the different
Primary_Benefit categories within that group. This gives a breakdown of reported benefits
for participants who use both supplements.


## What the Data Cannot Answer

A question I might want to answer is: Did using a particular supplement cause participants
to gain more weight or strength? This dataset cannot answer that question by itself because
it does not provide a controlled comparison or enough information about other factors that
could affect weight and strength, such as diet, exercise routine, or dosage. The dataset has
initial weight, final weight, weeks, and strength gain, but simply observing differences between supplement groups does not prove that the supplement caused those differences. It would be misleading to assume that an association between supplement use and an outcome automatically means the supplement was the cause.
