import sumy
import nltk

'''
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer

def summarize_text(text, summary_ratio=0.2):
    """
    Summarize the given text using the Luhn algorithm.
    
    Args:
        text (str): The input text to be summarized.
        summary_ratio (float): The desired ratio of the summary length to the original text length (between 0 and 1).
        
    Returns:
        str: The summarized text.
    """
    # Parse the input text
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    
    # Create the LuhnSummarizer instance
    summarizer = LuhnSummarizer()
    
    # Summarize the text
    summary = summarizer(parser.document, summary_ratio)
    
    # Join the summary sentences into a single string
    summarized_text = " ".join([str(sentence) for sentence in summary])
    
    return summarized_text

'''

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer

def summarize_text(text, num_sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LuhnSummarizer()
    summary = summarizer(parser.document, num_sentences)
    summarized_text = " ".join([str(sentence) for sentence in summary])
    return summarized_text