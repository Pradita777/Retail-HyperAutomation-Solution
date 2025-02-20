from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from sentence_transformers import SentenceTransformer
import ollama
import faiss
import numpy as np
import pandas as pd
import requests  # Para llamar a Ollama

app = FastAPI()

# Configurar CORS para evitar errores en el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cargar datos y modelo de embeddings
df = pd.read_csv("data/products.csv")
model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index("embeddings/product_embeddings.faiss")

def query_ollama(prompt: str) -> str:
    try:
        response = ollama.chat(
            model='mistral',
            messages=[
                {
                    'role': 'user',
                    'content': prompt,
                },
            ]
        )
        
        # Extraer el contenido de la respuesta
        response_content = response['message']['content']
        
        return response_content
    
    except Exception as e:
        # Manejar cualquier error que pueda ocurrir
        print(f"❌ Error: {e}")  # <-- DEBUG
        return f"❌ Error: {e}"

@app.post("/recommend")
async def recommend(request: Request):
    data = await request.json()
    query = data.get("query")

    # 1️⃣ Generar embedding para la consulta
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype('float32')

    # Normalizar el embedding de la consulta
    query_embedding = query_embedding / np.linalg.norm(query_embedding)

    # 2️⃣ Buscar productos similares en la base de datos
    k = 3  # Número de resultados
    similarities, indices = index.search(query_embedding, k)  # Usamos Inner Product (similitud del coseno)

    # 3️⃣ Preparar lista de productos recomendados
    results = []
    for i, idx in enumerate(indices[0]):
        product = df.iloc[idx]
        similarity = float(similarities[0][i])  # Similitud del coseno (ya está normalizada)
        results.append({
            "Product_ID": int(product["Product_ID"]),
            "Product Name": str(product["Product Name"]),
            "Category": str(product["Category"]),
            "Description": str(product["Description"]),
            "Similarity": similarity
        })

    # 4️⃣ Llamar a Ollama para generar respuesta
    ollama_prompt = f"Based on this query: '{query}', what recommendations can you give?"
    llm_text = query_ollama(ollama_prompt)

    # 5️⃣ Devolver respuesta con productos y el texto generado por Ollama
    return {
        "query": query,
        "llm_response": llm_text,
        "results": results
    }
