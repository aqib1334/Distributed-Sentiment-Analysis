import tkinter as tk
from tkinter import messagebox
import data_preprocessing
import model1
import model2
import model3
import ensemble_evaluation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import pandas as pd
from io import BytesIO
from PIL import Image, ImageTk
import base64


class SentimentAnalyzerApp:
    def __init__(self, master):
        self.master = master
        master.title("Distributed Sentiment Analysis System")
        master.geometry("1000x850")
        master.resizable(False, False)

        tk.Label(master, text="Distributed Sentiment Analysis System",
                 font=("Helvetica", 20, "bold"), fg="#2c3e50").pack(pady=15)

        btn_frame = tk.Frame(master, bg="#ecf0f1")
        btn_frame.pack(pady=10)

        self.btn_preprocess = tk.Button(btn_frame, text="1. Data Preprocessing", width=20,
                                        font=("Helvetica", 12), bg="#3498db", fg="white",
                                        command=self.run_preprocessing)
        self.btn_preprocess.pack(side=tk.LEFT, padx=5)

        self.btn_model1 = tk.Button(btn_frame, text="2. Train Model 1", width=20,
                                    font=("Helvetica", 12), bg="#2ecc71", fg="white",
                                    command=self.run_model1)
        self.btn_model1.pack(side=tk.LEFT, padx=5)

        self.btn_model2 = tk.Button(btn_frame, text="3. Train Model 2", width=20,
                                    font=("Helvetica", 12), bg="#27ae60", fg="white",
                                    command=self.run_model2)
        self.btn_model2.pack(side=tk.LEFT, padx=5)

        self.btn_model3 = tk.Button(btn_frame, text="4. Train Model 3", width=20,
                                    font=("Helvetica", 12), bg="#1abc9c", fg="white",
                                    command=self.run_model3)
        self.btn_model3.pack(side=tk.LEFT, padx=5)

        self.btn_eval = tk.Button(btn_frame, text="5. Ensemble Evaluation", width=22,
                                  font=("Helvetica", 12), bg="#e67e22", fg="white",
                                  command=self.run_ensemble)
        self.btn_eval.pack(side=tk.LEFT, padx=5)

        self.preprocess_frame = tk.LabelFrame(master, text="🧹 Preprocessing Summary", font=("Helvetica", 13, "bold"),
                                              padx=15, pady=10)
        self.preprocess_frame.pack(pady=10, fill="both")

        self.preprocess_text = tk.Text(self.preprocess_frame, height=6, width=100, wrap=tk.WORD,
                                       font=("Helvetica", 11))
        self.preprocess_text.pack()

        self.summary_frame = tk.LabelFrame(master, text="🧠 Model Training Summary", font=("Helvetica", 13, "bold"),
                                           padx=15, pady=10)
        self.summary_frame.pack(pady=10, fill="both")

        summary_scrollbar = tk.Scrollbar(self.summary_frame)
        summary_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.summary_text = tk.Text(self.summary_frame, height=10, width=100, wrap=tk.WORD, yscrollcommand=summary_scrollbar.set)
        self.summary_text.pack(side=tk.LEFT, fill=tk.BOTH)
        summary_scrollbar.config(command=self.summary_text.yview)

        self.eval_frame = tk.LabelFrame(master, text="📈 Evaluation Results", font=("Helvetica", 13, "bold"),
                                        padx=10, pady=10)
        self.eval_frame.pack(pady=10, fill="both", expand=True)

        eval_canvas = tk.Canvas(self.eval_frame)
        eval_scrollbar = tk.Scrollbar(self.eval_frame, orient="vertical", command=eval_canvas.yview)
        self.eval_content = tk.Frame(eval_canvas)

        self.eval_content.bind("<Configure>", lambda e: eval_canvas.configure(scrollregion=eval_canvas.bbox("all")))

        eval_canvas.create_window((0, 0), window=self.eval_content, anchor="nw")
        eval_canvas.configure(yscrollcommand=eval_scrollbar.set)

        eval_canvas.pack(side=tk.LEFT, fill="both", expand=True)
        eval_scrollbar.pack(side=tk.RIGHT, fill="y")

        self.viz_frame = tk.LabelFrame(master, text="🌊 Visualizations", font=("Helvetica", 13, "bold"), padx=10, pady=10)
        self.viz_frame.pack(pady=10, fill="both", expand=True)

        viz_canvas = tk.Canvas(self.viz_frame)
        viz_scrollbar = tk.Scrollbar(self.viz_frame, orient="vertical", command=viz_canvas.yview)
        self.viz_content = tk.Frame(viz_canvas)

        self.viz_content.bind("<Configure>", lambda e: viz_canvas.configure(scrollregion=viz_canvas.bbox("all")))

        viz_canvas.create_window((0, 0), window=self.viz_content, anchor="nw")
        viz_canvas.configure(yscrollcommand=viz_scrollbar.set)

        viz_canvas.pack(side=tk.LEFT, fill="both", expand=True)
        viz_scrollbar.pack(side=tk.RIGHT, fill="y")

        footer = tk.Frame(master, pady=10)
        footer.pack()
        tk.Label(footer, text="© 2025 Distributed Sentiment Analyzer",
                 font=("Helvetica", 10), fg="#95a5a6").pack()

    def run_preprocessing(self):
        result = data_preprocessing.preprocess_data()
        self.preprocess_text.insert(tk.END, "Preprocessing completed.\nFiles generated:\ndata_part1.csv\ndata_part2.csv\ndata_part3.csv\n" + "-"*50 + "\n")
        messagebox.showinfo("Preprocessing Result", result)

    def run_model1(self):
        result = model1.train_model1()
        self.summary_text.insert(tk.END, "Model 1 trained on data_part1.csv\nAlgorithm: Random Forest\nVectorization: TF-IDF\nFiles: model1.pkl, vectorizer1.pkl\n" + "-"*50 + "\n")
        messagebox.showinfo("Model 1", result)

    def run_model2(self):
        result = model2.train_model2()
        self.summary_text.insert(tk.END, "Model 2 trained on data_part2.csv\nAlgorithm: Random Forest\nVectorization: TF-IDF\nFiles: model2.pkl, vectorizer2.pkl\n" + "-"*50 + "\n")
        messagebox.showinfo("Model 2", result)

    def run_model3(self):
        result = model3.train_model3()
        self.summary_text.insert(tk.END, "Model 3 trained on data_part3.csv\nAlgorithm: Random Forest\nVectorization: TF-IDF\nFiles: model3.pkl, vectorizer3.pkl\n" + "-"*50 + "\n")
        messagebox.showinfo("Model 3", result)

    def run_ensemble(self):
        # Show loading in main frame
        for widget in self.eval_content.winfo_children():
            widget.destroy()

        loading_label = tk.Label(self.eval_content, text="🔄 Evaluating ensemble model, please wait...",
                                font=("Helvetica", 13), fg="blue")
        loading_label.pack(pady=20)

        self.master.update_idletasks()

        # Run ensemble evaluation
        accuracy, y_true, y_pred, label_counts = ensemble_evaluation.evaluate_models(return_details=True)

        # Clear loading
        for widget in self.eval_content.winfo_children():
            widget.destroy()

        acc_label = tk.Label(self.eval_content, text=f"✅ Ensemble Accuracy: {accuracy:.2f}",
                            font=("Helvetica", 14, "bold"), fg="#2ecc71")
        acc_label.pack(pady=20)

        # -------------------------
        # Create Pop-Up Visualization Window
        # -------------------------
        viz_window = tk.Toplevel(self.master)
        viz_window.title("📊 Visualizations")
        viz_window.geometry("800x700")

        canvas = tk.Canvas(viz_window)
        scrollbar = tk.Scrollbar(viz_window, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas)

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=tk.LEFT, fill="both", expand=True)
        scrollbar.pack(side=tk.RIGHT, fill="y")

        # Confusion Matrix
        cm = confusion_matrix(y_true, y_pred)
        fig1, ax1 = plt.subplots(figsize=(6, 6))
        ConfusionMatrixDisplay(confusion_matrix=cm).plot(ax=ax1)
        ax1.set_title("Confusion Matrix", fontsize=14)

        buf1 = BytesIO()
        fig1.savefig(buf1, format="png", bbox_inches="tight")
        buf1.seek(0)
        img1 = Image.open(buf1)
        img1 = ImageTk.PhotoImage(img1)

        label_img1 = tk.Label(scroll_frame, image=img1)
        label_img1.image = img1
        label_img1.pack(pady=20)

        # Bar Chart
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        ax2.bar(label_counts.keys(), label_counts.values(), color=['#3498db', '#e74c3c', '#2ecc71'])
        ax2.set_title("Sentiment Distribution", fontsize=14)

        buf2 = BytesIO()
        fig2.savefig(buf2, format="png", bbox_inches="tight")
        buf2.seek(0)
        img2 = Image.open(buf2)
        img2 = ImageTk.PhotoImage(img2)

        label_img2 = tk.Label(scroll_frame, image=img2)
        label_img2.image = img2
        label_img2.pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = SentimentAnalyzerApp(root)
    root.mainloop()