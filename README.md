# Projeto de Detecção de Fogo usando Flask e YOLOv5

Este projeto tem como objetivo detectar fogo em tempo de execução utilizando **YOLOv5** para processar vídeos da câmera do notebook. A aplicação é construída com **Flask** e utiliza **OpenCV** para capturar e exibir o vídeo ao vivo.

## Funcionalidades

- Exibe o feed de vídeo da câmera do notebook em tempo real.
- Utiliza o modelo YOLOv5 para detectar focos de incêndio.
- Desenha caixas delimitadoras nas áreas onde o fogo foi detectado.
- Interface web para visualizar o vídeo e as detecções diretamente no navegador.

## Pré-requisitos

Antes de rodar a aplicação, você precisará dos seguintes componentes:

- **Python 3.7 ou superior**
- **Flask**
- **OpenCV**
- **PyTorch**
- **YOLOv5** (modelo pré-treinado ou personalizado)

### Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/seu-usuario/deteccao-de-fogo-flask.git
    cd deteccao-de-fogo-flask
    ```

2. Crie um ambiente virtual e ative-o:

    ```bash
    python -m venv env
    source env/bin/activate  # Linux/MacOS
    .\env\Scripts\activate   # Windows
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Baixe e configure o **YOLOv5**:

    - Clone o repositório YOLOv5:

      ```bash
      git clone https://github.com/ultralytics/yolov5.git
      cd yolov5
      ```

    - Instale as dependências do YOLOv5:

      ```bash
      pip install -r requirements.txt
      ```

    - Coloque o arquivo de pesos treinado (`.pt`) no diretório apropriado (ou use o modelo pré-treinado).

## Como rodar a aplicação

1. Certifique-se de que você está no diretório raiz do projeto.
2. Inicie o servidor Flask:

    ```bash
    python run.py
    ```

3. Abra seu navegador e acesse a aplicação:

    ```
    http://127.0.0.1:5000/testar_modelo
    ```

Você verá o feed de vídeo da sua câmera, com as detecções de fogo feitas pelo modelo YOLOv5.

## Estrutura do Projeto

```plaintext
front_end_fogo_fumaca/
│
├── app/
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   └── testar_modelo.html
│   ├── static/
│   ├── __init__.py
│   ├── routes.py
├── yolov5/  # Repositório YOLOv5
│   ├── yolov5s.pt  # Modelo pré-treinado ou personalizado
├── run.py
├── requirements.txt
├── README.md
├── .gitignore
