import speech_recognition as sr
import numpy as np
import os
import math

# Créer un objet Recognizer
r = sr.Recognizer()
pi = 3.1416
option = 0
# Ouvrir le flux audio à partir du micro
with sr.Microphone() as source:
    print("Parlez maintenant...")
    # Écouter le discours et le stocker dans la variable audio
    audio = r.listen(source)

try:
    # Utiliser Google Speech Recognition pour transcrire le discours en texte
    texte = r.recognize_google(audio, language='fr-FR')
    if texte.find("racine") != -1:
        option = 1
    print("Vous avez dit : " + texte)
    for i in range(len(texte)):
        if texte[i] == "x":
            texte=texte.replace("x", "*")

    texte=texte.replace("au carré", "**2")
    texte=texte.replace("au cube", "**3")

    # Évaluer la réponse mathématique donnée à l'oral
    if option == 0:
        result = str(eval(texte))
    else : 
        texte = texte.replace("racine de", "")
        result = math.sqrt(int(texte))

    # Afficher le résultat
    print("Le résultat est : " + str(result))

except sr.UnknownValueError:
    print("Impossible de comprendre l'audio")
except sr.RequestError as e:
    print("Erreur lors de la requête à Google Speech Recognition; {0}".format(e))
