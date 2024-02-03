
import tkinter as tk
from tkinter import ttk

from tkinter import Canvas, Scrollbar, Frame
import customtkinter as ctk

from collections import OrderedDict


class Interface(ctk.CTk):

    def __init__(self, mail_manager):
        super().__init__()

        self.mail_manager = mail_manager

        self.title("Mail Manager")
        

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.show_connexion_frame(user=mail_manager.mail_user, password=mail_manager.mail_password)

        # self.show_analyse_frame(list=[])


    ### Page connexion

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


    ### Page action

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
        self.mail_count_entry.insert(0, 5)

        # Bouton Analyse
        analyse_button = ctk.CTkButton(self, text="Analyse", command=self.on_analyse_clicked, fg_color="#4CAF50")  # Vert
        analyse_button.grid(column=0, row=2, pady=10)

        # Bouton Déconnexion
        self.logout_button = ctk.CTkButton(self, text="Déconnexion", command=self.on_logout_clicked, fg_color="#F44336")  # Rouge
        self.logout_button.grid(column=1, row=2, pady=10)


    def on_analyse_clicked(self):
        # Récupérez le nombre de mails à analyser et lancez l'analyse
        mail_count = int(self.mail_count_entry.get())


        self.clear_widgets()

        self.progress_bar = ctk.CTkProgressBar(self)
        self.progress_bar.pack(pady=20)
        self.progress_bar.set(0)

        self.update()

        list = self.mail_manager.analyse(count=mail_count, interface=self)

        self.clear_widgets()
        self.show_analyse_frame(list=list)


    def on_logout_clicked(self):
        
        self.mail_manager.logout()
        self.clear_widgets()
        self.create_connexion_widgets(user=self.mail_manager.mail_user, password=self.mail_manager.mail_password)


    ### Page analyse

    def show_analyse_frame(self, list):

        self.geometry("500x500")

        self.canvas = Canvas(self, bg="#2B2B2B", highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        style = ttk.Style()
        style.theme_use("clam")

        # Configurer le style de la Scrollbar pour un thème sombre
        style.configure("Vertical.TScrollbar", background="#333333", troughcolor="#2B2B2B", bordercolor="#333333", arrowcolor="white")

        # Scrollbar verticale
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview, style="Vertical.TScrollbar")
        self.scrollbar.pack(side="right", fill="y")

        # Frame qui contiendra les widgets du tableau
        self.table_frame = Frame(self.canvas, bg="#2B2B2B")
        self.canvas.create_window((0, 0), window=self.table_frame, anchor="nw")

        self.table_frame.bind("<Configure>", self.on_frame_configure)
        # self.table_frame.bind("<MouseWheel>", self.on_mousewheel)


        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # self.canvas.bind("<MouseWheel>", self.on_mousewheel)
        self.canvas.bind_all("<MouseWheel>", lambda event: self.on_mousewheel(event))
        self.table_frame.bind("<Configure>", lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.populate_table(list)


    def populate_table(self, list):

        list = OrderedDict(sorted(list.items(), key=lambda item: len(item[1]), reverse=True))

        i=0
        for sender in list:  # Exemple avec 50 lignes
            i+=1
            ctk.CTkLabel(self.table_frame, text=sender, width=200, height=30, corner_radius=0).grid(row=i, column=0, sticky="ew", padx=10, pady=2)
            ctk.CTkLabel(self.table_frame, text=len(list[sender]), width=100, height=30, corner_radius=0).grid(row=i, column=1, sticky="ew", padx=10, pady=2)

            delete_button = ctk.CTkButton(self.table_frame, text="Supprimer", 
                          width=100, height=30, corner_radius=0)
            
            delete_button.grid(row=i, column=2, sticky="ew", padx=10, pady=2)

            delete_button.configure(command=lambda sender=sender, delete_button=delete_button: self.delete_row(list[sender], delete_button))


    def delete_row(self, mail_list, delete_button):

        print(mail_list)
        self.mail_manager.delete_mail_list(mail_list)

        delete_button.destroy()




    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/20)), "units")
    




