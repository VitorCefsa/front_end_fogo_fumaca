// Função para carregar o modelo e iniciar o vídeo
async function startVideo() {
    const video = document.getElementById('video');

    // Solicitar permissão para acessar a webcam
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(function (stream) {
        video.srcObject = stream;
        console.log("Webcam funcionando");
      })
      .catch(function (err) {
        console.error("Erro ao acessar a webcam: " + err);
      });

    // Tente carregar o modelo Tiny Face Detector do diretório /models
    try {
        console.log("Carregando modelo Tiny Face Detector...");
        await faceapi.nets.tinyFaceDetector.loadFromUri('/models');
        console.log("Modelo Tiny Face Detector carregado com sucesso!");
    } catch (error) {
        console.error("Erro ao carregar o modelo:", error);
    }

    // Iniciar a detecção de faces quando o vídeo for reproduzido
    video.addEventListener('play', () => {
      const canvas = faceapi.createCanvasFromMedia(video);
      document.body.append(canvas);
      const displaySize = { width: video.width, height: video.height };
      faceapi.matchDimensions(canvas, displaySize);

      setInterval(async () => {
        const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions());
        const resizedDetections = faceapi.resizeResults(detections, displaySize);
        canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height);
        faceapi.draw.drawDetections(canvas, resizedDetections);
      }, 100);
    });
}

// Iniciar o processo de vídeo e detecção ao carregar a página
window.onload = function () {
  startVideo();
};
