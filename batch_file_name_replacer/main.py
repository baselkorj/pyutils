import os

dir_path = input("Enter directory path: ")
old_text = input("Enter text to replace: ")
new_text = input("Enter new text: ")

for filename in os.listdir(dir_path):
    if old_text in filename:
        new_filename = filename.replace(old_text, new_text)
        os.rename(os.path.join(dir_path, filename), os.path.join(dir_path, new_filename))