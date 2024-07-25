import os
from mutagen.id3 import ID3, TXXX, error
from tqdm import tqdm

def clean_metadata(file_path):
    try:
        audio = ID3(file_path)
        keywords = ["www.t.me/pmedia_music", "P.M.E.D.I.A", "PMEDIA"]
        removal_count = 0

        for frame in audio.values():
            if isinstance(frame, TXXX):
                original_value = frame.text[0]
                for keyword in keywords:
                    if keyword in original_value:
                        frame.text[0] = original_value.replace(keyword, '')
                        removal_count += 1

        audio.save(v2_version=3)  # Ensure the changes are saved properly
        return removal_count, None
    except Exception as e:
        return 0, str(e)

def main(directory):
    error_log = []

    audio_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(('.mp3', '.flac', '.ogg', '.m4a'))]
    progress_bar = tqdm(audio_files, desc="Processing Files", unit="file")
    total_removals = 0

    for audio_file in progress_bar:
        removals, error_message = clean_metadata(audio_file)
        total_removals += removals
        if error_message:
            error_log.append(f"Error processing {audio_file}: {error_message}")

    print(f"Total removals: {total_removals}")

    if error_log:
        with open(os.path.join(directory, "error_log.txt"), "w") as log_file:
            log_file.write("\n".join(error_log))

if __name__ == "__main__":
    directory = input("Enter the directory containing the audio files: ")
    main(directory)
    
# - The Nite-Side Devs -
