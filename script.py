import speech_recognition as sr
import openai
import os

openai.organization = "org-HPvNNcKGWKq4IiEv6ucQSwsC"
openai.api_key = "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"
openai.Model.list()

# Créer un objet Recognizer
r = sr.Recognizer()

# Ouvrir le flux audio à partir du micro
with sr.Microphone() as source:
    print("Parlez maintenant...")
    # Écouter le discours et le stocker dans la variable audio
    audio = r.listen(source)

try:
    # Utiliser Google Speech Recognition pour transcrire le discours en texte
    texte = r.recognize_google(audio, language='fr-FR')
    print("Vous avez dit : " + texte)

    # Utiliser l'API OpenAI GPT-3 pour résoudre le problème donné à l'oral
    completions = openai.Completion.create(
        engine="davinci", prompt=texte+"?", max_tokens=100
    )

    # Afficher la réponse générée par l'API OpenAI GPT-3
    print(completions.choices[0].text)

except sr.UnknownValueError:
    print("Impossible de comprendre l'audio")
except sr.RequestError as e:
    print("Erreur lors de la requête à Google Speech Recognition; {0}".format(e))
