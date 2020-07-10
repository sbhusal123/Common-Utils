import PIL.Image
import tempfile

def create_test_image():
    """Generate temporary test image file"""
    image = PIL.Image.new('RGB', size=(10, 10))
    file = tempfile.NamedTemporaryFile(suffix='.jpg')
    image.save(file)
    return file