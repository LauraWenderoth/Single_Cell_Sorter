import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Step 1: Create a function to select the image folder and create sorted folders
def select_image_folder():
    # Use filedialog to select the folder
    initial_dir = os.path.expanduser("~")
    image_folder = filedialog.askdirectory(initialdir=initial_dir)

    if image_folder:
        # Create the 'sorted_' folder in the parent directory
        parent_folder = os.path.dirname(image_folder)
        sorted_folder = os.path.join(parent_folder, 'sorted_' + os.path.basename(image_folder))
        os.makedirs(sorted_folder, exist_ok=True)

        # Create subfolders for each category
        categories = {
            "Abnormal eosinophil": "purple",
            "Artefact": "gray",
            "Basophil": "royalblue",
            "Blast": "orange",
            "Erythroblast": "red",
            "Eosinophil": "cornflowerblue",
            "Hairy cell": "green",
            "Smudge cell": "darkgreen",
            "Immature lymphocyte": "lightblue",
            "Lymphocyte": "blue",
            "Metamyelocyte": "goldenrod",
            "Imature Granulocyt": "goldenrod",
            "Monoblast": "yellow",
            "Monocyte": "dodgerblue",
            "Myelocyte": "chocolate",
            "Myeloblast": "orange",
            "Neutrophil (band)": "navy",
            "Neutrophil (segmented)": "darkblue",
            "Not identifiable": "black",
            "Other cell": "brown",
            "Proerythroblast": "red",
            "Plasma cell": "pink",
            "Promyelocyte (bilobed)": "peru",
            "Promyelocyte": "sandybrown",
            "Lymphocyte (atypical)": "lightblue",
            "Platlets": "brown"
        }

        for category in categories:
            os.makedirs(os.path.join(sorted_folder, category), exist_ok=True)

        # Close the current window and open the sorting window
        root.destroy()
        open_sorting_window(sorted_folder, categories, image_folder, get_image_paths(image_folder))


# Step 2: Create a function to get a list of image paths recursively
def get_image_paths(folder):
    image_paths = []
    for root_dir, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp','.tiff')):
                image_paths.append(os.path.join(root_dir, file))
    return image_paths

# Step 3: Modify the open_sorting_window function to display the first image on the left side
def open_sorting_window(sorted_folder, categories, image_folder, image_paths):
    # Create a Tkinter window
    root = tk.Tk()
    root.title("Image Sorter")

    current_image_index = 0
    total_images = len(image_paths)

    # Store the last copied image information
    last_copied_image_path = None
    last_copied_image_index = None

    back_button_clicked = False
    # Define a function to display the next image
    def display_image():
        nonlocal current_image_index
        if current_image_index < len(image_paths):
            image_path = image_paths[current_image_index]
            image = Image.open(image_path)
            image.thumbnail((500, 500))
            tk_image = ImageTk.PhotoImage(image)
            canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
            canvas.image = tk_image
            progress_label.config(text=f"Progress: {current_image_index}/{len(image_paths)}")

    current_image_index = 0

    def move_to_category(category):
        nonlocal current_image_index, last_copied_image_path, last_copied_image_index, back_button_clicked

        if current_image_index < total_images:
            # Get the current image path
            current_image_path = image_paths[current_image_index]

            # Move the current image to the corresponding category folder
            destination_folder = os.path.join(sorted_folder, category)
            os.makedirs(destination_folder, exist_ok=True)
            image_filename = os.path.basename(current_image_path)
            destination_path = os.path.join(destination_folder, image_filename)
            os.rename(current_image_path, destination_path)

            # Store the last copied image information
            last_copied_image_path = destination_path
            last_copied_image_index = current_image_index

            # Update the progress label
            current_image_index += 1
            progress_label.config(text=f"Progress: {current_image_index}/{total_images}")

            # Display the next image
            display_image()
            back_button_clicked = False
        else:
            # All images are classified
            canvas.delete("all")  # Clear the canvas
            canvas.create_text(250, 250, text="Finished\nAll images are classified!", font=("Helvetica", 16), justify=tk.CENTER)
            progress_label.config(text=f"Progress: {current_image_index}/{len(image_paths)}")

    def move_back():
        nonlocal current_image_index, last_copied_image_path, last_copied_image_index, back_button_clicked

        if last_copied_image_path and not back_button_clicked:
            # Move the last copied image back to the original folder
            original_folder = image_folder
            image_filename = os.path.basename(last_copied_image_path)
            original_path = os.path.join(original_folder, image_filename)
            os.rename(last_copied_image_path, original_path)

            # Update the progress label and current_image_index
            current_image_index = last_copied_image_index
            progress_label.config(text=f"Progress: {current_image_index}/{total_images}")

            # Display the last copied image again
            display_image()

            # Set the "Back" button clicked flag to True
            back_button_clicked = True


    # Create a frame to hold the buttons on the right side
    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.RIGHT, padx=10)

    # Create buttons for each category
    for category, color in categories.items():
        button = tk.Button(button_frame, text=category, bg=color, command=lambda cat=category: move_to_category(cat))
        button.pack(side=tk.TOP, fill=tk.X)

     # Create a "Back" button under the image
    back_button = tk.Button(root, text="Back", command=move_back)
    back_button.pack(side=tk.BOTTOM, padx=10, pady=10)


    # Create a canvas to display the image
    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack(side=tk.LEFT, padx=10)

    # Create a progress bar label
    progress_label = tk.Label(root, text="Progress: 0/0")
    progress_label.pack()

    # Load and display the first image
    display_image()

    root.mainloop()


# Step 3: Call the select_image_folder function to start the application
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    select_image_folder()
