document.querySelectorAll(".abrir-modal").forEach(function (boton) {
    boton.addEventListener("click", function () {
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
