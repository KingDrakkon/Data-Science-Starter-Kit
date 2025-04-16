import os

folder_path = "C:\\Users\\nie27\\Documents\\GitHub\\Data-Science-Starter-Kit"

if os.path.exists(folder_path):
    print("✅ Folder exists!")
    print("Contents:", os.listdir(folder_path))
else:
    print("❌ Folder not found.") 