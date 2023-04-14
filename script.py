import speech_recognition as sr
import numpy as np
import os
import math
import tkinter as tk

# Créer un objet Recognizer
r = sr.Recognizer()

#def pi
pi = 3.1416

# Permet de gerer les options non prises en compte par la fonction eval
option = 0


def main(option):
    # Ouvrir le flux audio à partir du micro
    with sr.Microphone() as source:
        print("Parlez maintenant...")
        # Écouter le discours et le stocker dans la variable audio
        audio = r.listen(source)

    try:
        # Utiliser Google Speech Recognition pour transcrire le discours en texte
        texte = r.recognize_google(audio, language='fr-FR')

        # Gérer les options
        if texte.find("racine") != -1:
            option = 1
        if texte.find("%") != -1:
            option = 2

        # Afficher le texte transcrit
        print("Vous avez dit : " + texte)

        # Gérer les erreurs de reconnaissance entre x et *
        for i in range(len(texte)):
            if texte[i] == "x":
                texte=texte.replace("x", "*")

        # Gérer les erreurs de reconnaissance entre au carré et au cube
        texte=texte.replace("au carré", "**2")
        texte=texte.replace("au cube", "**3")

        # Évaluer la réponse mathématique donnée à l'oral
        if option == 0:
            result = str(eval(texte))
        elif option == 1:
            texte = texte.replace("racine de", "")
            result = math.sqrt(int(texte))
        else :
            diviseur = int((texte.split("de")[0]).replace(" %", ""))
            divisé = int(texte.split("de")[1])
            result=(diviseur/100)*divisé

        # Afficher le résultat dans la fenêtre
        result_label.config(text="Le résultat est : " + str(result))

    # Gérer les erreurs sur le micro
    except sr.UnknownValueError:
        print("Impossible de comprendre l'audio")
    except sr.RequestError as e:
        print("Erreur lors de la requête à Google Speech Recognition; {0}".format(e))

def get_input():
    global option
    option = 0
    main(option)

# Créer une fenêtre Tkinter
window = tk.Tk()
window.title("Calculatrice Vocale")
window.geometry("400x300")

# Ajouter une étiquette pour afficher le résultat
result_label = tk.Label(window, text="Le résultat sera affiché ici.")
result_label.pack()

# Ajouter un bouton pour déclencher l'enregistrement vocal
record_button = tk.Button(window, text="Enregistrer", command=get_input)
record_button.pack()

# Lancer la boucle d'affichage de la fenêtre
window.mainloop()