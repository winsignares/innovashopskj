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
    window.location.href = "/";
    history.replaceState({}, "", "/");
  }

  const botonSalir = document.querySelector(".menu .enlace a[onclick='salir()']");
  if (botonSalir) {
    botonSalir.addEventListener('click', salir);
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
