document.getElementById("searchForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const query = document.getElementById("query").value;
    const resultsDiv = document.getElementById("results");

    // 🔹 Mostrar pantalla de carga
    resultsDiv.innerHTML = `<p id="loading">⏳ Cargando resultados...</p>`;

    try {
        const response = await fetch("http://127.0.0.1:8000/recommend", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ query }),
        });

        const data = await response.json();
        displayResults(data);
    } catch (error) {
        resultsDiv.innerHTML = `<p style="color: red;">❌ Error al obtener resultados</p>`;
    }
});

function displayResults(data) {
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = `<h2>Resultados para: ${data.query}</h2>`;

    // Mostrar la respuesta generada por el modelo LLM
    const llmDiv = document.createElement("div");
    llmDiv.innerHTML = `<p>${data.llm_response}</p>`;
    resultsDiv.appendChild(llmDiv);

    // Crear tabla de productos recomendados
    const table = document.createElement("table");
    table.innerHTML = `
        <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Descripción</th>
            <th>Similitud (%)</th>
        </tr>
    `;

    data.results.forEach(result => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${result.ID}</td>
            <td>${result["Person Name"]}</td>
            <td>${result.Description}</td>
            <td>${(result.Similarity * 100).toFixed(2)}%</td>
        `;
        table.appendChild(row);
    });

    resultsDiv.appendChild(table);
}
