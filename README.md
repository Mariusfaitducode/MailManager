# MailManager

Application pour gérer ses e-mails. Le principe est le suivant, l'algorithme va parcourir la boîte de réception et regroupé tous les mails provenant du même envoyeur.
Ainsi vous récupérez une liste classé par ordre décroissant de la quantité de mail envoyés par adresse mail. Les adresses qui ressortent le plus sont toujours les adresses de spam ou de notifications. Vous avez ainsi accès à un bouton supprimer permettant de nettoyer tous les mails venant de la même adresse en une seule fois.

Très pratique pour faire un nettoyage de sa boîte mail occasionelle.

Réalisé en python avec les librairies imaplib et customtkinter. 
Disponible pour l'instant aux adresses gmail, pour se connecter il faut renseigner son mot de passe d'application, facilement retrouvable sur son compte google.
