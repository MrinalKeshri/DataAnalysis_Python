#In this challenge you must analyze demographic data using Pandas.

#You must use Pandas to answer the following questions:- 
#How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
#What is the average age of men?
#What is the percentage of people who have a Bachelor's degree?
#What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
#What percentage of people without advanced education make more than 50K?
#What is the minimum number of hours a person works per week?
#What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
#What country has the highest percentage of people that earn >50K and what is that percentage?
#Identify the most popular occupation for those who earn >50K in India.

import pandas as pd

def calculate_demographic_data(print_data=True):
    # Load data
    df = pd.read_csv('adult.data.csv')

    # 1. How many of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(
        (df['education'] == 'Bachelors').sum() / df.shape[0] * 100, 1)

    # 4 & 5. Percentage of people with and without advanced education earning >50K
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    higher_education_rich = round(
        (higher_education['salary'] == '>50K').sum() / higher_education.shape[0] * 100, 1)
    lower_education_rich = round(
        (lower_education['salary'] == '>50K').sum() / lower_education.shape[0] * 100, 1)

    # 6. Minimum hours per week
    min_work_hours = df['hours-per-week'].min()

    # 7. Percentage of people working minimum hours and earning >50K
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (min_workers['salary'] == '>50K').sum() / min_workers.shape[0] * 100, 1)

    # 8. Country with highest percentage of rich (>50K) people
    rich_by_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    total_by_country = df['native-country'].value_counts()
    rich_percentage_country = (rich_by_country / total_by_country * 100).round(1)
    highest_earning_country = rich_percentage_country.idxmax()
    highest_earning_country_percentage = rich_percentage_country.max()

    # 9. Most common occupation for rich people in India
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    # Return dictionary of all results
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_education_rich)
        print("Percentage without higher education that earn >50K:", lower_education_rich)
        print("Min work time:", min_work_hours)
        print("Percentage of rich among those who work fewest hours:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
