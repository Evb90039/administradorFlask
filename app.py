from flask import Flask
from routes.guardar import guardar_bp

app = Flask(__name__)

# Registrar blueprints
app.register_blueprint(guardar_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

