import os
import git
import time
import shutil
import tkinter as tk

# Git uygulamasının yolunu belirtin
os.environ['GIT_PYTHON_GIT_EXECUTABLE'] = r'C:\Program Files\Git\bin\git.exe'

# Ayarlar
local_repo_path = 'C:/Users/user/Documents/ses'  # Yerel repo yolu
remote_repo_url = 'https://github.com/metinciris/patolojises.git'  # Uzak repo URL'si
audio_files_folder = os.path.join(local_repo_path, 'project/mc/audio_files')  # Audio files folder
transcriptions_folder = os.path.join(local_repo_path, 'project/mc/transcriptions')  # Transcriptions folder

# GitHub deposunu mevcut yerel depo üzerinden kullan
repo = git.Repo(local_repo_path)

def get_remote_files():
    remote_files = []
    try:
        repo.git.fetch()
        temp_dir = os.path.join(local_repo_path, 'temp_clone')
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        repo.git.clone(remote_repo_url, temp_dir)
        remote_repo = git.Repo(temp_dir)
        for item in remote_repo.tree().traverse():
            if item.type == 'blob':
                remote_files.append(item.path)
        shutil.rmtree(temp_dir)
    except Exception as e:
        print(f"Failed to get remote files: {e}")
    return remote_files

def upload_files(folder_path, target_folder):
    current_files = set()
    for subdir, dirs, files in os.walk(folder_path):
        for file in files:
            relative_path = os.path.relpath(os.path.join(subdir, file), local_repo_path)
            current_files.add(relative_path)

    if current_files:
        print(f"Yeni dosyalar bulundu: {current_files}")
        repo.git.add(all=True)
        repo.index.commit(f"Yeni dosyalar eklendi: {current_files}")

        # Uzak depodan güncellemeleri çek ve birleştir
        try:
            repo.git.pull('origin', 'main', '--rebase')
        except Exception as e:
            print(f"Failed to pull remote changes: {e}")

        # Değişiklikleri uzak depoya gönder
        try:
            repo.git.push("origin", "main")
        except Exception as e:
            print(f"Failed to push changes: {e}")

# GUI kurulumu
def start_upload():
    root.withdraw()
    while True:
        upload_files(audio_files_folder, 'mc/audio_files')
        upload_files(transcriptions_folder, 'mc/transcriptions')
        time.sleep(10)  # 10 saniyede bir kontrol et

root = tk.Tk()
root.withdraw()
start_upload()
