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

document.getElementById('buscar_alternos').addEventListener('input', function() {
    const termino = this.value;
    const sugerenciasContainer = document.getElementById('sugerencias_alternos');

    if (termino.length >= 2) {  
        fetch(`/buscar_productos?termino=${termino}`)
            .then(response => response.json())
            .then(data => {

                sugerenciasContainer.innerHTML = '';

                data.forEach(producto => {
                    const suggestion = document.createElement('div');
                    suggestion.className = 'sugerencia';
                    suggestion.textContent = producto;

                    suggestion.addEventListener('click', function() {
                        const alternosField = document.getElementById('alternos_seleccionados');
                        alternosField.value += (alternosField.value ? ',' : '') + producto;  
                        document.getElementById('buscar_alternos').value = '';  
                        sugerenciasContainer.innerHTML = '';  
                    });

                    sugerenciasContainer.appendChild(suggestion);
                });
            });
    } else {
        sugerenciasContainer.innerHTML = ''; 
    }
});

