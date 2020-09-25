from summarizer import Summarizer
import json

def summarise(document):
    model = Summarizer()
    result = model(document, min_length=60)
    full = ''.join(result)
    return full

