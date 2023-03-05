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

document.querySelector('#login-form').addEventListener('submit', function(event) {
  event.preventDefault();
  var email = document.querySelector('#email').value;
  var password = document.querySelector('#password').value;

  fetch('/login/', {
    method: 'POST',
    body: JSON.stringify({email: email, password: password}),
    headers: {'Content-Type': 'application/json'}
  })
  .then(function(response) {
    return response.json();
  })
  .then(function(data) {
    firebase.auth().signInWithCustomToken(data.token)
      .then(function(userCredential) {
        console.log('Usuario autenticado con éxito:', userCredential.user.email);
      })
      .catch(function(error) {
        console.error('Error al autenticar al usuario:', error);
      });
  })
  .catch(function(error) {
    console.error('Error al enviar los datos del formulario:', error);
  });
});