import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Inicializar Firebase
cred = credentials.Certificate("jeeimkgServiceKey.json")
firebase_admin.initialize_app(cred, {
    'projectId': 'jeeimkg-5705b',
})

# Crear una instancia del cliente Firestore
db = firestore.client()

# Exportar el cliente Firestore
def get_firestore_client():
    return db
