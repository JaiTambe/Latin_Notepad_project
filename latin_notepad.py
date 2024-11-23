import tkinter as tk
from deep_translator import GoogleTranslator
import threading

# Offline dictionary for Latin-English as a fallback
offline_dictionary = {
    "amor": "love",
    "bellum": "war",
    "caelum": "sky",
    "carpe": "seize",
    "corpus": "body",
    "cura": "care",
    "deus": "god",
    "dies": "day",
    "dominus": "lord",
    "ego": "I",
    "et": "and",
    "fides": "faith",
    "fortis": "strong",
    "gloria": "glory",
    "gratia": "grace",
    "homo": "man",
    "ignis": "fire",
    "in": "in",
    "lux": "light",
    "magna": "great",
    "mors": "death",
    "natura": "nature",
    "nihil": "nothing",
    "nomen": "name",
    "novus": "new",
    "oculus": "eye",
    "omnis": "all",
    "pax": "peace",
    "populus": "people",
    "rex": "king",
    "sacer": "sacred",
    "scientia": "knowledge",
    "sol": "sun",
    "spes": "hope",
    "tempus": "time",
    "terra": "earth",
    "veritas": "truth",
    "vita": "life",
    "vox": "voice",
    "aqua": "water",
    "ars": "art",
    "aurum": "gold",
    "beneficium": "benefit",
    "causa": "cause",
    "civitas": "state",
    "clarus": "clear",
    "consilium": "plan",
    "cura": "care",
    "dignus": "worthy",
    "dolor": "pain",
    "felix": "happy",
    "fuga": "flight",
    "honor": "honor",
    "humanus": "human",
    "imperium": "power",
    "ius": "law",
    "libertas": "freedom",
    "locus": "place",
    "miles": "soldier",
    "modus": "manner",
    "mons": "mountain",
    "munus": "duty",
    "natura": "nature",
    "numerus": "number",
    "onus": "burden",
    "pars": "part",
    "patria": "homeland",
    "primus": "first",
    "proelium": "battle",
    "puella": "girl",
    "puer": "boy",
    "res": "thing",
    "sanctus": "holy",
    "servus": "slave",
    "somnus": "sleep",
    "soror": "sister",
    "stella": "star",
    "studium": "study",
    "urbs": "city",
    "verbum": "word",
    "via": "road",
    "vinum": "wine",
    "virtus": "virtue",
    "voluntas": "will",
    "ad": "to",
    "cum": "with",
    "de": "about",
    "ex": "from",
    "per": "through",
    "pro": "for",
    "sub": "under",
    "super": "above",
    "trans": "across"
}

# Initialize the translator
translator = GoogleTranslator(source='latin', target='english')

# Global debounce timer
debounce_timer = None

def translate_word(word):
    """
    Translate a Latin word using online translator first,
    then fallback to offline dictionary if online fails.
    """
    try:
        # Attempt online translation
        translation = translator.translate(word)
        if translation and translation != word:
            return translation
    except Exception:
        pass  # Fallback to offline dictionary
    
    # Use offline dictionary as a fallback
    return offline_dictionary.get(word, None)

def perform_translation(latest_word):
    """
    Perform the translation in a background thread and update the UI.
    """
    translation = translate_word(latest_word)
    if translation:
        meaning_label.config(text=f"{latest_word}: {translation}")
    else:
        meaning_label.config(text="")  # Leave the label blank if no translation is found

def on_key_release(event):
    """
    Trigger translation after a debounce delay.
    """
    global debounce_timer

    # Cancel any existing timer
    if debounce_timer:
        root.after_cancel(debounce_timer)

    # Start a new timer to trigger the translation
    debounce_timer = root.after(300, trigger_translation)

def trigger_translation():
    """
    Extract the latest word and start a translation in a separate thread.
    """
    content = text_area.get("1.0", tk.END).strip().split()
    if content:
        latest_word = content[-1].strip(".,;!?")
        threading.Thread(target=perform_translation, args=(latest_word,), daemon=True).start()
    else:
        meaning_label.config(text="")

def clear_text_area():
    """
    Clear the text area and reset the meaning label.
    """
    text_area.delete("1.0", tk.END)
    meaning_label.config(text="")

# Set up the main application window
root = tk.Tk()
root.title("Latin Notepad")
root.geometry("600x500")

# Text area for typing Latin words/phrases
text_area = tk.Text(root, wrap="word", font=("Arial", 12))
text_area.pack(expand=True, fill="both")
text_area.bind("<KeyRelease>", on_key_release)

# Meaning label for displaying translations
meaning_label = tk.Label(root, text="", font=("Arial", 14), fg="blue", anchor="w", justify="left", height=3)
meaning_label.pack(side="bottom", anchor="w", fill="x")

# Clear button to reset the text area
clear_button = tk.Button(root, text="Clear", font=("Arial", 12), command=clear_text_area)
clear_button.pack(side="top", anchor="ne", padx=10)

root.mainloop()