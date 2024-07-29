# yüklenmedi ise şunları yükleyin: 
# yüklenmedi ise şunları cmd komut dosyası ile yükleyin: pip install gitpython
# yüklenmedi ise şunları cmd komut ile yükleyin:  pip install tk
import os
import git
import time
import tkinter as tk
from tkinter import simpledialog

# Git uygulamasının yolunu belirtin
os.environ['GIT_PYTHON_GIT_EXECUTABLE'] = r'C:\Program Files\Git\bin\git.exe'

# Ayarlar
local_repo_path = 'C:/Users/user/Documents/ses'  # Yerel repo yolu
remote_repo_url = 'https://github.com/metinciris/patolojises.git'  # Uzak repo URL'si
project_folder = os.path.join(local_repo_path, 'project')  # Proje klasörü

# Kullanıcı adı al
root = tk.Tk()
root.withdraw()
user_id = simpledialog.askstring("Input", "Enter your user ID (2 characters):")
if len(user_id) != 2:
    raise ValueError("User ID must be exactly 2 characters long")

# Kullanıcı klasörü
user_folder = os.path.join(project_folder, user_id)

# GitHub deposunu mevcut yerel depo üzerinden kullan
repo = git.Repo(local_repo_path)

# Daha önce commit edilmiş dosyaların listesini al
committed_files = [item.a_path for item in repo.index.diff('HEAD')]

def upload_files():
    current_files = set()
    for subdir, dirs, files in os.walk(user_folder):
        for file in files:
            current_files.add(os.path.relpath(os.path.join(subdir, file), local_repo_path))
    new_files = [f for f in current_files if f not in committed_files]

    if new_files:
        print(f"Yeni dosyalar bulundu: {new_files}")
        repo.git.add(all=True)
        repo.index.commit(f"Yeni dosyalar eklendi: {new_files}")
        repo.git.push("origin", "main")
        committed_files.extend(new_files)

# GUI kurulumu
def start_upload():
    root.withdraw()
    while True:
        upload_files()
        time.sleep(10)  # 10 saniyede bir kontrol et

upload_button = tk.Button(root, text="Start Uploading", command=start_upload)
upload_button.pack(pady=10)
root.mainloop()

