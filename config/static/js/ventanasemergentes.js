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
    const termino = this.value.trim();
    const sugerenciasContainer = document.getElementById('sugerencias_alternos');

    if (termino.length >= 2) {  
        fetch(`/buscar_productos?termino=${encodeURIComponent(termino)}`) 
            .then(response => response.json())
            .then(data => {
                sugerenciasContainer.innerHTML = '';

                if (data.length > 0) {
                    data.forEach(producto => {
                        const suggestion = document.createElement('div');
                        suggestion.className = 'sugerencia';
                        suggestion.textContent = producto.nombre;

                        suggestion.addEventListener('click', function() {
                            const alternosField = document.getElementById('alternos_seleccionados');
                            const alternos = alternosField.value.split(',').map(val => val.trim()).filter(Boolean);

                            if (!alternos.includes(producto.nombre)) { 
                                alternos.push(producto.nombre);
                                alternosField.value = alternos.join(',');
                            }

                            document.getElementById('buscar_alternos').value = '';
                            sugerenciasContainer.innerHTML = '';
                        });

                        sugerenciasContainer.appendChild(suggestion);
                    });
                } else {

                    const noResult = document.createElement('div');
                    noResult.className = 'sugerencia';
                    noResult.textContent = 'No se encontraron resultados';
                    sugerenciasContainer.appendChild(noResult);
                }
            });
    } else {
        sugerenciasContainer.innerHTML = '';
    }
});








// Cargar opciones de clientes al cargar la página
document.addEventListener('DOMContentLoaded', () => {
    fetch('/obtener-ids-clientes')
    .then(response => response.json())
    .then(ids => {
        const selectCliente = document.getElementById('id-cliente');
        ids.forEach(id => {
            const option = document.createElement('option');
            option.value = id;
            option.textContent = id;
            selectCliente.appendChild(option);
        });
    })
    .catch(error => console.error('Error:', error));
});



// Calcular el total del carrito
function calcularTotalCarrito() {
    let total = 0;
    // Obtener todos los elementos del carrito
    const productosCarrito = document.querySelectorAll('.producto-en-carrito');
    // Iterar sobre los elementos del carrito y sumar los precios
    productosCarrito.forEach((producto) => {
        const precioProducto = parseFloat(producto.dataset.precio);
        total += precioProducto;
    });
    return total;
}

// Función para abrir el modal de compra y mostrar el total del carrito
function abrirModalCompra() {
    // Obtener el total del carrito
    const totalCarrito = calcularTotalCarrito();

    // Mostrar el total del carrito en el campo de "Total" dentro del modal de compra
    const totalCarritoLabel = document.getElementById('totalCarrito');
    totalCarritoLabel.textContent = `$${totalCarrito.toFixed(2)}`;

    // Abrir el modal de compra
    const modalCompra = document.getElementById('modal-compra');
    modalCompra.style.display = 'block';
}
