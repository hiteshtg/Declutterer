# 📂 Declutterer - File Organizer Tool

**Declutterer** is a simple yet effective Python-based file organizer. It helps you clean up a given directory by moving files into categorized subfolders based on file extensions.

Great for organizing cluttered folders like `~/Downloads`, `~/.config`, or any messy directory.

---

## ✅ Features

- Recursively organizes files in a directory and its subdirectories
- Categorizes files by extension (via customizable dictionary)
- Skips creating duplicate folders
- Easy to modify and extend

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/hiteshtg/Declutterer.git
cd Declutterer
```

### 2. Make sure Python is installed

Check with:
```bash
python3 --version
```

### 3. Customize your file extension mapping

Open `helper.py` and edit the dictionary:

```python
ext_dict = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Images": [".jpg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv"],
    "Archives": [".zip", ".tar.gz", ".rar"],
    # Add more categories as needed
}
```

### 4. Run the script

Set the `path` variable inside `main.py` to your target directory and run or add path:

```bash
python3 main.py path
```

---

## 💡 Example

If you set `path="/home/hitesh/.config/"` and run the script, files will be organized into folders like this:

```
/home/hitesh/.config/
├── Documents/
│   └── notes.txt
├── Images/
│   └── wallpaper.png
└── ...
```

---

## 🔧 Planned Features

- [ ] `--dry-run` flag to preview changes
- [ ] `--verbose` mode for detailed output
- [ ] Command-line support for input directory
- [ ] Logging support for audit trail

---

## 🧠 Contributing

Feel free to fork, clone, and send pull requests! You can help with:
- Adding command-line flags
- Improving performance
- Creating a GUI wrapper (maybe with Tkinter or Flask)

---

## 📄 License

This project is licensed under the MIT License.

---

**Made with ❤️ by Hitesh**
