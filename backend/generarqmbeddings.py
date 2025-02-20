from sentence_transformers import SentenceTransformer
import pandas as pd
import faiss
import numpy as np
import os

# Cargar datos
# Obtener la ruta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta relativa al archivo CSV
csv_path = os.path.join(current_dir, "data", "products.csv")

# Cargar datos
df = pd.read_csv(csv_path)
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

# Construir la ruta relativa para guardar el índice FAISS
faiss_index_path = os.path.join(current_dir, "embeddings", "product_embeddings.faiss")

# Guardar el índice FAISS
faiss.write_index(index, faiss_index_path)