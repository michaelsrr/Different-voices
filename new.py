import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

def preprocess_audio(filepath, label):
    # Cargar la grabación
    y, sr = librosa.load(filepath)

    # Realizar algún tipo de preprocesamiento, por ejemplo, extraer el espectrograma
    spectrogram = librosa.feature.melspectrogram(y=y, sr=sr)
    
    return spectrogram, label

# Directorios donde se encuentran las grabaciones
directories = {
    "lento_bajo": "C:/Users/Michael/Desktop/Tono-Ritmo/audios/lento_bajo",
    "medio_medio": "C:/Users/Michael/Desktop/Tono-Ritmo/audios/medio_medio",
    "rapido_alto": "C:/Users/Michael/Desktop/Tono-Ritmo/audios/rapido_alto",
}

# Lista para almacenar las grabaciones y las etiquetas correspondientes
data = []
labels = []

# Iterar sobre los directorios y las grabaciones y procesar cada una
for label, directory in directories.items():
    for i in range(408):
        filename = f"{label}_{i}.wav"
        filepath = os.path.join(directory, f"{label}_{i}.wav").replace("\\", "/")

        # Preprocesar la grabación
        spectrogram, emotion_label = preprocess_audio(filepath, label)

        # Añadir los datos preprocesados y la etiqueta a las listas
        data.append(spectrogram)
        labels.append(emotion_label)

# Convertir las listas a matrices numpy
data = np.array(data)
labels = np.array(labels)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# Visualizar un ejemplo de espectrograma
librosa.display.specshow(librosa.power_to_db(data[0], ref=np.max), y_axis='mel', x_axis='time')
plt.colorbar(format='%+2.0f dB')
plt.show()
