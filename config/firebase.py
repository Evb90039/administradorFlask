"""Configuración e inicialización de Firebase."""
import os
import firebase_admin
from firebase_admin import credentials, firestore

# Cargar credenciales desde variables de entorno
cred = credentials.Certificate({
    "type": os.environ.get("type"),
    "project_id": os.environ.get("project_id"),
    "private_key_id": os.environ.get("private_key_id"),
    "private_key": os.environ.get("private_key").replace('\\n', '\n'),
    "client_email": os.environ.get("client_email"),
    "client_id": os.environ.get("client_id"),
    "auth_uri": os.environ.get("auth_uri"),
    "token_uri": os.environ.get("token_uri"),
    "auth_provider_x509_cert_url": os.environ.get("auth_provider_x509_cert_url"),
    "client_x509_cert_url": os.environ.get("client_x509_cert_url"),
    "universe_domain": os.environ.get("universe_domain"),
})

firebase_admin.initialize_app(cred)
db = firestore.client()
