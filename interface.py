
import tkinter as tk
from tkinter import ttk

import customtkinter as ctk


class Interface(ctk.CTk):

    def __init__(self, mail_manager):
        super().__init__()

        self.mail_manager = mail_manager

        self.title("Mail Manager")
        

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        
        self.show_connexion_frame(user=mail_manager.mail_user, password=mail_manager.mail_password)


    def show_connexion_frame(self, user, password):

        self.geometry("350x150")

        self.rowconfigure(0, weight=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self.email_label = ctk.CTkLabel(self, text="Adresse Email:")
        self.email_label.grid(column=0, row=1, sticky=tk.W, padx=16, pady=6)

        self.email_entry = ctk.CTkEntry(self)
        self.email_entry.grid(column=1, row=1, sticky=tk.EW, padx=16, pady=6)
        self.email_entry.insert(0, user)

        self.password_label = ctk.CTkLabel(self, text="Mot de Passe:")
        self.password_label.grid(column=0, row=2, sticky=tk.W, padx=16, pady=6)

        self.password_entry = ctk.CTkEntry(self, show="*")
        self.password_entry.grid(column=1, row=2, sticky=tk.EW, padx=16, pady=6)
        self.password_entry.insert(0, password)

        self.login_button = ctk.CTkButton(self, text="Se Connecter", command=self.on_login_clicked)
        self.login_button.grid(column=0, row=3, columnspan=2, pady=16)


    def on_login_clicked(self):
        print("Login button clicked")
        mail_user = self.email_entry.get()
        mail_password = self.password_entry.get()
        self.mail_manager.login(mail_user, mail_password)

        self.show_action_frame()


    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()


    def show_action_frame(self):
        # Supprimer les widgets existants
        self.clear_widgets()

        self.geometry("350x150")

        # Widgets pour la page principale
        main_label = ctk.CTkLabel(self, text="Vous êtes connecté!")
        main_label.grid(row=0, columnspan=2, pady=10)

        self.count_label = ctk.CTkLabel(self, text="Nombres de mails à analyser:")
        self.count_label.grid(column=0, row=1, padx=(16, 0), pady=20)

        # Champ pour le nombre de mails à analyser
        self.mail_count_entry = ctk.CTkEntry(self)
        self.mail_count_entry.grid(column=1, row=1, pady=20)
        self.mail_count_entry.insert(0, "50")

        validate_command = self.register(self.on_validate_entry), '%P'
        self.mail_count_entry.configure(validate='key', validatecommand=validate_command)

        # Bouton Analyse
        analyse_button = ctk.CTkButton(self, text="Analyse", command=self.on_analyse_clicked, fg_color="#4CAF50")  # Vert
        analyse_button.grid(column=0, row=2, pady=10)

        # Bouton Déconnexion
        self.logout_button = ctk.CTkButton(self, text="Déconnexion", command=self.on_logout_clicked, fg_color="#F44336")  # Rouge
        self.logout_button.grid(column=1, row=2, pady=10)


        
    def on_validate_entry(P):
        return P.isdigit() or P == ""

    def on_analyse_clicked(self):
        # Récupérez le nombre de mails à analyser et lancez l'analyse
        mail_count = self.mail_count_entry.get()
        print(f"Analyse de {mail_count} mails...")

        messages = self.mail_manager.get_mailbox()

        print(f"Analyse de {len(messages)} mails terminée!")

        self.clear_widgets()
        self.show_analyse_frame(messages=messages)


    def on_logout_clicked(self):
        
        self.mail_manager.logout()
        self.clear_widgets()
        self.create_connexion_widgets(user=self.mail_manager.mail_user, password=self.mail_manager.mail_password)


    def show_analyse_frame(self, messages):
        
        # Création du tableau d'adresses mail
        self.tree = ttk.Treeview(self, columns=("Email"), show="headings")
        self.tree.heading("Email", text="Adresse Email")
        self.tree.column("Email", anchor=tk.CENTER)

        # Ajout des barres de défilement
        vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(self, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        vsb.pack(side="right", fill="y")
        hsb.pack(side="bottom", fill="x")
        self.tree.pack(side="top", fill="both", expand=True)

        # Bouton pour simuler l'ajout d'adresses mail
        self.load_button = ctk.CTkButton(self, text="Charger les Emails", command=self.load_emails)
        self.load_button.pack(pady=10)

        # Bouton de suppression
        self.delete_button = ctk.CTkButton(self, text="Supprimer l'Email", command=self.delete_email)
        self.delete_button.pack(pady=10)

    def load_emails(self):
        # Simuler le chargement des emails
        emails = ["user1@example.com", "user2@example.com", "user3@example.com"]
        for email in emails:
            self.tree.insert("", tk.END, values=(email,))

    def delete_email(self):
        selected_item = self.tree.selection()[0]  # Obtenir l'item sélectionné
        self.tree.delete(selected_item) 

    




