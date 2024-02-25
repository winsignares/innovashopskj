const usuarioPorDefecto = "keiler";
const contrasenaPorDefecto = "123456";

function verificarAdministrador() {

    const rolSeleccionado = document.getElementById("rol").value;
  
    const usuario = document.getElementById("usuario").value;
    const contrasena = document.getElementById("contrasena").value;


    if (rolSeleccionado === "administrador") {
        if (usuario === usuarioPorDefecto && contrasena === contrasenaPorDefecto) {
            alert("¡Bienvenido administrador!");
            window.open("Administradores.html", "_blank");
          } else {
            alert("Usuario o contraseña incorrectos.");
          }
    } else {
      alert("El acceso solo está permitido para administradores.");
    }
  }