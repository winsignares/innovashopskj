document.addEventListener("DOMContentLoaded", function () {

    const botonesParametrizacion = document.querySelectorAll(".abrir-modal[data-modal-id='modal-parametrizacion']");

    botonesParametrizacion.forEach(boton => {
        boton.addEventListener("click", function () {

            const fila = this.closest("tr");
            const productoId = fila.querySelector("td:nth-child(2)").textContent;
            

            const inputId = document.querySelector("#modal-parametrizacion input[name='id']");
            inputId.value = productoId;
        });
    });
});
