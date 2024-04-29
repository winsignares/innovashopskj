document.addEventListener("DOMContentLoaded", function() {
    const filasProductos = document.querySelectorAll("table tbody tr.abrir-modal");

    filasProductos.forEach(fila => {
        fila.addEventListener("click", function() {
            const modalId = this.getAttribute("data-modal-id");
            const modal = document.getElementById(modalId);

            const celdas = this.querySelectorAll("td");

            const imgUrl = celdas[0].querySelector("img").src;
            const id = celdas[1].textContent.trim(); // ID del producto
            const nombre = celdas[2].textContent.trim();
            const precioUni = celdas[3]. textContent.trim();
            const precioVenta = celdas[5]. textContent.trim();
            const cantidad = celdas[6]. textContent.trim();
            const cantidadMin = celdas[7]. textContent.trim();

            document.getElementById("imgdesc").src = imgUrl;

            const inputFields = document.querySelectorAll("#modal-DescripcionProducto .txt_box");
            inputFields[0].value = id;
            inputFields[1].value = nombre;
            inputFields[2].value = precioUni;
            inputFields[3].value = precioVenta;
            inputFields[4].value = cantidad;
            inputFields[5].value = cantidadMin;

            // Generar el código de barras para el ID del producto
            const barcodeElement = document.getElementById("barcode");
            JsBarcode(barcodeElement, id, {
                format: "CODE128",
                lineColor: "#000000",
                width: 2,
                height: 50,
                displayValue: true, // Muestra el valor del código de barras
            });

            modal.style.display = "flex"; // Muestra el modal
        });
    });

    document.querySelectorAll(".cerrar-modal").forEach(function(cerrar) {
        cerrar.addEventListener("click", function() {
            const modal = this.closest(".modal");
            modal.style.display = "none"; // Cierra el modal
        });
    });

    window.addEventListener("click", function(event) {
        if (event.target.classList.contains("modal")) {
            event.target.style.display = "none"; // Cierra el modal si se hace clic fuera
        }
    });
});







document.addEventListener("DOMContentLoaded", function() {
    var botonImprimir = document.getElementById("imprimir-pdf");
    var contenido = document.querySelector("#modal-DescripcionProducto .found");

    if (botonImprimir && contenido) {
        botonImprimir.addEventListener("click", function() {
            contenido.querySelectorAll('label, .txt_box').forEach(el => {
                el.style.color = "#000";
            });

            var opciones = {
                filename: 'descripcion_producto.pdf',
                jsPDF: { orientation: 'portrait', unit: 'mm', format: 'a4' },
                html2canvas: { scale: 2 }
            };

            html2pdf().set(opciones).from(contenido).save();
        });
    } else {
        console.error("Botón de impresión o contenido para imprimir no encontrado.");
    }
});






