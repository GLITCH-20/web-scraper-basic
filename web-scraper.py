import requests
from bs4 import BeautifulSoup
import csv

print("Starting script...")

url = "https://books.toscrape.com/"
response = requests.get(url)
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    book_titles = soup.find_all('h3')

    print(f"Found {len(book_titles)} books:\n")

    # Open a CSV file to save the data
    with open('books.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Book Title"])  # Write header

        for book in book_titles:
            title = book.a['title']
            print(title)
            writer.writerow([title])  # Write book title to CSV
else:
    print("Failed to load the website.")
