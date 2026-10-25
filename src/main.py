import tkinter as tk
from tkinter import ttk, messagebox
from generator import generate_password
from checker import check_password_strength


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("420x460")
        self.root.resizable(False, False)

        # Farben / Stil
        self.root.configure(bg="#1e1e2e")
        style = ttk.Style()
        style.theme_use("clam")

        # Variablen
        self.length_var = tk.IntVar(value=12)
        self.use_lower = tk.BooleanVar(value=True)
        self.use_upper = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=False)

        self.create_widgets()

    def create_widgets(self):
        # Überschrift
        title = tk.Label(
            self.root,
            text="Password Generator",
            font=("Segoe UI", 18, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        )
        title.pack(pady=(20, 15))

        # --- Länge ---
        length_frame = tk.Frame(self.root, bg="#1e1e2e")
        length_frame.pack(pady=10, padx=30, fill="x")

        tk.Label(
            length_frame,
            text="Länge:",
            font=("Segoe UI", 11),
            bg="#1e1e2e",
            fg="#cdd6f4"
        ).pack(side="left")

        self.length_label = tk.Label(
            length_frame,
            textvariable=self.length_var,
            font=("Segoe UI", 11, "bold"),
            bg="#1e1e2e",
            fg="#89b4fa",
            width=3
        )
        self.length_label.pack(side="right")

        self.slider = ttk.Scale(
            self.root,
            from_=1,
            to=20,
            orient="horizontal",
            variable=self.length_var,
            command=self.update_length_label
        )
        self.slider.pack(pady=5, padx=30, fill="x")

        # --- Checkboxes ---
        checks_frame = tk.Frame(self.root, bg="#1e1e2e")
        checks_frame.pack(pady=15)

        for text, var in [
            ("Kleinbuchstaben (a-z)", self.use_lower),
            ("Großbuchstaben (A-Z)", self.use_upper),
            ("Zahlen (0-9)", self.use_digits),
            ("Symbole (!@#$...)", self.use_symbols),
        ]:
            tk.Checkbutton(
                checks_frame,
                text=text,
                variable=var,
                font=("Segoe UI", 10),
                bg="#1e1e2e",
                fg="#cdd6f4",
                selectcolor="#313244",
                activebackground="#1e1e2e",
                activeforeground="#cdd6f4"
            ).pack(anchor="w", pady=2)

        # --- Generate Button ---
        generate_btn = tk.Button(
            self.root,
            text="Generate Password",
            font=("Segoe UI", 11, "bold"),
            bg="#89b4fa",
            fg="#1e1e2e",
            activebackground="#74c7ec",
            activeforeground="#1e1e2e",
            relief="flat",
            cursor="hand2",
            command=self.generate
        )
        generate_btn.pack(pady=15, ipadx=10, ipady=5)

        # --- Passwort-Anzeige + Copy-Button ---
        result_frame = tk.Frame(self.root, bg="#1e1e2e")
        result_frame.pack(pady=10, padx=30, fill="x")

        self.password_var = tk.StringVar(value="")

        self.password_entry = tk.Entry(
            result_frame,
            textvariable=self.password_var,
            font=("Consolas", 13),
            justify="center",
            bg="#313244",
            fg="#a6e3a1",
            relief="flat",
            bd=0
        )
        self.password_entry.pack(side="left", fill="x", expand=True, ipady=12)

        copy_btn = tk.Button(
            result_frame,
            text="Copy",
            font=("Segoe UI", 10, "bold"),
            bg="#a6e3a1",
            fg="#1e1e2e",
            activebackground="#94e2d5",
            activeforeground="#1e1e2e",
            relief="flat",
            cursor="hand2",
            command=self.copy_password
        )
        copy_btn.pack(side="right", padx=(10, 0), ipady=6, ipadx=8)

        # --- Stärke-Anzeige ---
        self.strength_var = tk.StringVar(value="")
        self.strength_label = tk.Label(
            self.root,
            textvariable=self.strength_var,
            font=("Segoe UI", 11, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4"
        )
        self.strength_label.pack(pady=(5, 15))

    def update_length_label(self, event=None):
        value = int(round(float(self.length_var.get())))
        self.length_var.set(value)

    def generate(self):
        try:
            length = int(self.length_var.get())
            password = generate_password(
                length,
                self.use_lower.get(),
                self.use_upper.get(),
                self.use_digits.get(),
                self.use_symbols.get()
            )
            self.password_var.set(password)

            # Stärke prüfen und anzeigen
            strength = check_password_strength(password)
            self.strength_var.set(f"Stärke: {strength}")

            # Farbe je nach Stärke
            if strength == "Schwach":
                self.strength_label.config(fg="#f38ba8")      # rot
            elif strength == "Mittel":
                self.strength_label.config(fg="#f9e2af")      # gelb
            else:
                self.strength_label.config(fg="#a6e3a1")      # grün

        except ValueError as e:
            messagebox.showerror("Fehler", str(e))
        except Exception as e:
            messagebox.showerror("Fehler", f"Etwas ist schiefgelaufen:\n{e}")

    def copy_password(self):
        password = self.password_var.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Kopiert", "Passwort wurde in die Zwischenablage kopiert!")
        else:
            messagebox.showwarning("Hinweis", "Es wurde noch kein Passwort generiert.")


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()