"""
scraper.py
----------------
Fetch and clean article text from a given URL.
Uses requests to download the HTML and BeautifulSoup to parse and extract the text.
"""

import requests
from bs4 import BeautifulSoup


def get_article_text(url: str) -> str:
    """
    Fetch and clean the article text from the given URL.

    Args:
        url (str): The URL of the article.

    Returns:
        str: The cleaned article text, or an empty string if fetching fails.
    """
    try:
        # Send GET request
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch article: {e}")
        return ""

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract paragraph text
    paragraphs = soup.find_all("p")
    article_text = " ".join(p.get_text().strip() for p in paragraphs)

    # Normalize whitespace
    article_text = " ".join(article_text.split())

    return article_text


if __name__ == "__main__":
    # Standalone testing
    url = input("Enter the article URL: ").strip()
    text = get_article_text(url)
    if text:
        print("\n===== ARTICLE TEXT PREVIEW =====\n")
        print(text[:1000] + "..." if len(text) > 1000 else text)
    else:
        print("[ERROR] Could not fetch article.")
