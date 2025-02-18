from PIL import Image, ImageGrab, ImageFilter, ImageOps, ImageEnhance
import tempfile
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import numpy as np

def check_balance():
    # capture = ImageGrab.grab(bbox=(33, 893, 181, 923))
    capture = ImageGrab.grab(bbox=(25, 880, 190, 930))

    capture = capture.convert("RGBA")
    
    # Convert the image to a NumPy array
    data = np.array(capture)
    
    # Define a mask to isolate the exact green pixels
    green_mask = (data[:, :, 0] == 0) & (data[:, :, 1] == 255) & (data[:, :, 2] == 0) & (data[:, :, 3] == 255)
    
    # Create a new image where the exact green pixels are white and other pixels are black
    filtered_data = np.zeros_like(data)
    filtered_data[green_mask] = [255, 255, 255, 255]
    
    # Convert the filtered data back to an image
    filtered_image = Image.fromarray(filtered_data)
    
    # Convert the image to grayscale
    capture = ImageOps.grayscale(filtered_image)
    
    # Increase the contrast
    enhancer = ImageEnhance.Contrast(capture)
    capture = enhancer.enhance(2)

    # Sharpen the image
    capture = capture.filter(ImageFilter.SHARPEN)
    
    # Apply thresholding
    capture = capture.point(lambda x: 0 if x < 140 else 255, '1')
    
    # Resize the image to improve OCR accuracy
    capture = capture.resize((capture.width * 2, capture.height * 2), Image.Resampling.LANCZOS)
    
    # Optional: Save the processed image to a file to inspect the result
    # capture.save("processed_image.png")

    # Extract text from the image using pytesseract with specific configuration
    custom_config = r'--oem 3 --psm 6 outputbase digits'
    text = pytesseract.image_to_string(capture, config=custom_config)
    return float(text.strip())
    