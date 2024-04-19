import pandas as pd

# Load the dataset
df = pd.read_csv('census_data.csv')

# Question 1: How many people of each race are represented in this dataset?
race_count = df['race'].value_counts()

# Question 2: What is the average age of men?
average_age_men = df[df['sex'] == 'Male']['age'].mean()

# Question 3: What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = (df['education'] == 'Bachelors').mean() * 100

# Question 4: What percentage of people with advanced education make more than 50K?
higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
percentage_higher_education = (higher_education['salary'] == '>50K').mean() * 100

# Question 5: What percentage of people without advanced education make more than 50K?
lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
percentage_lower_education = (lower_education['salary'] == '>50K').mean() * 100

# Question 6: What is the minimum number of hours a person works per week?
min_work_hours = df['hours-per-week'].min()

# Question 7: What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
num_min_workers = df[df['hours-per-week'] == min_work_hours]
rich_percentage = (num_min_workers['salary'] == '>50K').mean() * 100

# Question 8: What country has the highest percentage of people that earn >50K and what is that percentage?
highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).idxmax()
highest_earning_country_percentage = (df[df['native-country'] == highest_earning_country]['salary'] == '>50K').mean() * 100

# Question 9: Identify the most popular occupation for those who earn >50K in India.
top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

# Print the results
print("Question 1: ", race_count)
print("Question 2: ", round(average_age_men, 1))
print("Question 3: ", round(percentage_bachelors, 1))
print("Question 4: ", round(percentage_higher_education, 1))
print("Question 5: ", round(percentage_lower_education, 1))
print("Question 6: ", min_work_hours)
print("Question 7: ", round(rich_percentage, 1))
print("Question 8: ", highest_earning_country, " with ", round(highest_earning_country_percentage, 1), "%")
print("Question 9: ", top_IN_occupation)
