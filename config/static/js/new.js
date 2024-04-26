
document.addEventListener("DOMContentLoaded", () => {

    const botonCerrarSesion = document.querySelector("#cerrar-sesion");
  
    function salir() {
      localStorage.clear();
      window.location.href = "/loginad";
      history.replaceState({}, "", "/loginad");
    }
  
    // Agregar evento de clic al botón de cerrar sesión
    if (botonCerrarSesion) {
      botonCerrarSesion.addEventListener("click", salir);  // Asignar el evento de salida
  };
});
  