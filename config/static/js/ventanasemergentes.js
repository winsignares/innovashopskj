//Codigo para las ventanas emergentes
document.querySelectorAll(".abrir-modal").forEach(function (boton) {
    boton.addEventListener("click", function () {
        event.stopPropagation();
        var modalId = this.getAttribute("data-modal-id");
        var modal = document.getElementById(modalId);
        modal.style.display = "flex";
    });
});

document.querySelectorAll(".cerrar-modal").forEach(function (cerrar) {
    cerrar.addEventListener("click", function () {
        var modal = this.closest(".modal");
        modal.style.display = "none";
    });
});

window.addEventListener("click", function (event) {
    if (event.target.classList.contains("modal")) {
        event.target.style.display = "none"; 
    }
});


//Codigo para buscar los productos alternos
document.getElementById('buscar_alternos').addEventListener('input', function() {
    const termino = this.value.trim(); // Asegúrate de eliminar espacios al inicio y al final
    const sugerenciasContainer = document.getElementById('sugerencias_alternos');

    if (termino.length >= 2) {  
        fetch(`/buscar_productos?termino=${encodeURIComponent(termino)}`) // Codifica el término para evitar problemas de seguridad
            .then(response => response.json())
            .then(data => {
                sugerenciasContainer.innerHTML = '';

                if (data.length > 0) {
                    data.forEach(producto => {
                        // Asegúrate de usar `producto.nombre` para el texto de la sugerencia
                        const suggestion = document.createElement('div');
                        suggestion.className = 'sugerencia';
                        suggestion.textContent = producto.nombre; // Muestra el nombre del producto

                        suggestion.addEventListener('click', function() {
                            const alternosField = document.getElementById('alternos_seleccionados');
                            const alternos = alternosField.value.split(',').map(val => val.trim()).filter(Boolean);

                            // Comprueba si el producto ya está en la lista para evitar duplicados
                            if (!alternos.includes(producto.nombre)) { 
                                alternos.push(producto.nombre); // Añade el nombre del producto a la lista
                                alternosField.value = alternos.join(','); // Actualiza el campo oculto con valores separados por comas
                            }

                            document.getElementById('buscar_alternos').value = ''; // Limpiar el campo de entrada
                            sugerenciasContainer.innerHTML = '';  // Limpiar las sugerencias
                        });

                        sugerenciasContainer.appendChild(suggestion); // Añadir la sugerencia al contenedor
                    });
                } else {
                    // Si no hay resultados, muestra un mensaje apropiado
                    const noResult = document.createElement('div');
                    noResult.className = 'sugerencia';
                    noResult.textContent = 'No se encontraron resultados';
                    sugerenciasContainer.appendChild(noResult);
                }
            });
    } else {
        sugerenciasContainer.innerHTML = ''; // Limpiar sugerencias si el término es muy corto
    }
});

