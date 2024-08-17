import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

class CSVParserApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CSV Parser")

        self.label = tk.Label(self.root, text="Upload a CSV File", font=('Arial', 14))
        self.label.pack(pady=10)

        self.upload_button = tk.Button(self.root, text="Upload CSV", command=self.upload_csv, font=('Arial', 12))
        self.upload_button.pack(pady=10)

        self.text_area = tk.Text(self.root, wrap='word', width=60, height=20, font=('Arial', 12))
        self.text_area.pack(pady=10)

        self.data = None

    def upload_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                self.data = pd.read_csv(file_path)
                self.display_data(self.data)
                messagebox.showinfo("Success", "CSV file has been uploaded successfully")
                self.close_and_return_data()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to read the CSV file.\nError: {e}")
    
    def close_and_return_data(self):
        # Close the UI and return the data
        self.root.quit()  # Close the Tkinter main loop
        self.root.destroy()  # Destroy the Tkinter window

    def display_data(self, data):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, data.to_string(index=False))

    def run(self):
        self.root.mainloop()
        return self.data  # Return the DataFrame after the UI closes
        

