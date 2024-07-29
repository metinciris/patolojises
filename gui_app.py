import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import sounddevice as sd
import wavio
import os
import numpy as np
import threading

# Ses kaydı için ayarlar
samplerate = 16000  # Örnekleme hızı
project_folder = "project"
config_file = "config.txt"
log_file = "log.txt"

# Kullanıcı adını kontrol et ve yapılandırma dosyasına kaydet
if not os.path.exists(config_file):
    user_id = simpledialog.askstring("Input", "Enter your user ID (2 characters):")
    if len(user_id) != 2:
        raise ValueError("User ID must be exactly 2 characters long")
    with open(config_file, "w") as f:
        f.write(user_id)
else:
    with open(config_file, "r") as f:
        user_id = f.read().strip()

# Kullanıcı klasörünü oluşturma
user_folder = os.path.join(project_folder, user_id)
audio_folder = os.path.join(user_folder, "audio_files")
transcription_folder = os.path.join(user_folder, "transcriptions")
example_reports_folder = os.path.join(user_folder, "example_reports")
os.makedirs(audio_folder, exist_ok=True)
os.makedirs(transcription_folder, exist_ok=True)
os.makedirs(example_reports_folder, exist_ok=True)

# Mevcut en yüksek dosya numarasını bulun
def get_next_file_number():
    files = os.listdir(audio_folder)
    if not files:
        return 1
    numbers = [int(f.split(".")[0].split("_")[1]) for f in files if f.endswith(".wav")]
    return max(numbers) + 1 if numbers else 1

next_file_number = get_next_file_number()
is_recording = False
audio_data = []

def start_recording():
    global is_recording, audio_data
    if not is_recording:
        is_recording = True
        audio_data = []
        threading.Thread(target=record_audio).start()

def record_audio():
    global audio_data
    with sd.InputStream(samplerate=samplerate, channels=1, callback=audio_callback):
        while is_recording:
            sd.sleep(100)

def stop_recording():
    global is_recording
    is_recording = False
    save_recording()

def audio_callback(indata, frames, time, status):
    audio_data.append(indata.copy())

def save_recording():
    global next_file_number
    filename = f"{user_id}_{next_file_number}.wav"
    audio_path = os.path.join(audio_folder, filename)
    wavio.write(audio_path, np.concatenate(audio_data), samplerate, sampwidth=2)
    next_file_number += 1
    log_transcription(filename, audio_path)

def log_transcription(audio_filename, audio_path):
    transcription_filename = os.path.splitext(audio_filename)[0] + ".txt"
    transcription_path = os.path.join(transcription_folder, transcription_filename)
    transcription_text = simpledialog.askstring("Input", f"Enter the transcription text for {audio_filename}:")
    if transcription_text:
        with open(transcription_path, "w", encoding="utf-8") as f:
            f.write(transcription_text)
        with open(log_file, "a", encoding="utf-8") as log:
            log.write(f"{audio_filename},{transcription_filename}\n")
        messagebox.showinfo("Info", f"Saved audio file to: {audio_path}\nSaved transcription to: {transcription_path}")

def list_unsent_files():
    sent_files = set()
    if os.path.exists(log_file):
        with open(log_file, "r", encoding="utf-8") as log:
            for line in log:
                audio_filename, transcription_filename = line.strip().split(",")
                if os.path.exists(os.path.join(audio_folder, audio_filename)):
                    sent_files.add(audio_filename)
    all_files = set(os.listdir(audio_folder))
    unsent_files = all_files - sent_files
    return unsent_files

def delete_file(filename):
    audio_path = os.path.join(audio_folder, filename)
    transcription_path = os.path.join(transcription_folder, os.path.splitext(filename)[0] + ".txt")
    if os.path.exists(audio_path):
        os.remove(audio_path)
    if os.path.exists(transcription_path):
        os.remove(transcription_path)
    messagebox.showinfo("Info", f"Deleted {filename} and its transcription.")

def show_unsent_files():
    unsent_files = list_unsent_files()
    if unsent_files:
        unsent_list = "\n".join(unsent_files)
        messagebox.showinfo("Unsent Files", f"Unsent files:\n{unsent_list}")
    else:
        messagebox.showinfo("Unsent Files", "No unsent files.")

def delete_file_prompt():
    filename_to_delete = simpledialog.askstring("Input", "Enter the filename to delete:")
    if filename_to_delete:
        delete_file(filename_to_delete)

def import_from_cloud():
    cloud_folder = filedialog.askdirectory(title="Select Cloud Folder")
    if cloud_folder:
        for file in os.listdir(cloud_folder):
            if file.endswith(".wav") or file.endswith(".txt"):
                file_path = os.path.join(cloud_folder, file)
                destination_path = os.path.join(audio_folder if file.endswith(".wav") else transcription_folder, file)
                os.rename(file_path, destination_path)
                messagebox.showinfo("Info", f"Imported {file} from cloud folder")

# GUI Kurulumu
root = tk.Tk()
root.title("Audio Recorder")

start_button = tk.Button(root, text="Start Recording", command=start_recording)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Recording", command=stop_recording)
stop_button.pack(pady=10)

unsent_button = tk.Button(root, text="List Unsent Files", command=show_unsent_files)
unsent_button.pack(pady=10)

delete_button = tk.Button(root, text="Delete File", command=delete_file_prompt)
delete_button.pack(pady=10)

import_button = tk.Button(root, text="Import from Cloud", command=import_from_cloud)
import_button.pack(pady=10)

root.mainloop()
