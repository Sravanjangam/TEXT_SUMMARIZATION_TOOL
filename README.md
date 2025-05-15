# TEXT_SUMMARIZATION_TOOL

COMPANY: CODETECH IT SOLUTIONS

NAME: SRAVAN JANGAM

INTERN ID: CODF209

DOMAIN: Artificial Intelligence Markup Language

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

The "Text Summarizer Using NLTK" project is a simple yet effective natural language processing (NLP) application designed to extract the most important content from a large body of text. Using Python and the Natural Language Toolkit (NLTK) library, this project applies basic text processing and frequency-based sentence scoring to generate a concise summary that retains the core information. Text summarization is a crucial application of NLP, especially in an age where vast volumes of information are generated every second. This project focuses on extractive summarization, where key sentences are selected directly from the original text without altering their structure. This approach contrasts with abstractive summarization, which involves paraphrasing or generating new content — a more complex task typically requiring deep learning. The core component of the application is the TextSummarizer class. Upon initialization, the class downloads necessary resources like tokenizers and stopwords from NLTK. Stopwords (e.g., "the", "is", "and") and punctuation are filtered out since they carry little semantic weight in summarization tasks. The input text is first tokenized into individual words and sentences. Word frequency is then calculated for the remaining meaningful words. Each sentence is scored based on the cumulative frequency of the significant words it contains. The top N sentences with the highest scores are selected as the summary. The number of sentences in the summary can be customized, with three being the default. The sentences are then returned as a single summarized paragraph. An example block is included in the main() function for testing. This example uses a passage on artificial intelligence and demonstrates how the tool extracts the most relevant content. The result is printed, showing both the original text and the summarized output. This project is highly educational for beginners in NLP. It demonstrates key concepts like tokenization, stopword removal, frequency distribution, and sentence scoring. Moreover, it is implemented using only basic tools from NLTK and Python’s standard libraries, making it accessible and lightweight. In practical terms, such a summarizer can be integrated into news applications, document editors, chatbots, or digital assistants to enhance readability and save user time. Although simple, the frequency-based approach provides decent performance for general use and can serve as a foundation for more advanced NLP tasks involving semantic analysis or deep learning
OUTPUT:


![Image](https://github.com/user-attachments/assets/b2e52a64-5606-42a5-ad43-7c2014e7c9f4)


