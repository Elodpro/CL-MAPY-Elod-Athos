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

    # VS et date (centré)
    vs_frame = tk.Frame(match_frame, bg="white")
    vs_frame.grid(row=0, column=2, padx=200)

    vs_label = tk.Label(vs_frame, text="VS", bg="white")
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

# Lancement de la boucle principalee
root.mainloop()