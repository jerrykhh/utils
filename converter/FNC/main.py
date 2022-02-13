import sys
from pathlib import Path
from fnc import Fn, Fnc


def main():
    fn = Fn(sys.argv)
    paths = sys.argv[3::]
    for path in paths:
        if path != "/":
            convert(fn.get_fnc(), path)
        
def convert(fnc: Fnc, target_path):
    path = Path(target_path)
    
    filename, convert_status = fnc.convert_filename(path.stem)
    
    filename = f"{path.parent}/{filename}"
    
    if path.is_file():
        filename += path.suffix
        
    if path.is_dir():
        for file in path.iterdir():
            convert(fnc, file.resolve())
            
    print(filename)
    
    if convert_status:
        path.rename(filename)
    
if __name__ == "__main__":
    main()