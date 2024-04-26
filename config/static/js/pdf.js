document.addEventListener("DOMContentLoaded", function() {
    var botonDescargar = document.querySelector(".btnpdf button");
    var factura = document.querySelector(".factura");

    botonDescargar.addEventListener("click", function() {
        // Opciones para html2pdf
        var opciones = {
            filename: 'factura.pdf', // Nombre del archivo PDF
            jsPDF: { orientation: 'portrait', unit: 'mm', format: 'a4' }, // Opciones de formato PDF
            html2canvas: { scale: 2 } // Escala para mayor resolución
        };

        // Convierte el contenido del div "factura" en PDF y descarga el archivo
        html2pdf().set(opciones).from(factura).save();
    });
});
