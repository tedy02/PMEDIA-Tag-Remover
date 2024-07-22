# PMEDIA-Tag-Remover

Automatically removes PMEDIA's promotional tags from your audio files.


## Features

- Scans your audio files for specific PMEDIA tags:
    - `www.t.me/pmedia_music`
    - `P.M.E.D.I.A`
    - `PMEDIA`

- Automatically removes these tags, leaving your metadata clean.
- Searches the specified directory and all subfolders.
- Progress bar to track the process.
- Logs errors to a file (`metadata_removal_errors.log`).


## Requirements

- Python 3.x
- `mutagen` module
- `tqdm` module


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/tedy02/PMEDIA-Tag-Remover.git
    cd PMEDIA-Tag-Remover
    ```

2. Create a virtual environment (optional, but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```


## Usage

1. **Download:** Get the script from [PMEDIA Tag Remover - GitHub](https://github.com/tedy02/PMEDIA-Tag-Remover).
2. **Run:** Launch the script `pmedia_remover.py`. You'll be prompted for the directory you want to clean. Press `Enter` to use the current directory.
3. **Relax:** The script will find and remove PMEDIA tags. Any errors will be logged to `metadata_removal_errors.log`.

```sh
python pmedia_remover.py
Enter the directory to search: /path/to/your/music
```


## Logging

If errors occur during processing, they will be logged in `metadata_removal_errors.log`.


## Why?

We love PMEDIA's music, but sometimes their promotional tags clutter our audio files. This script keeps things tidy without removing any music!


## Contributing

We're always looking to improve this script!

- **Found a bug?** Please open an issue.
- **Know other PMEDIA tags or unwanted metadata?** Let us know in the comments!
- **Have coding skills?** Feel free to fork the repository and submit pull requests.


## Created by

#### *- The Nite-Side Devs -*
