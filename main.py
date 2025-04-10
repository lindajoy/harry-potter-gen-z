print('Hello Friend, Ready to start your journey to Mordor alongside Frodo? 🥳')
print('Tell me your name')
x = input()
print('Hello ' + x + ', How are you?')

from langchain_community.document_loaders import DirectoryLoader

DATA_PATH = "data/books"

def load_data():
    # Load data from the directory
    loader = DirectoryLoader(DATA_PATH, glob="**/*.md")
    documents = loader.load()
    return documents

print('I am done!')
