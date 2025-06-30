# ROI Cropper GUI Tool

A simple GUI tool to help you quickly crop rectangles of interest (ROIs) and obtain their coordinates in order to train your neural networks.

<p align="center">
<img src="https://i.ibb.co/wNZxGkBW/Captura-de-pantalla-2025-06-25-161840.png" width="700">
</p>

## Installation
1. Clone this repository:
```
    git clone https://github.com/CovaVJ/roi-cropper.git
    cd roi-cropper
```
2. Create a virtual environment (optional but recommended):
```
    python -m venv venv
    source venv/bin/activate # or on Windows -> .\venv\Scripts\activate
```
3. Install dependencies:
```
    pip install -r requirements.txt
```

## Usage

- Open the `roiCropper.py` file and configure the **variables**. Check them [here](#configuration-variables).
- **Run `roiCropper.py`**. A graphical user interface will appear. Make sure to check the console while using this tool, as additional information will be printed there.
- On your image, **click on the upper-left corner** of the ROI you want to crop. A blue dot will be drawn.
- Then, **click on the lower-right corner**. A red dot and a rectangle will be drawn. This rectangle contains the area that will be cropped.
- Keep selecting points to define more ROIs, and click on 'Next image' when you're ready to save. You can click 'Undo' to remove the last point you selected.
- Every time you click 'Next image' or close the window, all cropped ROIs and a text file will be saved for the current image. Keep in mind that these output files **will be overwritten** each time you run the tool (if the image name remains the same).
- More information about the output is available [here](#output).

<p align="center">
    <img src="https://i.ibb.co/5W9p7cf3/Captura-de-pantalla-2025-06-25-162010.png" width="350">
</p>
<p align="center">
    Example of console output during usage
</p>

## Configuration Variables

- `input_path`: Path to your original images directory.
- `cmap`: Colormap used to display and save images. You can check all available maps on [Matplotlib’s page](https://matplotlib.org/stable/users/explain/colors/colormaps.html).
- `coords_path`: Path where the generated text files containing the selected coordinates for each image will be saved.
- `cropped_path`: Path where the cropped rectangles of interest will be saved.
- `img_format`: Format of both input and output images.

## Output

This tool will generate:

- A **text file** for each input image. It will have the same name as the image but with a `.txt` extension. It will contain the coordinates of every pair of points that form a rectangle, with one rectangle per line. Each line in this file represents a ROI selected on your image. If an odd number of points is selected, the last line will contain only one point. If no points are selected, this file will be empty.
- As many **cropped images** as ROIs you selected for each input image. These images will contain the pixels within the corresponding ROI. If an odd number of points is selected, a ROI cannot be generated, and a cropped image will not be saved.

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.