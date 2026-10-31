import cv2
import numpy as np
from sklearn.decomposition import PCA
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from math import log10, sqrt

# =========================
# MAIN WINDOW
# =========================
root = Tk()

root.title("PCA Image Compression")

root.geometry("1100x700")

root.configure(bg="#f2f5f7")

root.resizable(False, False)

# =========================
# GLOBAL VARIABLES
# =========================
original_image = None
compressed_image = None

# =========================
# PSNR FUNCTION
# =========================
def calculate_psnr(original, compressed):

    mse = np.mean((original - compressed) ** 2)

    if mse == 0:
        return 100

    max_pixel = 255.0

    psnr = 20 * log10(max_pixel / sqrt(mse))

    return psnr

# =========================
# PCA FUNCTION
# =========================
def pca_compress_channel(channel, components):

    pca = PCA(n_components=components)

    transformed = pca.fit_transform(channel)

    reconstructed = pca.inverse_transform(transformed)

    reconstructed = np.clip(reconstructed, 0, 255)

    return reconstructed.astype(np.uint8)

# =========================
# UPLOAD + COMPRESS IMAGE
# =========================
def upload_and_compress():

    global original_image
    global compressed_image

    file_path = filedialog.askopenfilename(
        filetypes=[
            ("Image Files", "*.jpg *.jpeg *.png")
        ]
    )

    if not file_path:
        return

    # Read image
    original_image = cv2.imread(file_path)

    # Split channels
    blue, green, red = cv2.split(original_image)

    # PCA Components
    components = 50

    # Compress channels
    blue_c = pca_compress_channel(blue, components)

    green_c = pca_compress_channel(green, components)

    red_c = pca_compress_channel(red, components)

    # Merge compressed channels
    compressed_image = cv2.merge(
        (blue_c, green_c, red_c)
    )

    # Show original image
    show_image(
        original_image,
        original_panel
    )

    # Show compressed image
    show_image(
        compressed_image,
        compressed_panel
    )

    status_label.config(
        text="Image Compressed Successfully",
        fg="green"
    )

# =========================
# DISPLAY IMAGE
# =========================
def show_image(image, panel):

    img = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB
    )

    img = Image.fromarray(img)

    img = img.resize((400, 300))

    img_tk = ImageTk.PhotoImage(img)

    panel.config(image=img_tk)

    panel.image = img_tk

# =========================
# SAVE IMAGE
# =========================
def save_image():

    global compressed_image

    if compressed_image is None:

        messagebox.showerror(
            "Error",
            "No compressed image available"
        )

        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".jpg",
        filetypes=[
            ("JPEG File", "*.jpg"),
            ("PNG File", "*.png")
        ]
    )

    if file_path:

        cv2.imwrite(
            file_path,
            compressed_image
        )

        messagebox.showinfo(
            "Success",
            "Compressed Image Saved"
        )

# =========================
# SHOW QUALITY GRAPH
# =========================
def show_graph():

    global original_image
    global compressed_image

    if original_image is None or compressed_image is None:

        messagebox.showerror(
            "Error",
            "Upload image first"
        )

        return

    # Quality Values
    original_quality = 100

    compressed_quality = calculate_psnr(
        original_image,
        compressed_image
    )

    labels = [
        "Original Image",
        "Compressed Image"
    ]

    quality = [
        original_quality,
        compressed_quality
    ]

    # Graph
    plt.figure(figsize=(6,5))

    plt.bar(labels, quality)

    plt.ylabel("Quality (PSNR)")

    plt.title("Image Quality Comparison")

    plt.show()

# =========================
# TITLE
# =========================
title = Label(
    root,
    text="PCA IMAGE COMPRESSION",
    font=("Arial", 28, "bold"),
    bg="#f2f5f7",
    fg="#003366"
)

title.pack(pady=20)

# =========================
# BUTTON FRAME
# =========================
button_frame = Frame(
    root,
    bg="#f2f5f7"
)

button_frame.pack(pady=20)

# Upload Button
upload_btn = Button(
    button_frame,
    text="Upload Image",
    font=("Arial", 14, "bold"),
    bg="#007bff",
    fg="white",
    padx=20,
    pady=10,
    command=upload_and_compress
)

upload_btn.grid(row=0, column=0, padx=20)

# Save Button
save_btn = Button(
    button_frame,
    text="Download Compressed Image",
    font=("Arial", 14, "bold"),
    bg="#28a745",
    fg="white",
    padx=20,
    pady=10,
    command=save_image
)

save_btn.grid(row=0, column=1, padx=20)

# Graph Button
graph_btn = Button(
    button_frame,
    text="Show Quality Graph",
    font=("Arial", 14, "bold"),
    bg="#ff9800",
    fg="black",
    padx=20,
    pady=10,
    command=show_graph
)

graph_btn.grid(row=0, column=2, padx=20)

# =========================
# IMAGE FRAME
# =========================
image_frame = Frame(
    root,
    bg="#f2f5f7"
)

image_frame.pack(pady=20)

# Original Image
original_text = Label(
    image_frame,
    text="Original Image",
    font=("Arial", 18, "bold"),
    bg="#f2f5f7"
)

original_text.grid(row=0, column=0)

original_panel = Label(
    image_frame,
    bg="white",
    width=400,
    height=300,
    relief=RIDGE,
    bd=3
)

original_panel.grid(row=1, column=0, padx=40)

# Compressed Image
compressed_text = Label(
    image_frame,
    text="Compressed Image",
    font=("Arial", 18, "bold"),
    bg="#f2f5f7"
)

compressed_text.grid(row=0, column=1)

compressed_panel = Label(
    image_frame,
    bg="white",
    width=400,
    height=300,
    relief=RIDGE,
    bd=3
)

compressed_panel.grid(row=1, column=1, padx=40)

# =========================
# STATUS LABEL
# =========================
status_label = Label(
    root,
    text="No Image Uploaded",
    font=("Arial", 12),
    bg="#f2f5f7",
    fg="red"
)

status_label.pack(pady=10)

# =========================
# RUN APP
# =========================
root.mainloop()