from sentence_transformers import SentenceTransformer
import pandas as pd
import faiss
import numpy as np

# Cargar datos
df = pd.read_csv(r"C:\Users\hvera\Documents\projects\Retail-HyperAutomation-Solution\backend\data\products.csv")
descriptions = df["Description"].tolist()

# Generar embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')  # Modelo all-minilm
embeddings = model.encode(descriptions)

# Normalizar los embeddings
embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)

# Crear índice FAISS con producto escalar (Inner Product)
dimension = embeddings.shape[1]
index = faiss.IndexFlatIP(dimension)  # Usamos Inner Product para similitud del coseno
index.add(np.array(embeddings).astype('float32'))

# Guardar el índice FAISS
faiss.write_index(index, r"C:\Users\hvera\Documents\projects\Retail-HyperAutomation-Solution\backend\embeddings\product_embeddings.faiss")