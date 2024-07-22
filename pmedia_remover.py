import os
import mutagen
from mutagen.easyid3 import EasyID3
from tqdm import tqdm
import logging

def setup_logging(log_filename='metadata_removal_errors.log'):
    logging.basicConfig(
        filename=log_filename,
        level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return log_filename

def remove_keywords_from_tags(directory, keywords):
    total_removals = 0
    files_to_process = []

    # Collect all music files to process first
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith((".mp3", ".flac", ".ogg", ".m4a")):
                files_to_process.append(os.path.join(root, file))

    # Iterate with tqdm for progress bar
    for filepath in tqdm(files_to_process, desc="Processing Files"):
        try:
            audio = mutagen.File(filepath, easy=True)
            if audio is not None:
                modified = False
                for tag in audio:
                    if tag in EasyID3.valid_keys:
                        if isinstance(audio[tag], list):
                            new_values = []
                            for value in audio[tag]:
                                for keyword in keywords:
                                    if keyword.lower() in value.lower():
                                        value = value.replace(keyword, "")
                                        total_removals += 1
                                        modified = True
                                new_values.append(value)
                            audio[tag] = new_values
                        elif isinstance(audio[tag], str):
                            for keyword in keywords:
                                if keyword.lower() in audio[tag].lower():
                                    audio[tag] = audio[tag].replace(keyword, "")
                                    total_removals += 1
                                    modified = True

                if modified:
                    audio.save()

        except mutagen.MutagenError as e:
            logging.error(f"Error reading metadata for {filepath}: {e}")
            continue

    return total_removals

if __name__ == "__main__":
    log_filename = setup_logging()
    default_directory = os.getcwd()
    music_directory = input(f"Enter the directory to search (leave blank for current directory '{default_directory}'): ")

    if not music_directory.strip():
        music_directory = default_directory

    keywords_to_remove = ["www.t.me/pmedia_music", "P.M.E.D.I.A", "PMEDIA"]

    total_removed = remove_keywords_from_tags(music_directory, keywords_to_remove)
    print(f"\nTotal keywords removed: {total_removed}")

    # Check if the log file exists and is not empty
    if os.path.exists(log_filename) and os.path.getsize(log_filename) > 0:
        log_path = os.path.abspath(log_filename)
        print(f"\nErrors were found during the process. Please check the log file at: {log_path}")
    else:
        print("\nNo errors were found during the process.")

# Created by - The Nite-Side Devs -
