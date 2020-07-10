import os
import pathlib
import uuid

"""
pip install uuid
"""

def unique_file_name(filename):
    """Generate uniqie file name"""

    # Get storage path
    ROOT_DIR =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = pathlib.Path(ROOT_DIR+"/uploads/")

    # Create directory if not exists
    if not path.exists():
        print(path.exists())
        os.makedirs(path)

    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename