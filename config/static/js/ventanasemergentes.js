var abrirModal = document.getElementById("abrir-modal");
var modal = document.getElementById("mi-modal");
var cerrarModal = document.querySelector(".cerrar-modal");

abrirModal.addEventListener("click", function () {
    modal.style.display = "flex";
});

cerrarModal.addEventListener("click", function () {
    modal.style.display = "none";
});

window.addEventListener("click", function (event) {
    if (event.target == modal) {
        modal.style.display = "none"; 
    }
});



