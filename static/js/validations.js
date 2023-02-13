function validateForm() {
    const emailInput = document.getElementById("email-input");
    const emailRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;

    emailInput.addEventListener("input", function(event) {
        if (!emailRegex.test(event.target.value)) {
        emailInput.setCustomValidity("Por favor, ingresa un correo electrónico válido");
        } else {
        emailInput.setCustomValidity("");
        }
    });
}