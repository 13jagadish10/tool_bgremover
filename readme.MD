# Background Remover Tool

A simple Python-based tool to remove the backgrounds of images using the **rembg** library. The tool processes all images in the specified input folder and saves the output as `.webp` images in the output folder.

---

## Features

- Automatically removes the background from images.
- Supports `.jpg`, `.jpeg`, and `.png` image formats as input.
- Converts and saves output images in `.webp` format.
- Efficiently processes multiple images in a single run.
- Easy to customize file paths and formats.

---

## Prerequisites

Before running the tool, ensure you have the following installed:

1. **Python 3.7 or higher**
2. Required Python packages:
   - **rembg**
   - **Pillow**

To install the required packages, run:
```bash
pip install rembg pillow
