# Article Summarizer with Web Scraping & Encoder–Decoder Model

This project scrapes the text from a user-provided article URL and summarizes it using a **Hugging Face encoder–decoder model** (BART by default).

---

## Project Structure
article_summarizer/
│
├── app.py # orchestrates scraping & summarization
├── scraper.py # fetches and cleans article text from given URL
├── summarizer.py # summarizes text using seq2seq LLM
├── README.md # documentation
└── requirements.txt # python dependencies


---

## Architecture Overview

### **1. Input**
- User provides the **URL** of an article.

### **2. Web Scraping (`scraper.py`)**
- Uses `requests` to download the HTML
- Parses the page with `BeautifulSoup`
- Extracts paragraph text (`<p>` tags)
- Cleans whitespace and combines into a single string

### **3. Summarization (`summarizer.py`)**
- Loads a Hugging Face summarization pipeline (default: `facebook/bart-large-cnn`)
- Optionally **chunks** long articles to fit within the model's token limit (prevents `IndexError`)
- Summarizes the text with specified `min_len` and `max_len` values
- Returns the final summary

### **4. Orchestration (`app.py`)**
- Gets the article text from `scraper.py`
- Passes it to `summarizer.py`
- Displays the summary in the terminal
- **Saves** the summary as a `.txt` file

---

## How to Run

### **Install Dependencies**
Make sure you have Python 3.8+ installed, then run:
```bash
pip install -r requirements.txt
```
or manually install
```bash
pip install requests beautifulsoup4 transformers torch
```
### **Run project**
In your terminal, navigate to the project directory and run:
```bash
python app.py
```
### Example output
```
Enter the article URL: https://example.com/sample-article
[INFO] Fetching article text...
[INFO] Article length: 854 words
[INFO] Summarizing article...

===== SUMMARY =====

This is the generated summary text...

[INFO] Summary saved to: /path/to/project/article_summary_20250815_102300.txt
```
