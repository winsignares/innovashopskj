//Codigo del dashboard
document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.querySelector(".toggle");
  const menuDashboard = document.querySelector(".menu-dashboard");
  const iconoMenu = toggle.querySelector("i");
  const enlaces = document.querySelectorAll(".menu .enlace");
  const paginas = document.querySelectorAll(".pagina");

  enlaces.forEach(enlace => {
    enlace.addEventListener("click", function() {
      const nombrePagina = this.getAttribute("data-pagina");
      mostrarPagina(nombrePagina);
    });
  });


  function mostrarPagina(nombrePagina) {
    paginas.forEach(pagina => {
      pagina.style.display = 'none';
    });

    const paginaActiva = document.querySelector(`.pagina.${nombrePagina}`);
    if (paginaActiva) {
      paginaActiva.style.display = 'block';
    }
  }

  function salir() {
    localStorage.clear();
    history.replaceState({}, "", "/");
    window.location.href = "/";
  }

  function saliradmin() {
    localStorage.clear();
    history.replaceState({}, "", "/loginad");
    window.location.href = "/loginad";
  }

  const botonSalir = document.querySelector(".menu .enlace[onclick='salir()']");
  const botonSaliradmin = document.querySelector(".menu .enlace[onclick='saliradmin()']");
  if (botonSalir) {
    botonSalir.addEventListener('click', function(event) {
        event.stopPropagation(); 
        salir(); 
    });
  }
  if (botonSaliradmin) {
    botonSaliradmin.addEventListener('click', function(event) {
        event.stopPropagation(); 
        saliradmin(); 
    });
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
