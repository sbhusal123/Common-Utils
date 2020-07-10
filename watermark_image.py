from PIL import Image
import os

"""
pip install pillow
"""

def watermark_image(original_image_path, name):
    ROOT_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    water_mark_image_path = ROOT_DIR + '/path/to/watermark/confidential.png'
    save_image_path = ROOT_DIR + '/path/to/save'+name

    letter = Image.open(original_image_path)

    letterWidth = letter.width
    letterHeight = letter.height

    confedential = Image.open(water_mark_image_path)
    confedentialWidth = confedential.width
    confedentialHeight = confedential.height

    size = 100,100
    watermark = confedential.resize(size)
    watermark_width = watermark.width
    watermark_height = watermark.height    

    try:
        letter.paste(watermark, (int(letterHeight/2-watermark_height/2), int(letterWidth/2-watermark_width/2)), watermark)
        letter.save(save_image_path)
    except Exception as e:
        print(e)