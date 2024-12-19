import tkinter as tk
from tkinter import ttk

# Création de la fenêtre principale
root = tk.Tk()
root.title("UEFA Champions League")
root.geometry("800x600")
root.configure(bg="white")

# Frame principale centrée
main_frame = tk.Frame(root, bg="white")
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Titre
title = tk.Label(main_frame, text="UEFA Champions League", font=("Arial", 16, "bold"), bg="white")
title.pack(pady=20)

# Style pour les frames des matchs
style = ttk.Style()
style.configure("Match.TFrame", background="white", relief="solid")

# Données des matchs
matches = [
    ("Milan AC", "MI", "14.02.24"),
    ("Athletico", "AT", "19.02.24"),
    ("Bâle", "BL", "24.02.24"),
    ("PSG", "PSG", "04.03.24"),
    ("Benfica", "BF", "05.03.24"),
    ("Porto FC", "PT", "12.03.24")
]

# Création des frames pour chaque match
for team, code, date in matches:
    match_frame = ttk.Frame(main_frame, style="Match.TFrame", padding=10)
    match_frame.pack(fill="x", padx=20, pady=5)

    # Configuration des colonnes pour centrer
    match_frame.grid_columnconfigure(2, weight=1)

    # Logo équipe gauche
    team_logo = tk.Canvas(match_frame, width=30, height=30, bg="white", highlightthickness=0)
    team_logo.create_oval(5, 5, 25, 25, fill="yellow")
    team_logo.grid(row=0, column=0, padx=5)

    # Nom équipe
    team_name = tk.Label(match_frame, text=team, bg="white")
    team_name.grid(row=0, column=1, padx=10)

    # frame augmantant la taille des tuiles
    vs_frame = tk.Frame(match_frame, bg="white")
    vs_frame.grid(row=0, column=2, padx=200)

    vs_label = tk.Label(vs_frame, text="", bg="white")
    vs_label.pack()
    date_label = tk.Label(vs_frame, text=date, bg="white")
    date_label.place(x=10,y=0)

    # Milan AC
    milan_name = tk.Label(match_frame, text="Milan AC", bg="white")
    milan_name.grid(row=0, column=3, padx=10)

    # Logo Milan
    milan_logo = tk.Canvas(match_frame, width=30, height=30, bg="white", highlightthickness=0)
    milan_logo.create_oval(5, 5, 25, 25, fill="yellow")
    milan_logo.grid(row=0, column=4, padx=5)

    def btnActions1():
        root = tk.Tk()
        root.title("UEFA Champions League / Milan AC VS Milan AC")
        root.geometry("800x600")
        root.configure(bg="white")

        # En-tête avec les équipes et la date
        header_frame = tk.Frame(root)
        header_frame.pack(pady=10)

        tk.Label(header_frame, text="MI", bg="yellow").pack(side=tk.LEFT, padx=10)
        tk.Label(header_frame, text="24.06.20").pack(side=tk.LEFT, padx=50)
        tk.Label(header_frame, text="MI", bg="yellow").pack(side=tk.LEFT, padx=10)

        # Contenu principal
        main_frame = tk.Frame(root, relief=tk.GROOVE, borderwidth=2)
        main_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Définition des sections et leurs éléments
        sections = {
            "Général": ["possession de balle: ", "tir au but: ", "duel gagné: ", "foules commises: "],
            "attaque": ["total tirs: ", "tirs au but: ", "corners: "],
            "défense": ["désarmer: "],
            "distribution": ["total passes: ", "précisions des passes: "],
            "discipline": ["foules commises: ", "cartons jaunes: ", "cartons rouges: "]
        }

        # Création des sections
        for title, items in sections.items():
            section_frame = tk.LabelFrame(main_frame, text=title)
            section_frame.pack(padx=5, pady=5, fill=tk.X)

            for item in items:
                tk.Label(section_frame, text=item).pack(anchor=tk.W, padx=5)

        root.mainloop()

    def btnActions2():
        root = tk.Tk()
        root.title("UEFA Champions League / Milan AC VS Milan AC")
        root.geometry("800x600")
        root.configure(bg="white")

        # En-tête avec les équipes et la date
        header_frame = tk.Frame(root)
        header_frame.pack(pady=10)

        tk.Label(header_frame, text="ATH", bg="yellow").pack(side=tk.LEFT, padx=10)
        tk.Label(header_frame, text="24.06.20").pack(side=tk.LEFT, padx=50)
        tk.Label(header_frame, text="MI", bg="yellow").pack(side=tk.LEFT, padx=10)

        # Contenu principal
        main_frame = tk.Frame(root, relief=tk.GROOVE, borderwidth=2)
        main_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Définition des sections et leurs éléments
        sections = {
            "Général": ["possession de balle: ", "tir au but: ", "duel gagné: ", "foules commises: "],
            "attaque": ["total tirs: ", "tirs au but: ", "corners: "],
            "défense": ["désarmer: "],
            "distribution": ["total passes: ", "précisions des passes: "],
            "discipline": ["foules commises: ", "cartons jaunes: ", "cartons rouges: "]
        }

        # Création des sections
        for title, items in sections.items():
            section_frame = tk.LabelFrame(main_frame, text=title)
            section_frame.pack(padx=5, pady=5, fill=tk.X)

            for item in items:
                tk.Label(section_frame, text=item).pack(anchor=tk.W, padx=5)

        root.mainloop()

    def btnActions3():
        root = tk.Tk()
        root.title("UEFA Champions League / Milan AC VS Milan AC")
        root.geometry("800x600")
        root.configure(bg="white")

        # En-tête avec les équipes et la date
        header_frame = tk.Frame(root)
        header_frame.pack(pady=10)

        tk.Label(header_frame, text="BL", bg="yellow").pack(side=tk.LEFT, padx=10)
        tk.Label(header_frame, text="24.06.20").pack(side=tk.LEFT, padx=50)
        tk.Label(header_frame, text="MI", bg="yellow").pack(side=tk.LEFT, padx=10)

        # Contenu principal
        main_frame = tk.Frame(root, relief=tk.GROOVE, borderwidth=2)
        main_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Définition des sections et leurs éléments
        sections = {
            "Général": ["possession de balle: ", "tir au but: ", "duel gagné: ", "foules commises: "],
            "attaque": ["total tirs: ", "tirs au but: ", "corners: "],
            "défense": ["désarmer: "],
            "distribution": ["total passes: ", "précisions des passes: "],
            "discipline": ["foules commises: ", "cartons jaunes: ", "cartons rouges: "]
        }

        # Création des sections
        for title, items in sections.items():
            section_frame = tk.LabelFrame(main_frame, text=title)
            section_frame.pack(padx=5, pady=5, fill=tk.X)

            for item in items:
                tk.Label(section_frame, text=item).pack(anchor=tk.W, padx=5)

        root.mainloop()

    def btnActions4():
        root = tk.Tk()
        root.title("UEFA Champions League / Milan AC VS Milan AC")
        root.geometry("800x600")
        root.configure(bg="white")

        # En-tête avec les équipes et la date
        header_frame = tk.Frame(root)
        header_frame.pack(pady=10)

        tk.Label(header_frame, text="PSG", bg="yellow").pack(side=tk.LEFT, padx=10)
        tk.Label(header_frame, text="24.06.20").pack(side=tk.LEFT, padx=50)
        tk.Label(header_frame, text="MI", bg="yellow").pack(side=tk.LEFT, padx=10)

        # Contenu principal
        main_frame = tk.Frame(root, relief=tk.GROOVE, borderwidth=2)
        main_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Définition des sections et leurs éléments
        sections = {
            "Général": ["possession de balle: ", "tir au but: ", "duel gagné: ", "foules commises: "],
            "attaque": ["total tirs: ", "tirs au but: ", "corners: "],
            "défense": ["désarmer: "],
            "distribution": ["total passes: ", "précisions des passes: "],
            "discipline": ["foules commises: ", "cartons jaunes: ", "cartons rouges: "]
        }

        # Création des sections
        for title, items in sections.items():
            section_frame = tk.LabelFrame(main_frame, text=title)
            section_frame.pack(padx=5, pady=5, fill=tk.X)

            for item in items:
                tk.Label(section_frame, text=item).pack(anchor=tk.W, padx=5)

        root.mainloop()

    def btnActions5():
        root = tk.Tk()
        root.title("UEFA Champions League / Milan AC VS Milan AC")
        root.geometry("800x600")
        root.configure(bg="white")

        # En-tête avec les équipes et la date
        header_frame = tk.Frame(root)
        header_frame.pack(pady=10)

        tk.Label(header_frame, text="BF", bg="yellow").pack(side=tk.LEFT, padx=10)
        tk.Label(header_frame, text="24.06.20").pack(side=tk.LEFT, padx=50)
        tk.Label(header_frame, text="MI", bg="yellow").pack(side=tk.LEFT, padx=10)

        # Contenu principal
        main_frame = tk.Frame(root, relief=tk.GROOVE, borderwidth=2)
        main_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Définition des sections et leurs éléments
        sections = {
            "Général": ["possession de balle: ", "tir au but: ", "duel gagné: ", "foules commises: "],
            "attaque": ["total tirs: ", "tirs au but: ", "corners: "],
            "défense": ["désarmer: "],
            "distribution": ["total passes: ", "précisions des passes: "],
            "discipline": ["foules commises: ", "cartons jaunes: ", "cartons rouges: "]
        }

        # Création des sections
        for title, items in sections.items():
            section_frame = tk.LabelFrame(main_frame, text=title)
            section_frame.pack(padx=5, pady=5, fill=tk.X)

            for item in items:
                tk.Label(section_frame, text=item).pack(anchor=tk.W, padx=5)

        root.mainloop()

    def btnActions6():
        root = tk.Tk()
        root.title("UEFA Champions League / Milan AC VS Milan AC")
        root.geometry("800x600")
        root.configure(bg="white")

        # En-tête avec les équipes et la date
        header_frame = tk.Frame(root)
        header_frame.pack(pady=10)

        tk.Label(header_frame, text="PT", bg="yellow").pack(side=tk.LEFT, padx=10)
        tk.Label(header_frame, text="24.06.20").pack(side=tk.LEFT, padx=50)
        tk.Label(header_frame, text="MI", bg="yellow").pack(side=tk.LEFT, padx=10)

        # Contenu principal
        main_frame = tk.Frame(root, relief=tk.GROOVE, borderwidth=2)
        main_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Définition des sections et leurs éléments
        sections = {
            "Général": ["possession de balle: ", "tir au but: ", "duel gagné: ", "foules commises: "],
            "attaque": ["total tirs: ", "tirs au but: ", "corners: "],
            "défense": ["désarmer: "],
            "distribution": ["total passes: ", "précisions des passes: "],
            "discipline": ["foules commises: ", "cartons jaunes: ", "cartons rouges: "]
        }

        # Création des sections
        for title, items in sections.items():
            section_frame = tk.LabelFrame(main_frame, text=title)
            section_frame.pack(padx=5, pady=5, fill=tk.X)

            for item in items:
                tk.Label(section_frame, text=item).pack(anchor=tk.W, padx=5)

        root.mainloop()

    #Boutons dans l'ordre
    bouton1 = tk.Button(root, text="VS", width=2, height=1, command=btnActions1)
    bouton2 = tk.Button(root, text="VS", width=2, height=1, command=btnActions2)
    bouton3 = tk.Button(root, text="VS", width=2, height=1, command=btnActions3)
    bouton4 = tk.Button(root, text="VS", width=2, height=1, command=btnActions4)
    bouton5 = tk.Button(root, text="VS", width=2, height=1, command=btnActions5)
    bouton6 = tk.Button(root, text="VS", width=2, height=1, command=btnActions6)

    bouton1.place(x=390,y=170)
    bouton2.place(x=390,y=230)
    bouton3.place(x=390,y=290)
    bouton4.place(x=390, y=350)
    bouton5.place(x=390,y=410)
    bouton6.place(x=390,y=470)

# Lancement de la boucle principalee
root.mainloop()