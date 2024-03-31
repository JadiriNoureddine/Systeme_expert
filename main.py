import tkinter as tk
from tkinter import messagebox, simpledialog
from systeme_expert import SystemeExpert

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Système Expert")
        self.geometry("300x150")
        self.mode = None
        self.expert = SystemeExpert()
        self.create_widgets()

    def create_widgets(self):
        mode_label = tk.Label(self, text="Choisir le mode :")
        mode_label.pack()

        expert_button = tk.Button(self, text="Mode Expert", command=self.show_expert_mode)
        expert_button.pack(pady=5)

        user_button = tk.Button(self, text="Mode Utilisateur", command=self.show_user_mode)
        user_button.pack(pady=5)

    def show_expert_mode(self):
        self.mode = "Expert"
        self.clear_widgets()
        self.title("Mode Expert")
        
        add_button = tk.Button(self, text="Ajouter Règle", command=self.add_rule)
        add_button.pack(pady=5)

        modify_button = tk.Button(self, text="Modifier Règle", command=self.modify_rule)
        modify_button.pack(pady=5)

        delete_button = tk.Button(self, text="Supprimer Règle", command=self.delete_rule)
        delete_button.pack(pady=5)

        quit_button = tk.Button(self, text="Quitter", command=self.quit)
        quit_button.pack(pady=5)

    def show_user_mode(self):
        self.mode = "Utilisateur"
        self.clear_widgets()
        self.title("Mode Utilisateur")
        
        diagnose_button = tk.Button(self, text="Diagnostiquer une panne", command=self.diagnose)
        diagnose_button.pack(pady=5)

        quit_button = tk.Button(self, text="Quitter", command=self.quit)
        quit_button.pack(pady=5)

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

    def add_rule(self):
        symptomes = simpledialog.askstring("Ajouter Règle", "Symptômes observés (séparés par des virgules):")
        if symptomes is not None:
            panne = simpledialog.askstring("Ajouter Règle", "Panne associée:")
            if panne is not None:
                self.expert.ajouter_regle(symptomes.split(","), panne)
                messagebox.showinfo("Succès", "Règle ajoutée avec succès!")

    def modify_rule(self):
        symptomes = simpledialog.askstring("Modifier Règle", "Symptômes à modifier (séparés par des virgules):")
        if symptomes is not None:
            nouvelle_panne = simpledialog.askstring("Modifier Règle", "Nouvelle panne associée:")
            if nouvelle_panne is not None:
                self.expert.modifier_regle(symptomes.split(","), nouvelle_panne)
                messagebox.showinfo("Succès", "Règle modifiée avec succès!")

    def delete_rule(self):
        symptomes = simpledialog.askstring("Supprimer Règle", "Symptômes à supprimer (séparés par des virgules):")
        if symptomes is not None:
            self.expert.supprimer_regle(symptomes.split(","))
            messagebox.showinfo("Succès", "Règle supprimée avec succès!")

    def diagnose(self):
        symptomes = simpledialog.askstring("Diagnostiquer une panne", "Symptômes observés (séparés par des virgules):")
        if symptomes is not None:
            panne_diagnostiquee = self.expert.diagnostiquer_panne(symptomes.split(","))
            messagebox.showinfo("Pannes possibles", f"Pannes possibles : {panne_diagnostiquee}")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
