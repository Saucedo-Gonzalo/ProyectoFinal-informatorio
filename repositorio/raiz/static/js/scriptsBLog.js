function confirmarGuardarCambios() {
  const confirmado = confirm("¿Estás seguro de que deseas guardar los cambios?");
  if (confirmado) {
    document.getElementById("formulario").submit();
  } else {
    recargar();
}}

function recargar() {
  // Si el usuario cancela, restaurar los valores originales del formulario
  const form = document.getElementById("formulario");
  const inputs = form.getElementsByTagName("input");
  const textareas = form.getElementsByTagName("textarea");
  
  // Guardar los valores actuales de los inputs
  const inputValues = {};
  for (let i = 0; i < inputs.length; i++) {
    const input = inputs[i];
    inputValues[input.id] = input.value;
  }
  
  // Guardar los valores actuales de los textareas
  const textareaValues = {};
  for (let i = 0; i < textareas.length; i++) {
    const textarea = textareas[i];
    textareaValues[textarea.id] = textarea.value;
  }
  
  // Restablecer los valores originales de los inputs
  for (let i = 0; i < inputs.length; i++) {
    const input = inputs[i];
    input.value = inputValues[input.id];
  }
  
  // Restablecer los valores originales de los textareas
  for (let i = 0; i < textareas.length; i++) {
    const textarea = textareas[i];
    textarea.value = textareaValues[textarea.id];
  }
}

function cancelarEdicion() {
document.getElementById("formulario").reset(); // restablecer el formulario a su estado original
}

function validarFormulario() {
  // obtengo los valores ingresados por el usuario
  const titulo = document.getElementById("id_titulo").value;
  const cuerpo = document.getElementById("id_cuerpo").value;

  // realiza la validación previa
  let isValid = true;

  if (titulo.length < 3) {
      alert("El título debe tener al menos 3 caracteres.");

      isValid = false;
      
  }

  if (cuerpo.length < 20) {
      alert("El cuerpo debe tener al menos 20 caracteres.");
      isValid = false;
      
  }

  if (!imagen.files || !imagen.files.length) {
    alert("Debes seleccionar una imagen.");

    isValid = false;
    
}

if (isValid) {
  const confirmado = confirm("¿Estás seguro de que deseas guardar los cambios?");
  if (confirmado) {
    document.getElementById("formulario").submit();
  } else {
    recargar();
  }
}
}

