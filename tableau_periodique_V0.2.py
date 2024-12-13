import tkinter as tk
from tkinter import ttk

# Liste des éléments chimiques (symbole, nom, numéro atomique, masse atomique, catégorie)
elements = [
    (1, "H", "Hydrogène", 1.008, "Non-métal"),
    (2, "He", "Hélium", 4.0026, "Gaz noble"),
    (3, "Li", "Lithium", 6.94, "Métal alcalin"),
    (4, "Be", "Béryllium", 9.0122, "Métal alcalino-terreux"),
    (5, "B", "Bore", 10.81, "Métalloïde"),
    (6, "C", "Carbone", 12.011, "Non-métal"),
    (7, "N", "Azote", 14.007, "Non-métal"),
    (8, "O", "Oxygène", 15.999, "Non-métal"),
    (9, "F", "Fluor", 18.998, "Halogène"),
    (10, "Ne", "Néon", 20.180, "Gaz noble"),
    (11,"NA", "Sodium", 22.990, "Métal alcalin"),
    (12,"Mg", "Magnésium", 24.305, "Métal alcalino-terreux"),
    (13, "Al", "Aluminium", 26.982, "Métaux de post-transition" ),
    (14, "Si", "Silicium", 28.086, "MétalloÏdes"),
    (15, "P", "Phosphore", 30.974, "Non-métal"),
    (16, "S", "Soufre", 32.065, "Non-métal"),
    (17, "Cl", "Chlore", 35.453, "Non-métal"),
    (18, "Ar", "Argon", 35.453, "Non-métal"),
    (19, "K", "Potassium", 39.098, "Métal alcalin"),
    (20, "Ca", "Calcium", 40.078, "Métal alcalino-terreaux"),
    (21, "Sc", "Scandium", 44.956, "Métaux de post-transition"),
    (22, "Ti", "Titane", 47.867, "")

    # Vous pouvez continuer à ajouter les éléments ici
]

# Catégories et leurs couleurs correspondantes
category_colors = {
    "Non-métal": "#F0E68C",
    "Gaz noble": "#FFD700",
    "Métal alcalin": "#FFB6C1",
    "Métal alcalino-terreux": "#87CEFA",
    "Métalloïde": "#98FB98",
    "Halogène": "#FFA07A",
    "Métaux de post-transition" : "#99FFAA",
    
}

class PeriodicTableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tableau Périodique des Éléments")
        
        self.create_widgets()

    def create_widgets(self):
        """Créer les widgets de l'interface graphique."""
        # Création de la grille pour le tableau
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        for element in elements:
            atomic_number, symbol, name, atomic_mass, category = element
            color = category_colors.get(category, "#FFFFFF")

            # Créer un bouton pour chaque élément
            btn = tk.Button(
                frame,
                text=f"{symbol}\n{atomic_number}",
                bg=color,
                width=10,
                height=4,
                command=lambda e=element: self.show_element_details(e)
            )

            # Position dans la grille (simplifiée ici pour la démo)
            row = (atomic_number - 1) // 10
            col = (atomic_number - 1) % 10
            btn.grid(row=row, column=col, padx=2, pady=2)

        # Créer une zone d'affichage des détails
        self.details_label = ttk.Label(self.root, text="Sélectionnez un élément pour voir les détails.",
                                        anchor="center", background="white", relief="solid", padding=10)
        self.details_label.pack(fill="x", padx=10, pady=10)

    def show_element_details(self, element):
        """Afficher les détails d'un élément dans la zone de détails."""
        atomic_number, symbol, name, atomic_mass, category = element
        details = (
            f"Nom : {name}\n"
            f"Symbole : {symbol}\n"
            f"Numéro atomique : {atomic_number}\n"
            f"Masse atomique : {atomic_mass}\n"
            f"Catégorie : {category}"
        )
        self.details_label.config(text=details)

if __name__ == "__main__":
    root = tk.Tk()
    app = PeriodicTableApp(root)
    root.mainloop()
