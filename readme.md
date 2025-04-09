# Ayuda Scanner
A utility application for batch renaming PDF files within folder structures. Ayuda Scanner helps organize and standardize filenames according to predefined patterns.

## Features
- Folder Scanning: Easily browse and select target directories
- Batch Renaming: Process multiple files at once following naming conventions
- Range Processing: Specify start and end intervals for processing multiple folders
- Name Transformation: Automatically transform filenames with patterns like "Paginas desde2563-1" to standardized formats
- Live Logging: View real-time feedback about renamed files
- User-Friendly Interface: Simple GUI designed for ease of use
## Requirements
Windows operating system
No additional software required (standalone executable)
## Installation
Option 1:Portable Version.

- Download the standalone AyudaScanner.exe file
- Place it in any location of your choice
- Double-click to run the application

## Usage
- Select Folder: Click the "Browse" button to navigate to your target "Carpeta Mes" folder

- Set Interval: Enter the starting and ending folder numbers in "Intervalo Inicio" and "Intervalo Final"

- Run Process: Click "Renombrar Expedientes" to begin the renaming process

- View Results: Check the log area at the bottom of the window for detailed information about the changes made
## Building from Source
### Requirements
- Python 3.6 or higher
- Required packages: tkinter, pyinstaller
### Steps
- Clone the repository
- Install dependencies
- Build the executable
- Find the executable in the dist folder

## Project Structure
### How It Works
The application scans specified folder ranges, looking for PDF files that match certain naming patterns. It then renames these files according to predefined rules stored in the conversion dictionary. The process respects folder structures and provides detailed logging of all changes.

## Notes
- Files are renamed in-place; consider backing up important data before running the tool
- The application is designed to handle Spanish characters and accents
- When selecting folders, make sure you have appropriate permissions
