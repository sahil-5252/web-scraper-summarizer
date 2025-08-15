"""
app.py
----------------
Main application to scrape an article and summarize it.
Also saves the generated summary to a text file in the same folder.
"""

import os
from datetime import datetime
from scraper import get_article_text
from summarizer import summarize_text


def save_summary_to_file(summary_text: str) -> str:
    """
    Saves the summary text to a file in the current directory.

    Args:
        summary_text (str): The summary to save.

    Returns:
        str: The path to the saved file.
    """
    # Directory of the current file (app.py)
    script_dir = os.path.dirname(os.path.abspath(__file__))

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"article_summary_{timestamp}.txt"
    filepath = os.path.join(script_dir, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(summary_text)

    return filepath


def main():
    """
    Orchestrates the scraping, summarization, and file export process.
    """
    url = input("Enter the article URL: ").strip()

    # Step 1: Scrape
    print("[INFO] Fetching article text...")
    article_text = get_article_text(url)

    if not article_text:
        print("[ERROR] Failed to retrieve article content.")
        return

    print(f"[INFO] Article length: {len(article_text.split())} words")

    # Step 2: Summarize
    print("[INFO] Summarizing article...")
    summary = summarize_text(article_text)

    # Step 3: Output
    print("\n===== SUMMARY =====\n")
    print(summary)

    # Step 4: Save to file
    file_path = save_summary_to_file(summary)
    print(f"\n[INFO] Summary saved to: {file_path}")


if __name__ == "__main__":
    main()