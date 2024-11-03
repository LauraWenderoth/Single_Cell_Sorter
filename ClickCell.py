import os
import tkinter as tk
from tkinter import filedialog

from PIL import Image, ImageTk
from tkmacosx import Button


# Step 1: Function to select the image folder and create sorted folders
def select_image_folder():
    initial_dir = os.path.expanduser("~")
    image_folder = filedialog.askdirectory(initialdir=initial_dir)

    if image_folder:
        parent_folder = os.path.dirname(image_folder)
        sorted_folder = os.path.join(
            parent_folder, "sorted_" + os.path.basename(image_folder)
        )
        os.makedirs(sorted_folder, exist_ok=True)

        categories = {
            "Abnormal eosinophil": "#9A4DFF",
            "Artefact": "#A9A9A9",
            "Basophil": "#4682B4",
            "Blast": "#FFA500",
            "Erythroblast": "#FF6347",
            "Eosinophil": "#6495ED",
            "Hairy cell": "#32CD32",
            "Smudge cell": "#3CB371",
            "Immature lymphocyte": "#87CEFA",
            "Lymphocyte": "#1E90FF",
            "Metamyelocyte": "#DAA520",
            "Imature Granulocyt": "#FFD700",
            "Monoblast": "#FFFF00",
            "Monocyte": "#1E90FF",
            "Myelocyte": "#D2691E",
            "Myeloblast": "#FF7F50",
            "Neutrophil (band)": "#4169E1",
            "Neutrophil (segmented)": "#4169E1",
            "Not identifiable": "#4B4B4B",
            "Other cell": "#8B4513",
            "Proerythroblast": "#FF4500",
            "Plasma cell": "#FF69B4",
            "Promyelocyte (bilobed)": "#CD853F",
            "Promyelocyte": "#F4A460",
            "Lymphocyte (atypical)": "#ADD8E6",
            "Platlets": "#8B4513",
        }

        for category in categories:
            os.makedirs(os.path.join(sorted_folder, category), exist_ok=True)

        root.destroy()
        open_sorting_window(
            sorted_folder, categories, image_folder, get_image_paths(image_folder)
        )


# Step 2: Function to get image paths recursively
def get_image_paths(folder):
    image_paths = []
    for root_dir, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(
                (".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff")
            ):
                image_paths.append(os.path.join(root_dir, file))
    return image_paths


# Step 3: Modify the open_sorting_window function
def open_sorting_window(sorted_folder, categories, image_folder, image_paths):
    root = tk.Tk()
    root.title("ClickCell")

    current_image_index = 0
    total_images = len(image_paths)
    last_copied_image_path = None
    last_copied_image_index = None
    back_button_clicked = False

    def display_image():
        nonlocal current_image_index
        if current_image_index < len(image_paths):
            image_path = image_paths[current_image_index]
            image = Image.open(image_path)
            image.thumbnail((500, 500))
            tk_image = ImageTk.PhotoImage(image)
            canvas.create_image(250, 250, anchor=tk.CENTER, image=tk_image)
            canvas.image = tk_image
            progress_label.config(
                text=f"Progress: {current_image_index}/{total_images}"
            )

    def move_to_category(category):
        nonlocal \
            current_image_index, \
            last_copied_image_path, \
            last_copied_image_index, \
            back_button_clicked

        if current_image_index < total_images:
            current_image_path = image_paths[current_image_index]
            destination_folder = os.path.join(sorted_folder, category)
            os.makedirs(destination_folder, exist_ok=True)
            image_filename = os.path.basename(current_image_path)
            destination_path = os.path.join(destination_folder, image_filename)
            os.rename(current_image_path, destination_path)

            last_copied_image_path = destination_path
            last_copied_image_index = current_image_index
            current_image_index += 1
            progress_label.config(
                text=f"Progress: {current_image_index}/{total_images}"
            )
            display_image()
            back_button_clicked = False
        else:
            canvas.delete("all")
            canvas.create_text(
                250,
                250,
                text="Finished\nAll images are classified!",
                font=("Helvetica", 16),
                justify=tk.CENTER,
            )
            progress_label.config(
                text=f"Progress: {current_image_index}/{len(image_paths)}"
            )

    def move_back():
        nonlocal \
            current_image_index, \
            last_copied_image_path, \
            last_copied_image_index, \
            back_button_clicked

        if last_copied_image_path and not back_button_clicked:
            original_folder = image_folder
            image_filename = os.path.basename(last_copied_image_path)
            original_path = os.path.join(original_folder, image_filename)
            os.rename(last_copied_image_path, original_path)

            current_image_index = last_copied_image_index
            progress_label.config(
                text=f"Progress: {current_image_index}/{total_images}"
            )
            display_image()
            back_button_clicked = True

    # Create layout for the central column
    central_frame = tk.Frame(root)
    central_frame.pack(side=tk.LEFT, padx=20, pady=20)

    # Place progress label at the top of the central column
    progress_label = tk.Label(central_frame, text="Progress: 0/0")
    progress_label.pack(anchor=tk.N)

    # Place canvas in the center of the central column
    canvas = tk.Canvas(central_frame, width=500, height=500)
    canvas.pack()

    # Place back button at the bottom of the central column
    back_button = Button(central_frame, text="Back", command=move_back, borderless=1)
    back_button.pack(pady=10)

    # Create buttons for categories on the right
    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.RIGHT, padx=10, pady=10)

    for category, color in categories.items():
        try:
            button = Button(
                button_frame,
                text=category,
                bg=color,
                command=lambda cat=category: move_to_category(cat),
                borderless=1,
            )
            button.pack(side=tk.TOP, fill=tk.X)
        except tk.TclError:
            print(
                f"Color '{color}' is not recognized, defaulting to system color for '{category}'."
            )
            button = Button(
                button_frame,
                text=category,
                command=lambda cat=category: move_to_category(cat),
                borderless=1,
            )
            button.pack(side=tk.TOP, fill=tk.X)

    display_image()
    root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    select_image_folder()
