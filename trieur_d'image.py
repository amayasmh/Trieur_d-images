#coding: utf-8

from pathlib import Path

dirs = {".png" : "Png",
        ".jpg" : "Jpg",
        ".jpeg": "Jpeg" 
}

tri_dir = Path.home() / "Bureau" / "img"
filles = [f for f in tri_dir.iterdir() if f.is_file()]

for f in filles:
    output_dir = tri_dir / dirs.get(f.suffix,"Autres")
    output_dir.mkdir(exist_ok = True)
    f.rename(output_dir / f.name)
    





