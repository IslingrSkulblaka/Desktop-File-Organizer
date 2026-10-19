import os
import shutil
import time
from datetime import datetime

# ==========================================
# CONFIGURATION
# ==========================================

# Defines all major system folders to clean up
TARGET_DIRECTORIES = [
    os.path.expanduser("~/Downloads"),
    os.path.expanduser("~/Documents"),
    os.path.expanduser("~/Desktop"),
    os.path.expanduser("~/Pictures")
]

# Comprehensive mapping of major file types
EXTENSION_MAP = {
    # Documents
    '.pdf': 'Documents/PDFs',
    '.docx': 'Documents/Word_Docs',
    '.doc': 'Documents/Word_Docs',
    '.txt': 'Documents/Text_Files',
    '.xlsx': 'Documents/Excel_Sheets',
    '.csv': 'Documents/Excel_Sheets',
    '.pptx': 'Documents/Presentations',
    
    # Images
    '.jpg': 'Pictures/Photos',
    '.jpeg': 'Pictures/Photos',
    '.png': 'Pictures/Photos',
    '.gif': 'Pictures/GIFs',
    '.svg': 'Pictures/Vectors',
    '.heic': 'Pictures/Photos',
    
    # Videos
    '.mp4': 'Videos',
    '.mov': 'Videos',
    '.avi': 'Videos',
    
    # Audio
    '.mp3': 'Audio',
    '.wav': 'Audio',
    
    # Archives/Code
    '.zip': 'Archives',
    '.tar': 'Archives',
    '.gz': 'Archives',
    '.py': 'Developer/Python',
    '.js': 'Developer/JavaScript',
    '.json': 'Developer/Data',
}

# Timer interval in seconds (60 seconds)
LOOP_INTERVAL_SECONDS = 60

# ==========================================
# CORE LOGIC
# ==========================================

def organize_directory(target_dir):
    if not os.path.exists(target_dir):
        return

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Scanning: {target_dir}")
    
    for filename in os.listdir(target_dir):
        file_path = os.path.join(target_dir, filename)
        
        # Skip directories to prevent moving folders inside folders infinitely
        if os.path.isdir(file_path):
            continue
            
        # Extract extension
        _, extension = os.path.splitext(filename)
        extension = extension.lower()
        
        # Ignore hidden system files (like .DS_Store on Mac or desktop.ini on Windows)
        if filename.startswith('.'):
            continue

        # Fallback to an 'Others' folder if the extension is unknown
        if extension in EXTENSION_MAP:
            subfolder_path = EXTENSION_MAP[extension]
        else:
            subfolder_path = 'Others/Unsorted'

        # Build destination path inside the CURRENT scanning folder
        destination_dir = os.path.join(target_dir, subfolder_path)
        
        # Handle edge case: Don't move a file into an 'Others' folder if it's already inside one
        if subfolder_path.split('/')[0] in file_path:
            continue

        # Create the subfolder hierarchy if it doesn't exist
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
            
        # Safely move the file
        try:
            destination_file_path = os.path.join(destination_dir, filename)
            
            # Avoid overwriting files with the exact same name
            if os.path.exists(destination_file_path):
                name, ext = os.path.splitext(filename)
                destination_file_path = os.path.join(destination_dir, f"{name}_{int(time.time())}{ext}")

            shutil.move(file_path, destination_file_path)
            print(f" -> Moved: {filename} to {subfolder_path}/")
        except Exception as e:
            print(f" -> Error moving {filename}: {e}")

def main():
    print("==================================================")
    print("GLOBAL SYSTEM FILE ORGANIZER STARTED")
    print(f"Monitoring: {', '.join([os.path.basename(d) for d in TARGET_DIRECTORIES])}")
    print(f"Interval loop: Every {LOOP_INTERVAL_SECONDS} seconds. Press Ctrl+C to stop.")
    print("==================================================")
    
    try:
        while True:
            for directory in TARGET_DIRECTORIES:
                organize_directory(directory)
            
            # Sleep for the designated interval
            time.sleep(LOOP_INTERVAL_SECONDS)
            
    except KeyboardInterrupt:
        print("\nOrganizer stopped safely by user.")

if __name__ == "__main__":
    main()