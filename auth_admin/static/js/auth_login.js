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
  
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);



// Leer el valor de la cookie 'session'
var token = getCookie('session');

// Autenticar al usuario con el token personalizado
firebase.auth().signInWithCustomToken(token)
  .then((userCredential) => {
    // El usuario ha sido autenticado exitosamente
  })
  .catch((error) => {
    // Manejar cualquier error que haya ocurrido durante la autenticación
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
  return cookieValue;
}