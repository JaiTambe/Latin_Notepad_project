# Latin Notepad

## Description
Latin Notepad is a user-friendly application that allows users to translate Latin words into English. The app uses the deep-translator library for online translations and provides an offline dictionary fallback for common Latin words. Built with tkinter, it features a real-time notepad interface where the latest word typed is automatically translated.

## Features
- *Online Translation*: Translates Latin words to English using GoogleTranslator from the deep-translator library.
- *Offline Dictionary*: Provides translations for common Latin words even when offline.
- *Real-Time Updates*: Automatically translates the last word typed after a short delay.
- *Notepad UI*: A simple and clean interface for typing and viewing translations.
- *Clear Button*: Option to reset the text area for new inputs.

## Prerequisites
To run this project, you need:
- Python 3.7 or higher
- Required libraries:
  - tkinter (comes pre-installed with Python)
  - deep-translator (install using pip)

## Installation
Follow these steps to set up and run the project:

1. Clone the repository to your computer:
   ```bash
   git clone https://github.com/JaiTambe/LatinNotepad.git
   cd LatinNotepad
   
2. Install the required libraries:
   pip install -r requirements.txt

   For Ubuntu/Debian:
   sudo apt-get install python3-tk

   For Windows/Mac:
   sudo dnf install python3-tkinter

   pip install deep-translator

   
4. Run the application:
   python latin_notepad.py

## Usage
1. Type in English in the text area. Whenever a Latin word is typed, the app will automatically display the English translation of that word at the bottom of the screen.
2. The translation updates in real time as you type, showing the meaning of any Latin word encountered.
3. Use the "Clear" button to reset the text area for a new session.

- Example
- Input = Jai tambe believes in power of veritas
- Output = veritas : truth

## Screenshots
![Screenshot from 2024-11-23 14-37-42](https://github.com/user-attachments/assets/cb63f9d9-3662-4b21-81c0-52ed210c64cc)


## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- *Deep Translator*: For providing the translation service used in this app.
- *Tkinter*: For the GUI framework used to build the notepad.
- *Python Community*: For their continuous support and helpful resources.
- Special thanks to *Dr. Yerriswamy T* for reviewing the code and providing valuable suggestions.

