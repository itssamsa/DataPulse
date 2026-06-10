var usuarios = [
  { usuario: "admin", contrasena: "1234" },
  { usuario: "juan", contrasena: "abcd" }
];

function iniciarSesion() {
  var usuario = document.getElementById("usuario").value;
  var contrasena = document.getElementById("contrasena").value;
  var error = document.getElementById("mensaje-error");

  if (usuario === "" || contrasena === "") {
    error.textContent = "Por favor completa todos los campos.";
    error.style.display = "block";
    return;
  }

  var encontrado = false;

  for (var i = 0; i < usuarios.length; i++) {
    if (usuarios[i].usuario === usuario && usuarios[i].contrasena === contrasena) {
      encontrado = true;
      break;
    }
  }

  if (encontrado) {
    error.style.display = "none";
    window.location.href = "Dashboard.html";
  } else {
    error.textContent = "Usuario o contraseña incorrectos.";
    error.style.display = "block";
  }
}

document.addEventListener("keydown", function(evento) {
  if (evento.key === "Enter") {
    iniciarSesion();
  }
});