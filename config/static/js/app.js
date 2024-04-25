document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.querySelector(".toggle");
  const menuDashboard = document.querySelector(".menu-dashboard");
  const iconoMenu = toggle.querySelector("i");
  const enlaces = document.querySelectorAll(".menu .enlace");
  const paginas = document.querySelectorAll(".pagina");

  function mostrarPagina(nombrePagina) {
    paginas.forEach(pagina => {
      pagina.style.display = 'none'; 
    });

    const paginaActiva = document.querySelector(`.pagina.${nombrePagina}`);
    if (paginaActiva) {
      paginaActiva.style.display = 'block';
    }
  }

  
  const hash = window.location.hash; 
  if (hash) {
    const nombrePagina = hash.substring(1); 
    mostrarPagina(nombrePagina); 
  }

  enlaces.forEach(enlace => {
    enlace.addEventListener("click", function() {
      const nombrePagina = this.getAttribute("data-pagina");
      mostrarPagina(nombrePagina); 
    });
  });

  function salir() {
    localStorage.clear(); 
    window.location.href = "/"; 
  }

  const botonSalir = document.querySelector(".menu .enlace a[onclick='salir()']");
  if (botonSalir) {
    botonSalir.addEventListener("click", salir);
  }

  toggle.addEventListener("click", () => {
    menuDashboard.classList.toggle("open"); 

    if (iconoMenu.classList.contains("bx-menu")) {
      iconoMenu.classList.replace("bx-menu", "bx-x");
    } else {
      iconoMenu.classList.replace("bx-x", "bx-menu");
    }
  });
});


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



