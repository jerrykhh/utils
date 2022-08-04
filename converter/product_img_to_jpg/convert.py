from pathlib import Path
from PIL import Image
import sys
import uuid

def main():
    
    paths = sys.argv[1::]
    for path in paths:
        if path != "/":
            print(path)
            convert(path)
        else:
            print(f'{path} is not vaild')
        
def convert(dir_name: str):
    
    path = Path(dir_name)
    
    if path.is_file():
        sku = path.parent.absolute().name
        
        if path.suffix != ".jpg" and path.name != ".DS_Store":
            print(f"{path.parent}/{path.name}")
            image = Image.open(f"{path.parent}/{path.name}")
            rgb_image = image.convert("RGB")
            # file_name = str(path.stem).replace(".jpg","")
            sku = path.parent.absolute().name
            rgb_image.save(f"{path.parent}/{sku}-{uuid.uuid4().hex}.jpg")
            path.unlink()
        elif path.suffix == ".jpg":
            path.rename(f"{path.parent}/{sku}-{uuid.uuid4().hex}.jpg")
            
                    
    if path.is_dir():
        for file in path.iterdir():
            convert(file.resolve())
        

if __name__ == "__main__":
    main()