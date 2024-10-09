from app import create_app
from flask import send_from_directory

# Criar a aplicação Flask usando o padrão factory
app = create_app()

# Rota para servir os arquivos da pasta 'models'
@app.route('/models/<path:filename>')
def serve_models(filename):
    return send_from_directory('models', filename)

# Executar o servidor Flask
if __name__ == "__main__":
    app.run(debug=True)
