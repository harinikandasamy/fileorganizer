import os
from pathlib import Path

# Define the list of file formats and their corresponding directories
file_formats = {
    "Images": [".jpeg", ".jpg", ".gif", ".png"],
    "Videos": [".wmv", ".mov", ".mp4", ".avi"],
    "Documents": [".pdf"],
    "Others": []  # Default for files that don't match any format
}


# Function to organize files
def organize_files(source_folder, target_folder):
    for entry in os.scandir(source_folder):
        if entry.is_file():
            file_path = Path(entry)
            file_extension = file_path.suffix.lower()

            target_dir = target_folder / "Others"
            for category, extensions in file_formats.items():
                if file_extension in extensions:
                    target_dir = target_folder / category
                    break

            target_dir.mkdir(parents=True, exist_ok=True)
            target_file_path = target_dir / file_path.name

            os.rename(file_path, target_file_path)
            print(f"Moved '{file_path}' to '{target_file_path}'")


if __name__ == "__main__":
    source_folder = Path(input("Enter the source folder path: "))
    target_folder = Path(input("Enter the target folder path: "))

    organize_files(source_folder, target_folder)
