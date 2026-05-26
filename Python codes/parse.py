import requests
from bs4 import BeautifulSoup
link = input("Enter the url you want to parse: ")
def parse(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        quotes = soup.find_all('div', class_='quote')
    
        if quotes:
            print("Article Titles:")
            for quote in quotes:
                quote_text = quote.find('span', class_='text').text.strip()
                author = quote.find('small', class_='author').text.strip()
                print(f"\"{quote_text}\" - {author}")
        else:
            print("No articles found with the specified class.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except Exception as e:
        print("An unexepected error occured: {e}")
parse(link)
    