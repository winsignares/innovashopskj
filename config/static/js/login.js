window.addEventListener("pageshow", function(event) {
  if (event.persisted) { // Esto indica que la página se cargó desde caché
      location.reload(); // Recarga la página
  }
});