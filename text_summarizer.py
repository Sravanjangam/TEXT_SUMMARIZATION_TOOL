# Import necessary libraries from NLTK and Python standard libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from string import punctuation
from heapq import nlargest

# Define a class for summarizing text
class TextSummarizer:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')

        # Create a set of stop words and punctuation to exclude from analysis
        self.stopwords = set(stopwords.words('english') + list(punctuation))

    def summarize(self, text, num_sentences=3):
        # Tokenize the text into sentences
        sentences = sent_tokenize(text)
        
        # Tokenize words and remove stopwords
        words = word_tokenize(text.lower())
        word_tokens = [word for word in words if word not in self.stopwords]

        # Count how often each word appears in the text
        freq = FreqDist(word_tokens)

        # Calculate sentence scores based on word frequency
        sentence_scores = {}
        for sentence in sentences:
            for word in word_tokenize(sentence.lower()):
                if word in freq:
                    if sentence not in sentence_scores:
                        sentence_scores[sentence] = freq[word]
                    else:
                        sentence_scores[sentence] += freq[word]

        # Get the summary (top N sentences)
        summary_sentences = nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
        summary = ' '.join(summary_sentences)
        
        return summary

def main():
    # Example usage
    text = """
    Artificial intelligence (AI) is a rapidly evolving technology that enables machines to mimic human cognitive functions such as learning, reasoning, and problem-solving.
    It powers applications like speech recognition, recommendation systems, autonomous vehicles, and medical diagnostics. 
    Machine learning, a subset of AI, allows systems to improve performance by analyzing data without explicit programming. 
    Deep learning, a more advanced approach, uses neural networks to process complex patterns and make predictions.
    AI has revolutionized industries by increasing efficiency, reducing human errors, and automating repetitive tasks.
    However, ethical concerns arise regarding privacy, bias, and job displacement as AI becomes more integrated into daily life.
    Researchers aim to develop responsible AI systems that align with human values and societal needs.
    The future of AI promises advancements in personalized healthcare, smarter automation, and enhanced creative collaboration.
    While AI continues to enhance productivity and innovation, its long-term impact requires careful consideration and regulation. 
    With proper guidance, AI can serve as a powerful tool to improve human experiences while minimizing potential risks.
    """

    summarizer = TextSummarizer()
    summary = summarizer.summarize(text, num_sentences=3)
    
    print("Original Text:")
    print(text.strip())
    print("\nSummary:")
    print(summary)

if __name__ == "__main__":
    main()