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

// Inicializar Firebase
firebase.initializeApp(firebaseConfig);

// Obtener el token de sesión del usuario (guardado en una cookie)
const sessionCookie = getCookie('session');

// Autenticar al usuario con el token de sesión
firebase.auth().signInWithCustomToken(sessionCookie)
  .then((userCredential) => {
    // El usuario ha sido autenticado exitosamente
    console.log('Usuario autenticado:', userCredential.user);
  })
  .catch((error) => {
    // Manejar cualquier error que haya ocurrido durante la autenticación
    console.error('Error de autenticación:', error);
  });

// Función para leer el valor de una cookie por su nombre
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookie
}