import tkinter as tk
from tkinter import messagebox, Canvas
import chempy
from chempy import balance_stoichiometry

class ChemicalReactionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cân Bằng Phản Ứng")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")
        
        self.label = tk.Label(root, text="Nhập chất phản ứng :", bg="#f0f0f0", font=("Arial", 12))
        self.label.pack(pady=5)
        
        self.reactants_entry = tk.Entry(root, width=50, font=("Arial", 12))
        self.reactants_entry.pack(pady=5)
        
        self.label2 = tk.Label(root, text="Nhập chất sản phẩm :", bg="#f0f0f0", font=("Arial", 12))
        self.label2.pack(pady=5)
        
        self.products_entry = tk.Entry(root, width=50, font=("Arial", 12))
        self.products_entry.pack(pady=5)
        
        self.balance_button = tk.Button(root, text="Cân bằng phương trình", command=self.balance_equation, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.balance_button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 14, "bold"), fg="#333")
        self.result_label.pack(pady=10)
        
        self.canvas = Canvas(root, width=500, height=150, bg="#ffffff")
        self.canvas.pack(pady=10)
    
    def balance_equation(self):
        reactants = self.reactants_entry.get().split('+')
        products = self.products_entry.get().split('+')
        try:
            balanced_eq = balance_stoichiometry(set(reactants), set(products))
            result_text = " + ".join(f"{v} {k}" for k, v in balanced_eq[0].items()) + " -> " + " + ".join(f"{v} {k}" for k, v in balanced_eq[1].items())
            self.result_label.config(text=result_text)
            self.draw_reaction(result_text)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể cân bằng phản ứng: {e}")
    
    def draw_reaction(self, reaction_text):
        self.canvas.delete("all")
        self.canvas.create_text(250, 75, text=reaction_text, font=("Arial", 14, "bold"), fill="#333", width=480)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChemicalReactionApp(root)
    root.mainloop()