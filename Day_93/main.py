import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL to scrape (this is a test site)
url = 'https://books.toscrape.com/'  # Sample website for scraping book data

# Send an HTTP GET request to fetch the page content
response = requests.get(url)

# Check if the request was successful (status code 200 means OK)
if response.status_code == 200:
    print("Successfully fetched the webpage!")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    exit()

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find all books on the page (each book is contained within 'article' tags with class 'product_pod')
books = soup.find_all('article', class_='product_pod')

# List to store the extracted book data
book_data = []

# Loop through each book and extract the title, price, and availability
for book in books:
    title = book.find('h3').find('a')['title']  # Extract book title
    price = book.find('p', class_='price_color').text  # Extract book price
    availability = book.find('p', class_='instock availability').text.strip()  # Extract availability status

    # Append the extracted information to the book_data list
    book_data.append({
        'Title': title,
        'Price': price,
        'Availability': availability
    })

# Create a DataFrame from the list of dictionaries (book data)
df = pd.DataFrame(book_data)

# Print the first few rows of the DataFrame to check the data
print(df.head())

# Save the DataFrame to a CSV file for future use
df.to_csv('books.csv', index=False)

print("Data saved to 'books.csv'.")
