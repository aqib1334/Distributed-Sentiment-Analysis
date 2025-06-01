import tkinter as tk
from tkinter import messagebox, ttk
import sentiment_analysis_gui  # Make sure this is in the same directory

class CustomLoginUI:
    def __init__(self, root):  # FIX: __init__, not _init_
        self.root = root
        self.root.title("Sentiment Analysis - Login")
        self.root.geometry("900x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f5f5f5")

        # Fonts
        self.title_font = ("Segoe UI", 24, "bold")
        self.label_font = ("Segoe UI", 11)
        self.button_font = ("Segoe UI", 12, "bold")
        self.entry_font = ("Segoe UI", 11)

        # Left Frame
        left_frame = tk.Frame(root, width=400, height=500, bg="#34495e")
        left_frame.pack(side="left", fill="both")

        canvas = tk.Canvas(left_frame, width=400, height=500, bg="#34495e", highlightthickness=0)
        canvas.pack()

        for i in range(500):
            gradient = "#{:02x}{:02x}{:02x}".format(
                52 + int(i * (104 / 500)),
                73 + int(i * (32 / 500)),
                94 + int(i * (26 / 500))
            )
            canvas.create_line(0, i, 400, i, fill=gradient)

        canvas.create_text(200, 180, text="Sentiment Analysis", font=self.title_font, fill="white", anchor="center")
        canvas.create_text(200, 230, text="Understand emotions in text", font=("Segoe UI", 12), fill="#ecf0f1", anchor="center")
        canvas.create_text(200, 350, text="📊", font=("Segoe UI", 80), fill="white")
        canvas.create_text(200, 420, text="Analyze Text Emotions", font=("Segoe UI", 14), fill="#ecf0f1")

        # Right Frame
        right_frame = tk.Frame(root, bg="white", width=500, height=500)
        right_frame.pack(side="right", fill="both", expand=True)

        header = tk.Frame(right_frame, bg="white", height=50)
        header.pack(fill="x")

        tk.Button(header, text="✕", font=("Segoe UI", 14), fg="#7f8c8d", bg="white",
                  bd=0, activebackground="#e74c3c", activeforeground="white",
                  command=root.destroy, cursor="hand2").pack(side="right", padx=10)

        content = tk.Frame(right_frame, bg="white")
        content.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(content, text="Welcome Back!", font=self.title_font, bg="white", fg="#2c3e50")\
            .grid(row=0, column=0, pady=(0, 30), columnspan=2)

        tk.Label(content, text="Username", font=self.label_font, bg="white", fg="#7f8c8d")\
            .grid(row=1, column=0, sticky="w", pady=(0, 5))

        self.username_entry = ttk.Entry(content, font=self.entry_font, width=30)
        self.username_entry.grid(row=2, column=0, pady=(0, 20), ipady=5)
        self.username_entry.focus()

        tk.Label(content, text="Password", font=self.label_font, bg="white", fg="#7f8c8d")\
            .grid(row=3, column=0, sticky="w", pady=(0, 5))

        self.password_entry = ttk.Entry(content, font=self.entry_font, width=30, show="•")
        self.password_entry.grid(row=4, column=0, pady=(0, 30), ipady=5)

        style = ttk.Style()
        style.configure("TButton", font=self.button_font, padding=10)
        style.map("TButton", background=[("active", "#1b82c6"), ("!disabled", "#1b6494")],
                  foreground=[("!disabled", "black")])

        login_btn = ttk.Button(content, text="Login", style="TButton", command=self.login_action, cursor="hand2")
        login_btn.grid(row=5, column=0, sticky="ew", pady=(0, 20))

        footer = tk.Frame(content, bg="white")
        footer.grid(row=6, column=0, sticky="ew")

        tk.Label(footer, text="Forgot password?", font=("Segoe UI", 9), fg="#3498db", bg="white", cursor="hand2").pack(side="left")
        tk.Label(footer, text="Don't have an account? Sign up", font=("Segoe UI", 9), fg="#7f8c8d", bg="white").pack(side="right")

        self.root.bind("<Return>", lambda event: self.login_action())

    def login_action(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "12345":
            messagebox.showinfo("Login Success", "Welcome to Sentiment Analysis!")
            self.root.destroy()  # Close login window

            # Launch new centered window for sentiment GUI
            new_root = tk.Tk()

            # Set a default size (adjust if needed)
            default_width = 1100
            default_height = 700
            screen_width = new_root.winfo_screenwidth()
            screen_height = new_root.winfo_screenheight()
            x = (screen_width // 2) - (default_width // 2)
            y = (screen_height // 2) - (default_height // 2)
            new_root.geometry(f"{default_width}x{default_height}+{x}+{y}")

            # Now load the sentiment GUI app in the centered window
            sentiment_analysis_gui.SentimentAnalyzerApp(new_root)

            new_root.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
            self.password_entry.delete(0, tk.END)



# Main launcher
if __name__ == "__main__":
    window = tk.Tk()
    try:
        window.iconbitmap("sentiment_icon.ico")
    except:
        pass
    app = CustomLoginUI(window)
    window.eval('tk::PlaceWindow . center')
    window.mainloop()
