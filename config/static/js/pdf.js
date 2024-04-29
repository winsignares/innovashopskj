document.addEventListener("DOMContentLoaded", function() {
    var botonDescargar = document.querySelector(".btnpdf button");
    var factura = document.querySelector(".factura");

    botonDescargar.addEventListener("click", function() {

        var opciones = {
            filename: 'factura.pdf',
            jsPDF: { orientation: 'portrait', unit: 'mm', format: 'a4' }, 
            html2canvas: { scale: 2 } 
        };

        html2pdf().set(opciones).from(factura).save();
    });
});
