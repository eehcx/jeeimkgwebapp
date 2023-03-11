// Your web app's Firebase configuration
var firebaseConfig = {
  apiKey: "AIzaSyBXEiXDLhTkwYUCVD4oANFZeMtzqEoPLls",
  authDomain: "jeeimkg-5705b.firebaseapp.com",
  databaseURL: "https://jeeimkg-5705b.firebaseio.com",
  projectId: "jeeimkg-5705b",
  storageBucket: "jeeimkg-5705b.appspot.com",
  messagingSenderId: "192952472904",
  appId: "jeeimkg-5705b",
  measurementId: "352373982",
};

firebase.initializeApp(firebaseConfig);

// Manejador de eventos para el formulario de inicio de sesión
document.getElementById('login-form').addEventListener('submit', function(event) {
  event.preventDefault();

  const form = document.getElementById('login-form');
  const formData = new FormData(form);

  const email = formData.get('email');
  const password = formData.get('password');
  const firebaseToken = formData.get('firebase_token');

  // Validamos que el correo electrónico, la contraseña y el token de Firebase no estén vacíos
  if (!email || !password || !firebaseToken) {
    console.error('Correo electrónico, contraseña y token de Firebase son obligatorios');
    return;
  }

  // Enviamos la información del formulario al servidor usando AJAX
  const xhr = new XMLHttpRequest();
  xhr.open('POST', form.action, true);
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      // Si la autenticación es exitosa, redireccionamos al usuario
      window.location.href = '/adminsystem/';
    } else if (xhr.readyState === 4 && xhr.status === 401) {
      console.error('Credenciales inválidas');
    }
  };
  xhr.send('email=' + encodeURIComponent(email) + '&password=' + encodeURIComponent(password) + '&firebase_token=' + encodeURIComponent(firebaseToken));
});






