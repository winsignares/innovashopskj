document.addEventListener("DOMContentLoaded", function() {
    const preciouniInput = document.querySelector("input[name='preciouni']");
    const precioGananciaInput = document.querySelector("input[name='precio_ganancia']");
    const ivaInput = document.querySelector("input[name='iva']");
    const precioVentaInput = document.querySelector("input[name='precio_venta']");

    function calcularPrecioVenta() {
        const preciouni = parseFloat(preciouniInput.value) || 0;
        const ganancia = parseFloat(precioGananciaInput.value) || 0;
        const iva = parseFloat(ivaInput.value) || 0;
        
        const gananciaTotal = preciouni * (ganancia / 100);
        const ivaTotal = (preciouni + gananciaTotal) * (iva / 100);
        const precioVenta = preciouni + gananciaTotal + ivaTotal;

        precioVentaInput.value = precioVenta.toFixed(2);
    }

    preciouniInput.addEventListener("input", calcularPrecioVenta);
    precioGananciaInput.addEventListener("input", calcularPrecioVenta);
    ivaInput.addEventListener("input", calcularPrecioVenta);
});
