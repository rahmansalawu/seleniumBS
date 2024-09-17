from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Import Service
from selenium.webdriver import ChromeOptions
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

def scrape_websites(urls):
    chrome_driver_path = "./chromedriver.exe"
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    history = []

    for url in urls:
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        text_content = soup.get_text(separator='\n', strip=True)
        
        history.append((url, text_content))

    driver.quit()
    return history

def display_scraped_data(history):
    for url, content in history:
        print(f"Scraped URL: {url}\n")
        print(content)
        print("\n" + "="*80 + "\n")  # Separator for styling

# Example usage
if __name__ == "__main__":
    urls_to_scrape = [
        "http://example.com",
        "http://example.org",
        # Add more URLs as needed
    ]
    scraped_history = scrape_websites(urls_to_scrape)
    display_scraped_data(scraped_history)