import barcode
import os

"""
pip install python-barcode
"""

def generate_barcode(id):
    provider = barcode.get_barcode_class('itf')
    # print(barcode.PROVIDED_BARCODES) # Providers
    bar = provider(str(id))

    path = 'your/save/path'
    bar.save(path+str(id))

if __name__ == "__main__":
    generate_barcode(200)
