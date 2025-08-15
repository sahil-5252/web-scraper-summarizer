"""
summarizer.py
----------------
Summarize a given text using a Hugging Face encoder–decoder model.
Default model: facebook/bart-large-cnn
"""

from transformers import pipeline, AutoTokenizer

'''
def summarize_text(text: str,
                   model_name: str = "facebook/bart-large-cnn",
                   max_len: int = 130,
                   min_len: int = 30) -> str:
    """
    Summarize the given text using a Hugging Face summarization model.

    Args:
        text (str): The article text to summarize.
        model_name (str): Hugging Face model name.
        max_len (int): Maximum length of the summary.
        min_len (int): Minimum length of the summary.

    Returns:
        str: The generated summary text.
    """
    if not text.strip():
        return "[ERROR] No text provided for summarization."

    # Check token length
    # tokenizer = AutoTokenizer.from_pretrained(model_name)
    # tokens = tokenizer.encode(text, truncation=False)
    # print(f"[DEBUG] Number of tokens in input: {len(tokens)}")

    summarizer = pipeline("summarization", model=model_name)

    # if len(tokens) > tokenizer.model_max_length:
    #    print(f"[WARNING] Input exceeds model max length ({tokenizer.model_max_length}). Chunking required.")

    # Summarization logic here...
    summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
    return summary[0]['summary_text']
'''

def summarize_text(text: str,
                   model_name: str = "facebook/bart-large-cnn",
                   max_len: int = 300,
                   min_len: int = 30) -> str:
    """
    Summarize input text using a Hugging Face summarization pipeline.
    Splits the text into chunks if it exceeds the model's max token limit.
    """
    if not text.strip():
        return "[ERROR] No text provided for summarization."

    summarizer = pipeline("summarization", model=model_name)

    # Hugging Face models have token limits; split long text into chunks of ~900 tokens worth of characters
    max_chunk_chars = 3500  # approx for BART (depends on language)
    chunks = [text[i:i+max_chunk_chars] for i in range(0, len(text), max_chunk_chars)]

    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=max_len, min_length=min_len, do_sample=False)
        summaries.append(summary[0]['summary_text'])

    # Optionally: join summaries and summarize again for a "summary of summaries"
    if len(summaries) > 1:
        combined = " ".join(summaries)
        final_summary = summarizer(combined, max_length=max_len, min_length=min_len, do_sample=False)
        return final_summary[0]['summary_text']

    return summaries[0]


if __name__ == "__main__":
    # Standalone testing
    sample_text = (
        "Artificial Intelligence (AI) is a rapidly evolving field, "
        "impacting industries ranging from healthcare to finance. "
        "With advancements in machine learning and deep learning, "
        "AI systems are now capable of performing tasks once thought "
        "to be uniquely human."
    )
    print(summarize_text(sample_text))