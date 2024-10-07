import cv2

class VideoCamera:
    def __init__(self):
        # Inicializa a câmera
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        # Libera o recurso da câmera
        self.video.release()

    def get_frame(self):
        # Captura o frame da câmera e o converte para bytes
        success, image = self.video.read()
        if success:
            ret, jpeg = cv2.imencode('.jpg', image)
            return jpeg.tobytes()

# Função que gera os frames continuamente
def gen_frames():
    camera = cv2.VideoCapture(0)  # Inicializa a câmera
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
