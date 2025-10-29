<<<<<<< HEAD
function CambiarPersonaje() {
  document.getElementById("typeSelector").addEventListener("change", async function () {
=======

document.getElementById("typeSelector").addEventListener("change", async function () {
>>>>>>> d4f00e2851bdac93d533cced804862ea0fc00432
    const type = this.value;
    if (!type) return;
    // Llamar al servlet para obtener los datos del personaje
    const response = await fetch(`EscogerServlet?type=${type}`);
    const data = await response.json();
<<<<<<< HEAD
    if (data.estado) {
      alert("Ya se tiene una fabrica" + data.estado);
    }
    // Mostrar personaje principal
    const main = document.getElementById("mainCharacter");
    main.innerHTML = `
    <div class="name" style="color: white; font-size:30px;" >${data.name}</div>
    <img src="${data.img}" alt="${type}" > 
    <button onclick="Reiniciar()">Reiniciar</button>`;
=======

    // Mostrar personaje principal
    const main = document.getElementById("mainCharacter");
    main.innerHTML = `<img src="${data.img}" alt="${type}">`;
>>>>>>> d4f00e2851bdac93d533cced804862ea0fc00432

    // Mostrar partes
    const parts = document.getElementById("partsContainer");
    parts.innerHTML = "";
    data.parts.forEach(part => {
<<<<<<< HEAD
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
=======
        const div = document.createElement("div");
        div.classList.add("part");
        div.innerHTML = `
          <img src="${part.img}" alt="Parte">
          <div class="info">${part.info}</div>
        `;
        parts.appendChild(div);
    });
});
>>>>>>> d4f00e2851bdac93d533cced804862ea0fc00432
