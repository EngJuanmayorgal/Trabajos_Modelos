function CambiarPersonaje() {
  document.getElementById("typeSelector").addEventListener("change", async function () {
    const type = this.value;
    if (!type) return;
    // Llamar al servlet para obtener los datos del personaje
    const response = await fetch(`EscogerServlet?type=${type}`);
    const data = await response.json();
    if (data.estado) {
      alert("Ya se tiene una fabrica" + data.estado);
    }
    // Mostrar personaje principal
    const main = document.getElementById("mainCharacter");
    main.innerHTML = `
    <div class="name" style="color: white; font-size:30px;" >${data.name}</div>
    <img src="${data.img}" alt="${type}" > 
    <button onclick="Reiniciar()">Reiniciar</button>`;

    // Mostrar partes
    const parts = document.getElementById("partsContainer");
    parts.innerHTML = "";
    data.parts.forEach(part => {
      const div = document.createElement("div");
      div.classList.add("part");
      div.innerHTML = `
          <img src="${part.img}" alt="Parte">
          <div class="info">${part.info}</div>
        `;
      parts.appendChild(div);
    });
  });
}

async function Reiniciar() {
  const response = await fetch("EscogerServlet", {
    method: "POST"
  });
  alert("Se reiniciara el personaje");
  location.reload();

}