# PCA Image Compression

## About the Project
PCA Image Compression is a Python-based application that uses Principal Component Analysis (PCA) to reduce image size while maintaining image quality.

The application allows users to upload an image, compress it using PCA, compare the original and compressed images, and view image quality through a graph.

## Features
- Upload images in JPG, JPEG, and PNG formats.
- Compress images using Principal Component Analysis (PCA).
- Display original and compressed images side by side.
- Download the compressed image.
- Calculate image quality using PSNR (Peak Signal-to-Noise Ratio).
- Display a quality comparison graph.

## Technologies Used
- **Python** – Main programming language.
- **OpenCV** – Image processing.
- **NumPy** – Numerical operations.
- **Scikit-learn** – PCA implementation.
- **Tkinter** – Graphical User Interface (GUI).
- **Pillow (PIL)** – Image display and handling.
- **Matplotlib** – Graph generation.

## Project Structure

```text
PCA-Image-Compression/
│
├── main.py
├── README.md
└── requirements.txt
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/PCA-Image-Compression.git
```

### 2. Open the Project Folder

```bash
cd PCA-Image-Compression
```

### 3. Install Required Libraries

```bash
pip install opencv-python numpy scikit-learn pillow matplotlib
```

### 4. Run the Application

```bash
python main.py
```

## How to Use

1. Run the Python application.
2. Click on **Upload Image**.
3. Select an image from your computer.
4. The application automatically compresses the image using PCA.
5. Compare the original and compressed images.
6. Click **Download Compressed Image** to save the result.
7. Click **Show Quality Graph** to view the PSNR comparison.

## Working Method

The project uses Principal Component Analysis (PCA) to reduce image data.

1. The uploaded image is divided into three colour channels: Blue, Green, and Red.
2. PCA is applied separately to each channel.
3. The number of principal components is set to 50.
4. The image is reconstructed using the selected components.
5. The reconstructed channels are combined to generate the compressed image.
6. PSNR is calculated to measure the quality of the compressed image.

## Image Quality Measurement

The project uses **PSNR (Peak Signal-to-Noise Ratio)** to measure the difference between the original and compressed images.

A higher PSNR value generally indicates better image quality.

## Applications
- Image storage optimization.
- Digital image processing.
- Image transmission.
- Data compression.
- Computer vision applications.

## Future Improvements
- Allow users to select the number of PCA components.
- Display image size before and after compression.
- Calculate compression ratio.
- Support more image formats.
- Improve compression speed and performance.

## Author

**Prashant Tiwari**

## License

This project is developed for educational and academic purposes.
