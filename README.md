# Hyperautomation Web Solution

This project is a web solution focused on hyperautomation that uses natural language processing (LLM) and embeddings for product recommendation.

## Technologies Used
- **Backend**: FastAPI
- **Embeddings**: FAISS, SentenceTransformers
- **LLM Models**: Ollama with `mistral` and `all-minilm:33m`
- **Frontend**: HTML + JavaScript
- **Database**: CSV + FAISS

## Project Structure
```
SolucionHiperautomatizacion/
│-- data/
│   └── products.csv  # Product file with columns: ID, Person Name, Description
│-- embeddings/
│   └── product_embeddings.faiss  # FAISS index of product embeddings
│-- main.py  # FastAPI server for product recommendation
│-- generarqmbeddings.py  # Code to generate the FAISS index
│-- requirements.txt  # Project dependencies
│-- frontend/
│   ├── index.html  # Graphical interface
│   ├── script.js  # Logic to interact with the API
```

## Requirements
1. Have the following Ollama models running locally:
  ```bash
  ollama pull nomic-embed-text
  ollama pull mistral
  ollama list
  ```
  Expected output:
  ```
  NAME              ID              SIZE      MODIFIED
  all-minilm:33m    4f5da3bd944d    67 MB     7 hours ago
  mistral:latest    f974a74358d6    4.1 GB    12 days ago
  ```

2. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

3. Run the FastAPI server:
  ```bash
  uvicorn main:app --reload
  ```

4. Open `index.html` in a browser.

## API Endpoints
### `POST /recommend`
- **Description**: Receives a user query and recommends products based on embeddings and an LLM model.
- **Body (JSON)**:
  ```json
  {
   "query": "Laptops for programming"
  }
  ```
- **Response (JSON)**:
  ```json
   {
    "query": "Laptops for programming",
    "llm_response": "Based on this query, I recommend...",
    "results": [
      {
       "ID": 101,
       "Person Name": "Laptop X",
       "Description": "Powerful laptop for coding",
       "Similarity": 0.89
      }
    ]
   }
   ```



## Contact
For questions or improvements, open an issue in this repository.

---
Thank you for using this solution! 🚀
