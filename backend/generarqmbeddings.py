from sentence_transformers import SentenceTransformer
import pandas as pd
import faiss
import numpy as np
import os

# Load data
# Get the path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Build the relative path to the CSV file
csv_path = os.path.join(current_dir, "data", "products.csv")

# Load data
df = pd.read_csv(csv_path)
descriptions = df["Description"].tolist()

# Generate embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')  # all-MiniLM model
embeddings = model.encode(descriptions)

# Normalize the embeddings
embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)

# Create FAISS index with Inner Product
dimension = embeddings.shape[1]
index = faiss.IndexFlatIP(dimension)  # Using Inner Product for cosine similarity
index.add(np.array(embeddings).astype('float32'))

# Build the relative path to save the FAISS index
faiss_index_path = os.path.join(current_dir, "embeddings", "product_embeddings.faiss")

# Save the FAISS index
faiss.write_index(index, faiss_index_path)