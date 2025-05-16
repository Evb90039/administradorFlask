"""Configuración base (puedes expandir esto según tus necesidades)."""

from .firebase import db

class Config:
    """Configuración de la aplicación."""
    DEBUG = True
    SECRET_KEY = 'supersecreto'
