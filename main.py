import streamlit as st
from scrape import scrape_websites  # Update the import to the new function

st.title("Chatbot")
urls = st.text_area("Enter the URLs of the websites you want to scrape (one per line)", placeholder="https://example.com\nhttps://example.org")
scrape_button = st.button("Scrape", disabled=not urls)

if scrape_button:
    st.write("Scraping the websites...")
    url_list = urls.splitlines()  # Split the input into a list of URLs
    scraped_history = scrape_websites(url_list)  # Call the updated function

    for url, content in scraped_history:
        st.write(f"**Scraped URL:** {url}")
        st.write(content)
        st.write("---")  # Separator for styling
