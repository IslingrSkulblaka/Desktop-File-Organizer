# Automated Global File Organizer

A AI-assisted, production-ready Python automation utility that continuously monitors major system folders (Downloads, Documents, Desktop, Pictures) and instantly files incoming documents, media, and raw assets into structured sub-directories.

## Features
* Simultaneously watches Desktop, Documents, Pictures, and Downloads.
* Matches over 20+ file extensions to dedicated nested folders.
* Safely isolates unrecognized file formats into an `Others/Unsorted` matrix rather than ignoring them.
* Leverages an efficient event sleep loop running every 60 seconds.
* Automatically appends unique Unix timestamps to duplicate file entries to prevent data erasure.

## Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd global-file-organizer
   ```

2. **Run the Daemon via Terminal:**
   ```bash
   python3 global_file_organizer.py
   ```

3. **To Stop:** 
   Press `Ctrl + C` in the console window.