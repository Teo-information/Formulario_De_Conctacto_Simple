// Simulación de "API" local
const mensajesEnviados = [];

document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('contactForm');
  const confirmation = document.getElementById('confirmation');

  if (!form) return;

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    const nombre = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const mensaje = document.getElementById('message').value.trim();

    let valid = true;

    if (!nombre) valid = false;
    if (!email || !/^[\w-.]+@([\w-]+\.)+[\w-]{2,4}$/.test(email)) valid = false;
    if (!mensaje) valid = false;

    if (valid) {
      // Envío a "API" simulado con fetch
      fetch('http://localhost:3001/mensajes', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nombre, email, mensaje, fecha: new Date().toISOString() })
      })
      .then(() => {
        confirmation.classList.add('show');
        confirmation.classList.remove('hidden');
        form.reset();
        setTimeout(() => {
          confirmation.classList.remove('show');
          confirmation.classList.add('hidden');
        }, 3000);
      });
    } else {
      alert('Por favor, completa todos los campos correctamente.');
    }
  });
});