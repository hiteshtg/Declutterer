import os

def check_dir(path :str):
    list_path = ["Downloads", "Pictures", "Music", "Documents", "Videos", "Archives"]

    for i in list_path:
        if os.path.isdir(os.path.join(path, i)):
            continue
        else:
            os.mkdir(os.path.join(path, i))

    print(f"All directory are present if not Created")

document_exts = [".pdf", ".doc", ".docx", ".txt", ".odt", ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".rtf", ".md", ".epub"]
image_exts = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg", ".ico", ".heic"]
audio_exts = [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma", ".opus", ".amr"]
video_exts = [".mp4", ".mkv", ".mov", ".avi", ".flv", ".wmv", ".webm", ".3gp", ".mpeg", ".ts"]
archive_exts = [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso", ".lz", ".ar", ".zst"]
executable_exts = [".exe", ".msi", ".sh", ".bat", ".cmd", ".appimage", ".apk", ".jar", ".bin", ".run"]

ext_dict = {
    "Downloads" : executable_exts,
    "Pictures" : image_exts,
    "Music" : audio_exts,
    "Videos" : video_exts,
    "Documents" : document_exts,
    "Archives" : archive_exts
}
