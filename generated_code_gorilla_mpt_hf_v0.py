from transformers import pipeline
import torch
summarizer = pipeline('summarization', model='google/pegasus-large')
text = "Text of the article here..."
summary = summarizer(text)[0]['summary_text']
print(summary)
