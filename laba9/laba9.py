import tkinter as tk
from tkinter import filedialog, messagebox
import fitz

class PDFViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Просмотрщик")
        self.root.geometry("800x600")

        self.pdf_document = None

        self.setup_ui()

    def setup_ui(self):
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side=tk.TOP, fill=tk.X)

        self.open_button = tk.Button(self.button_frame, text="Открыть PDF", command=self.open_pdf)
        self.open_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.scroll_frame = tk.Frame(self.root)
        self.scroll_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.scroll_frame)
        self.scrollbar = tk.Scrollbar(self.scroll_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.inner_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
        self.inner_frame.bind("<Configure>", lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

    def open_pdf(self):
        file_path = filedialog.askopenfilename(
            title="Выберите PDF файл",
            filetypes=(("PDF файлы", "*.pdf"), ("Все файлы", "*.*"))
        )
        if not file_path:
            return

        try:
            self.pdf_document = fitz.open(file_path)
            self.display_all_pages()
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось открыть PDF файл: {e}")

    def display_all_pages(self):
        for widget in self.inner_frame.winfo_children():
            widget.destroy()

        for page_number in range(len(self.pdf_document)):
            page = self.pdf_document[page_number]
            text = page.get_text()

            page_label = tk.Label(self.inner_frame, text=f"Страница {page_number + 1}", font=("Arial", 14, "bold"))
            page_label.pack(anchor="w", pady=10)

            page_text = tk.Text(self.inner_frame, wrap=tk.WORD, height=20)
            page_text.insert(tk.END, text)
            page_text.config(state=tk.DISABLED)
            page_text.pack(anchor="w", fill=tk.BOTH, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFViewerApp(root)
    root.mainloop()
