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
    for dir_path, dire, files in os.walk(path, topdown=False):
        for file in files:
            for category, ext in helper.ext_dict.items():
                for extention in ext:
                    if file.endswith(extention):
                        if not os.path.isdir(os.path.join(dir_path, category)):
                            os.mkdir(os.path.join(dire, category))
                        move(os.path.join(dir_path, file), os.path.join(path, category, file))
    print(f"Files Decluttered")
                
if __name__ == "__main__":
    app()

