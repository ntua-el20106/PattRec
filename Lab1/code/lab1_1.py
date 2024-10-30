#       Code for Lab1 - PattRec

import os
import librosa

# Χάρτης για τη μετατροπή των λέξεων σε αριθμούς
digit_map = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def parse_audio_files(directory):
    wav_data = []  # Λίστα για το wav περιεχόμενο
    speakers = []  # Λίστα για τους ομιλητές
    digits = []  # Λίστα για τα ψηφία

    # Διατρέχουμε όλα τα αρχεία στον φάκελο `digits/`
    for filename in os.listdir(directory):
        if filename.endswith(".wav"):
            # Διαβάζουμε το wav αρχείο
            file_path = os.path.join(directory, filename)
            wav, _ = librosa.load(file_path, sr=None)
            wav_data.append(wav)

            filename = os.path.splitext(filename)[0]
            # Διαχωρισμός ψηφίου και ομιλητή από το όνομα αρχείου
            digit_word = "".join([char for char in filename if char.isalpha()])
            speaker_id = "".join([char for char in filename if char.isdigit()])

            # Μετατροπή λέξης ψηφίου σε αριθμό
            digit = digit_map.get(digit_word, None)

            if digit is not None and speaker_id:
                digits.append(digit)
                speakers.append(speaker_id)
            else:
                print(f"Σφάλμα στην επεξεργασία του αρχείου: {filename}")

    return wav_data, speakers, digits


# Χρήση της συνάρτησης
wav_data, speakers, digits = parse_audio_files("../pr_lab2_data/digits")
