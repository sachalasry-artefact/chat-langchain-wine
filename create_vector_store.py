"""Load html from files, clean up, split, ingest into Weaviate."""
import pickle

from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS

from langchain.document_loaders import CSVLoader
import pandas as pd

def create_vector_store():
    """Load documents."""
    #loader = ReadTheDocsLoader("langchain.readthedocs.io/en/latest/")

    sample_size = 10
    df = pd.read_csv("data/winemag-data-130k-v2.csv").drop(columns=["Unnamed: 0"]).head(sample_size)
    df.to_csv(f"data/sample_to_test_{sample_size}.csv", index=False)
    loader = CSVLoader(file_path="data/sample_to_test.csv")
    raw_documents = loader.load()
    #text_splitter = RecursiveCharacterTextSplitter(
    #    chunk_size=1000,
    #    chunk_overlap=200,
    #)

    #documents = text_splitter.split_documents(raw_documents)
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(raw_documents, embeddings)

    # Save vectorstore
    with open(f"vectorstore_moet.pkl", "wb") as f:
        pickle.dump(vectorstore, f)


if __name__ == "__main__":
    create_vector_store()
