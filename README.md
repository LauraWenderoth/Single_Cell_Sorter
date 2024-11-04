# ClickCell 🦠 📸🧬 - Simple, intuitive and productive

Welcome to **ClickCell** ! This application is designed to provide a low-entry, simple, and fast solution for classifying single-cell images. While intended for haematological single-cell images, this app can easily adapt to various types of images, making it versatile for different research needs.

![CellSorter Application Screenshot](/images/ClickCell.png)

🚀 **Purpose** 🚀 ClickCell aims to assist research groups in the initial prototyping phase by offering an intuitive interface for image classification. With this app, you can quickly classify unlabelled single-cell images simply by viewing them and clicking a button corresponding to the desired class.

## 🖥️ Features

- **Easy to Use**: A straightforward interface that makes navigation and classification simple.
- **Quick Classification**: Classify images in just a few clicks, making your research process faster.
- **Versatile**: While focused on blood cell images, the app can easily be adjusted for different types of single-cell images.
- **Cross-Platform**: Works on both macOS and Linux, so more users can access it.
- **Prototyping Tool**: Great for research groups looking to test out classification methods and gather initial data.

## 📦 ⬇  Download

1. Clone git repository

    ```bash
    git clone https://github.com/LauraWenderoth/ClickCell.git
    cd ClickCell
    ```

2. create conda environment and install requirements

    ```bash
    conda create --name env_clickcell python=3.10
    conda activate env_clickcell
    pip install -r requirements.txt
    ```

3. Building the ClickCell application using PyInstaller

    ```bash
    pyinstaller --onefile --hidden-import='PIL._tkinter_finder' --windowed --icon=icon.ico ClickCell.py
    ```

- Download example data from kaggle

    ```bash
    python download_example_data.py
    ```

## 📥 Getting Started

1. **Open the App**: Double-click the application icon in the ``ClickCell/dist`` folder to launch it.  

    ![CellSorter Application Screenshot](/images/open_app.png)

    or start the app via command line

    ```bash
    cd dist
    ./ClickCell
    ```

3. **Choose Your Images**: This will open a folder where you can select the location of the images you want to classify.

    ![CellSorter Folder Select](/images/select.png)

4. **Classification Process**: After selecting the folder with your images, the app will display one image at a time, along with buttons for each class and a back button (which allows you to go back one image). As you classify the images, the app will copy them from the original folder to a new folder called `$YOURNAME_sorted`, creating subfolders for each class. The aim is to have the original folder empty by the end of the classification process.

    ![Sorted](/images/sorted_folder.png)

5. **Exiting the App**: To exit, click the red button in the top-left corner. When you reopen the app, it will pick up from where you left off, with progress updated to show the remaining unclassified images.

    ![Sorted](/images/adjustedCLickcell.png)

## 🛠️ Requirements

- macOS (version 10.15 or later recommended) or Linux
- A collection of unclassified single-cell images

Thank you for choosing **ClickCell** for your research! Together, we can simplify the classification process and enhance our understanding of hematopathology. Happy classifying! 🎉
