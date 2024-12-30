import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("/home/rebel/Roger/Training/100_Days_with_Python/Day_99/Space_Corrected.csv")

# Check the first few rows to understand the structure
print(data.head())

# Drop unnecessary or irrelevant columns (like 'Unnamed: 0' if it's an index column)
data.drop(columns=['Unnamed: 0'], inplace=True)

# Convert the 'Datum' column (assuming it contains launch dates) to datetime format
# Assuming 'Datum' column contains the date of launch
data['Datum'] = pd.to_datetime(data['Datum'], errors='coerce')

# Drop rows with invalid dates
data.dropna(subset=['Datum'], inplace=True)

# 1. Number of launches over time (by year)
launches_by_year = data.groupby(data['Datum'].dt.year).size()

# Plotting the number of launches over the years
plt.figure(figsize=(10, 6))
plt.plot(launches_by_year.index, launches_by_year.values, marker='o')
plt.title('Number of Space Missions Over Time', fontsize=14)
plt.xlabel('Year')
plt.ylabel('Number of Launches')
plt.grid(True)
plt.show()

# 2. Number of launches by company
launches_by_company = data['Company Name'].value_counts()

# Plotting the number of launches by company
plt.figure(figsize=(10, 6))
sns.barplot(x=launches_by_company.index, y=launches_by_company.values, palette='Set2')
plt.title('Number of Space Missions by Company', fontsize=14)
plt.xlabel('Company Name')
plt.ylabel('Number of Launches')
plt.xticks(rotation=45)
plt.show()

# 3. Status of rockets (assuming 'Status Rocket' column contains rocket status)
rocket_status = data['Status Rocket'].value_counts()

# Plotting rocket status distribution
plt.figure(figsize=(8, 6))
sns.barplot(x=rocket_status.index, y=rocket_status.values, palette='Set1')
plt.title('Rocket Status Distribution', fontsize=14)
plt.xlabel('Rocket Status')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()

# 4. Status of missions (assuming 'Status Mission' column contains mission status)
mission_status = data['Status Mission'].value_counts()

# Plotting mission status distribution
plt.figure(figsize=(8, 6))
sns.barplot(x=mission_status.index, y=mission_status.values, palette='Set3')
plt.title('Mission Status Distribution', fontsize=14)
plt.xlabel('Mission Status')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()

# 5. Additional Analysis: For example, filtering by a specific rocket type or company
# Here, we filter by a sample rocket type or company and analyze
sample_rocket_type = 'Falcon'  # Example rocket type (change as needed)
filtered_data = data[data['Rocket'].str.contains(sample_rocket_type, na=False)]

# Number of launches of the specific rocket type over time
launches_by_year_rocket = filtered_data.groupby(filtered_data['Datum'].dt.year).size()

# Plotting launches by year for a specific rocket type
plt.figure(figsize=(10, 6))
plt.plot(launches_by_year_rocket.index, launches_by_year_rocket.values, marker='o', color='orange')
plt.title(f'Number of Launches by {sample_rocket_type} Rocket Over Time', fontsize=14)
plt.xlabel('Year')
plt.ylabel('Number of Launches')
plt.grid(True)
plt.show()
