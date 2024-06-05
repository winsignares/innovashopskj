document.addEventListener('DOMContentLoaded', () => {
    let totalCarrito = 0;
    const totalCarritoLabel = document.getElementById('totalCarrito');
    const productosEnCarrito = document.getElementById('productos-en-carrito');
    const botonesAgregarCarrito = document.querySelectorAll('.agregar-al-carrito');
    let carrito = [];

    // Función para actualizar el contenido del carrito y el total
    function actualizarContenidoCarrito() {
        productosEnCarrito.innerHTML = '';
        carrito.forEach(producto => {
            const productoHTML = `
                <div class="producto-en-carrito">
                    <span>${producto.nombre}</span>
                    <span>Cantidad: ${producto.cantidad}</span>
                    <span>Precio: $${producto.precio}</span>
                </div>
            `;
            productosEnCarrito.innerHTML += productoHTML;
        });
        totalCarritoLabel.textContent = `$${totalCarrito.toFixed(2)}`;
    }

    // Función para agregar un producto al carrito
    function agregarAlCarrito(id, nombre, precio) {
        const productoExistente = carrito.find(item => item.id === id);
        if (productoExistente) {
            productoExistente.cantidad++;
        } else {
            carrito.push({ id, nombre, precio, cantidad: 1 });
        }
        totalCarrito += parseFloat(precio);
        actualizarContenidoCarrito();
    }

    // Manejar el clic en los botones "Agregar al carrito"
    botonesAgregarCarrito.forEach(boton => {
        boton.addEventListener('click', () => {
            const productoId = boton.getAttribute('data-producto-id');
            const productoNombre = boton.parentElement.querySelector('label').textContent;
            const productoPrecio = boton.getAttribute('data-producto-precio');
            agregarAlCarrito(productoId, productoNombre, productoPrecio);
        });
    });

    // Manejar la compra cuando se hace clic en "Completar compra"
    document.getElementById('HacerCompra').addEventListener('click', () => {
        fetch('/completar-compra', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ productos: carrito, total: totalCarrito })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Compra completada con éxito');
                carrito = [];
                totalCarrito = 0;
                actualizarContenidoCarrito();
            } else {
                alert('Hubo un error al completar la compra');
            }
        })
        .catch(error => console.error('Error:', error));
    });

    // Función para actualizar el contador de productos en el carrito
    function actualizarContadorCarrito() {
        document.getElementById('numProductosCarrito').textContent = carrito.length;
    }

    // Event listener para el botón "Agregar al carrito"
    document.querySelectorAll('.btnAgregarCarrito').forEach(boton => {
        boton.addEventListener('click', () => {
            // Incrementar el contador de productos en el carrito
            contadorCarrito++;
            // Actualizar el número mostrado en el botón del carrito
            actualizarContadorCarrito();
        });
    });

    // Función para agregar un producto al contenedor
    function agregarProductoAlContenedor(producto) {
        // Crear el elemento del producto
        const productoElemento = document.createElement('div');
        productoElemento.classList.add('productoInfo');
        productoElemento.innerHTML = `
            <img src="${producto.imagen}" alt="${producto.nombre}" class="imgProducto">
            <div class="info">
                <label class="nombre-producto">${producto.nombre}</label>
                <label class="precio-producto">${producto.precio}</label>
                <button type="button" class="btn btn-primary btn-lg agregar-al-carrito" data-producto-id="${producto.id}" data-producto-precio="${producto.precio}">Agregar al carrito</button>
            </div>
        `;

        // Agregar el producto al contenedor
        document.getElementById('contenedorProductos').appendChild(productoElemento);
    }

    // Agregar los productos al contenedor
    productos.forEach(producto => {
        agregarProductoAlContenedor(producto);
    });
});





