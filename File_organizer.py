import os
import shutil
import tkinter as tk 
from tkinter import filedialog

class FileOrganizerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("File Organizer")
        self.master.geometry("400x200")

        self.label = tk.Label(self.master, text="Select a directory to organize:")
        self.label.pack(pady=10)

        self.browse_button = tk.Button(self.master, text="Browse", command=self.browse_directory)
        self.browse_button.pack(pady=10)

        self.organize_button = tk.Button(self.master, text="Organize Files", command=self.organize_files)
        self.organize_button.pack(pady=10)

    def browse_directory(self):
        self.directory_path = filedialog.askdirectory()
        self.label.config(text=f"Selected Directory: {self.directory_path}")

    def organize_files(self):
        if not hasattr(self, 'directory_path') or not self.directory_path:
            self.label.config(text="Please select a directory first.")
            return

        self.label.config(text="Organizing files...")

        for filename in os.listdir(self.directory_path):
            file_path = os.path.join(self.directory_path, filename)

            if os.path.isfile(file_path):
                file_type = self.get_file_type(filename)
                target_folder = os.path.join(self.directory_path, file_type)

                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                shutil.move(file_path, os.path.join(target_folder, filename))

        self.label.config(text="Files organized successfully!")

    def get_file_type(self, filename):
        file_extension = filename.split('.')[-1].lower()

        # Define file types and their corresponding folders
        file_types = {
            'images': ['jpg', 'jpeg', 'png', 'gif'],
            'documents': ['pdf', 'doc', 'docx', 'txt'],
            'videos': ['mp4', 'avi', 'mkv', 'mov'],
            'others': []  # Default folder for unrecognized file types
        }

        for file_type, extensions in file_types.items():
            if file_extension in extensions:
                return file_type

        return 'others'


if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerApp(root)
    root.mainloop()
