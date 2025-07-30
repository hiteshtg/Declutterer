#!/usr/bin/env python3

import typer
import os
import helper
import shutil

app = typer.Typer()

@app.command()
def check_directory(path :str):
    helper.check_dir(path = path)

@app.command()
def declutter(path :str):
    files = os.listdir(path)
    for file in files:
        for category, ext in helper.ext_dict.items():
            for extention in ext:
                if file.endswith(extention):
                    shutil.move(os.path.join(path, file), os.path.join(path, category))
    print(f"Files Decluttered")
                
if __name__ == "__main__":
    app()

