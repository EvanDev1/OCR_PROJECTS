from PIL import ImageGrab, ImageFilter, ImageOps
import tempfile
import os
import re
from ocrspace import API

import time

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# OCR_api_key = "K87833002088957"
OCR_api_key = "K87155629288957"

OCR_api = API(api_key=OCR_api_key, language='eng', ocrengine='2')
dur_pattern = r'\b(?:\d+h\s*\d+m|\d+m\s*\d+s|\d+s)\b'


class Processing():
    def capture(cords, threshold=False):
        region = cords
        capture = ImageGrab.grab(bbox=region)

        capture = ImageOps.grayscale(capture)
        capture = capture.filter(ImageFilter.SHARPEN)
        
        if threshold:
            capture = capture.point(lambda p: 0 if p < threshold else 255)

        return capture
    
    def extract_text(image):
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_img:
            temp_img_path = temp_img.name
            image.save(temp_img_path)

        # text = pytesseract.image_to_string(temp_img_path, lang='eng', config=f"--psm 6 --oem 3")
        text = OCR_api.ocr_file(temp_img_path)

        os.unlink(temp_img_path)
        return text
    
    def extract_duration_line(text):
        # Define the duration pattern for regex matching
        dur_pattern = r'\b(?:\d+h|\d+m|\d+s)\b'

        # Process each line and find the line that contains the duration pattern
        for line in text.split('\n'):
            if re.search(dur_pattern, line):
                return line

        # If no line contains the duration pattern, return None
        return None
    
    def get_duration(capture):
        width, height = capture.size
        crop_box = (width - 35, 100, width, height)
        dur_capture = capture.crop(crop_box)

        dur_capture = ImageOps.grayscale(dur_capture)
        dur_capture = ImageOps.autocontrast(dur_capture)

        dur_capture = dur_capture.filter(ImageFilter.GaussianBlur(radius=1))
        dur_text = Processing.extract_text(dur_capture)

        return Processing.extract_duration_line(dur_text)
        

    def has_recipe(capture, item):
        width, height = capture.size

        crop_box = (0, 0, 50, height)
        
        recipe_capture = capture.crop(crop_box)

        recipe_capture = ImageOps.grayscale(recipe_capture)
        recipe_capture = ImageOps.autocontrast(recipe_capture)
        recipe_capture = recipe_capture.filter(ImageFilter.GaussianBlur(radius=1))

        extracted_text = Processing.extract_text(recipe_capture).lower()
        if 'recipe' in extracted_text:
            return True
        else:
            print(f'COULD NOT FIND RECIPE FOR {item}')




    def process_text(current_item, text, item_list):
        # Define the words to check for
        words_to_check = ['water', 'axnit', 'gel', 'korrelite', 'narcor', 'red narcor', 'reknite', 'vexnium', 'blue', 'drone command core', 'power cell', 'metal scraps']
        
        # Split the text into lines
        idx = []
        for word in words_to_check:
            if word in text:
                idx.append(text.find(word))
        for item in item_list:
            lower_t = item.lower()
            
            if lower_t in text.lower():
                index = text.lower().find(lower_t)
                idx.append(index)
        
        cutoff_index = min(idx)
        cut_text = text[cutoff_index:]

        lines = cut_text.splitlines()
        has_blueprint = False

        cut_lines = []

        for line in lines:
            if 'geltium' in line:
                new_line = line.replace('geltium', 'gellium', 1)
                cut_lines.append(new_line)
            elif 'blue' in line:
                has_blueprint = True
            elif line != '':
                match = False
                for word in words_to_check:
                    if word in line:
                        match = True
                        break
                for item in item_list:
                    lower_t = item.lower()
                    if lower_t in line.lower():
                        match = True
                if 'cell' in line:
                    match = True
                if match:
                    cut_lines.append(line)
        item_recipe = {}
        if has_blueprint == True:
            item_recipe = {current_item + ' blueprint': 1}
        for line in cut_lines:
            match = re.search(r'((?:\w+\s*)+)\s*\((\d+)\)', line)
            
            if match:
                word_before_number = match.group(1).strip().title()  # Capturing group 1 corresponds to the word before the number
        
                extracted_number = match.group(0)[match.group(0).index('(') + 1:-1]  # Extract the number
                item_recipe[word_before_number] = int(extracted_number)
            elif ('drone command core' in line):
                item_recipe['Drone Command Core'] = 1
            else:
                for item in item_list:
                    if item.lower() in line.lower():
                        item_recipe[line] = 1
                        match = True
                if match == False:
                    print(f"No match found for line for item {current_item} Line: {line}")
                    print(cut_lines)

        return item_recipe



    def capture_recipe(capture, item, item_list):
        width, height = capture.size

        show_width = 123

        left_crop = max(width - show_width, 0)
        crop_box = (left_crop, 0, width, height)

        recipe_capture = capture.crop(crop_box)

        recipe_capture = ImageOps.grayscale(recipe_capture)
        recipe_capture = ImageOps.autocontrast(recipe_capture)

        text = Processing.extract_text(capture).lower()
        return Processing.process_text(item, text, item_list)


    def get_item_recipe(item_name, item_list):
        
        capture = Processing.capture((1060, 380, 1217, 790))

        time.sleep(1)

        item_duration = Processing.get_duration(capture)

        item_recipe = Processing.capture_recipe(capture, item_name, item_list)
        item_recipe['duration'] = item_duration

        return item_recipe




    def remove_suffix(text):
        if text.endswith('_'):
            text = text[:-1]  # Remove the '_' at the end
        if text.endswith(' -'):
            text = text[:-2]  # Remove the ' -' at the end
        return text
        


