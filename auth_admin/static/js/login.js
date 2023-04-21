// Configurar Firebase con las credenciales de tu proyecto
firebase.initializeApp({
    apiKey: 'AIzaSyBXEiXDLhTkwYUCVD4oANFZeMtzqEoPLls',
    authDomain: 'jeeimkg-5705b.firebaseapp.com',
    projectId: 'jeeimkg-5705b'
  });
  
  // Definir la función de inicio de sesión
  function login(email, password) {
    // Hacer la solicitud a la API de login
    return fetch('https://restapi-jeeimkg.onrender.com/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        email: email,
        password: password
      })
    })
    .then(response => response.json())
    .then(data => {
      // Si la API devuelve un token, iniciar sesión en Firebase
      if (data.token) {
        return firebase.auth().signInWithCustomToken(data.token);
      }
      // Si la API no devuelve un token, devolver un error
      throw new Error(data.message);
    })
    .then(userCredential => {
      // Si la autenticación es exitosa, devolver el usuario
      return userCredential.user;
    });
  }
  