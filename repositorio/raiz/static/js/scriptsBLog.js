function confirmarGuardarCambios() {
  const confirmado = confirm("¿Estás seguro de que deseas guardar los cambios?");
  if (confirmado) {
    document.getElementById("formulario").submit();
  } else {
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
}
  

function cancelarEdicion() {
document.getElementById("formulario").reset(); // Restablecer el formulario a su estado original
}