import os
import firebase_admin
from firebase_admin import credentials, firestore

# Cargar credenciales desde variables de entorno
cred = credentials.Certificate({
    "projectId": os.environ.get("FIREBASE_PROJECT_ID"),
    "private_key": os.environ.get("FIREBASE_PRIVATE_KEY").replace('\\n', '\n'),
    "client_email": os.environ.get("FIREBASE_CLIENT_EMAIL"),
})

firebase_admin.initialize_app(cred)
db = firestore.client() 