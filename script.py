import speech_recognition as sr
import numpy as np
import os
import math

# Créer un objet Recognizer
r = sr.Recognizer()
pi = 3.1416

# Ouvrir le flux audio à partir du micro
with sr.Microphone() as source:
    print("Parlez maintenant...")
    # Écouter le discours et le stocker dans la variable audio
    audio = r.listen(source)

try:
    # Utiliser Google Speech Recognition pour transcrire le discours en texte
    texte = r.recognize_google(audio, language='fr-FR')
    print("Vous avez dit : " + texte)
    for i in range(len(texte)):
        if texte[i] == "x":
            texte = texte[:i] + "*" + texte[i+1:]

    # Évaluer la réponse mathématique donnée à l'oral
    result = str(eval(texte))

    # Afficher le résultat
    print("Le résultat est : " + result)

except sr.UnknownValueError:
    print("Impossible de comprendre l'audio")
except sr.RequestError as e:
    print("Erreur lors de la requête à Google Speech Recognition; {0}".format(e))
