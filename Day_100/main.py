import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets (replace 'police_deaths.csv' and 'census_data.csv' with the actual file paths)
police_deaths = pd.read_csv('police_deaths.csv')  # Dataset of police deaths
census_data = pd.read_csv('census_data.csv')  # Dataset of U.S. census data

# Preprocess the police deaths data
# Ensure that the 'date' column is in datetime format and handle missing values
police_deaths['date'] = pd.to_datetime(police_deaths['date'], errors='coerce')
police_deaths.dropna(subset=['date'], inplace=True)  # Remove rows with missing date
police_deaths['year'] = police_deaths['date'].dt.year  # Extract the year from the date

# Explore the data
print(police_deaths.head())
print(census_data.head())

# Merge the datasets based on the 'state' column (or other relevant column depending on the dataset)
merged_data = pd.merge(police_deaths, census_data, how='inner', on='state')

# Analyze deaths by year
deaths_by_year = police_deaths.groupby('year').size()

# Plotting the number of deaths by year
plt.figure(figsize=(10, 6))
plt.plot(deaths_by_year.index, deaths_by_year.values, marker='o', color='blue')
plt.title('Number of Police Deaths in the US by Year', fontsize=14)
plt.xlabel('Year')
plt.ylabel('Number of Deaths')
plt.grid(True)
plt.show()

# 1. Racial Disparities: Number of police deaths by race
deaths_by_race = police_deaths['race'].value_counts()

# Plotting racial disparities
plt.figure(figsize=(8, 6))
sns.barplot(x=deaths_by_race.index, y=deaths_by_race.values, palette='Set2')
plt.title('Number of Police Deaths by Race', fontsize=14)
plt.xlabel('Race')
plt.ylabel('Number of Deaths')
plt.xticks(rotation=45)
plt.show()

# 2. Analyzing the relationship between income level and police deaths
# Assuming 'income_level' is a column in the census data that contains average income by state
merged_data['income_level'] = pd.to_numeric(merged_data['income_level'], errors='coerce')

# Correlation between income level and police deaths
income_death_corr = merged_data[['income_level', 'year']].groupby('year').size()

# Plotting income level vs police deaths
plt.figure(figsize=(10, 6))
plt.plot(income_death_corr.index, income_death_corr.values, marker='x', color='red')
plt.title('Income Level vs. Police Deaths Over Time', fontsize=14)
plt.xlabel('Year')
plt.ylabel('Number of Deaths')
plt.grid(True)
plt.show()

# 3. Regional analysis: Deaths by region
# Assuming 'region' is a column in the census dataset
deaths_by_region = merged_data.groupby('region')['year'].count()

# Plotting deaths by region
plt.figure(figsize=(10, 6))
sns.barplot(x=deaths_by_region.index, y=deaths_by_region.values, palette='Set1')
plt.title('Police Deaths by Region', fontsize=14)
plt.xlabel('Region')
plt.ylabel('Number of Deaths')
plt.xticks(rotation=45)
plt.show()

# 4. Hypothesis Testing (Optional): Test if the racial disparity is statistically significant
from scipy import stats

# Conducting a chi-squared test for racial disparity in police deaths (assuming 'race' and 'status' columns)
contingency_table = pd.crosstab(police_deaths['race'], police_deaths['status'])
chi2, p, _, _ = stats.chi2_contingency(contingency_table)

# Output the result of the chi-squared test
print(f"Chi-squared: {chi2}, p-value: {p}")
if p < 0.05:
    print("There is a statistically significant relationship between race and the status of police deaths.")
else:
    print("There is no statistically significant relationship between race and the status of police deaths.")
