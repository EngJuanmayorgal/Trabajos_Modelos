<%-- Document : index Created on : 15 sept 2025, 19:26:06 Author : juan mayorga --%>

    <%@page contentType="text/html" pageEncoding="UTF-8" %>
        <!DOCTYPE html>
        <html lang="es">

        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Selección de Personaje</title>
            <link rel="stylesheet" href="css/styles.css">
        </head>

        <body style="background: url('images/fondo.jpeg'); background-size: cover; background-attachment: fixed;">
            <div class="container">
                <!-- Personaje principal -->
                <div class="main-character" id="mainCharacter">
                    <p>Selecciona un tipo de personaje</p>
                </div>

                <!-- Barra lateral -->
                <div class="sidebar">
                    <!-- Selección de tipo de personaje -->
                    <div class="character-type">
                        <select id="typeSelector" onchange="changeCharacterType()">
                            <option value="">-- Escoge tipo --</option>
                            <option value="humano">Humano</option>
                            <option value="elfo">Elfo</option>
                            <option value="enano">Enano</option>
                            <option value="orco">Orco</option>
                        </select>
                    </div>

                    <!-- Partes del personaje -->
                    <div class="parts" id="partsContainer">
                        <div class="part">
                            <img src="images/fondo.jpeg" alt="Arma">
                            <div class="info">Arma del personaje</div>
                        </div>
                        <div class="part">
                            <img src="images/fondo.jpeg" alt="Armadura">
                            <div class="info">Armadura del personaje</div>
                        </div>
                        <div class="part">
                            <img src="images/fondo.jpeg" alt="Montura">
                            <div class="info">Montura del personaje</div>
                        </div>
                    </div>
                </div>
            </div>
            <script src="index.js"></script>
        </body>

        </html>