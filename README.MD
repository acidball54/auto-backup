# auto-backup

A Python-based automated backup tool.

## Features

- Monitors specified directories for changes.
- Automatically creates backups of files and folders.
- Supports scheduling backups at custom intervals.
- Stores backups in a user-defined location.
- Maintains backup history for easy restoration.
- Logs backup activities for tracking and troubleshooting.

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/acidball54/auto-backup.git
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Configure directories and backup settings in `config.yml`.
4. Run the backup tool:
    ```bash
    python main.py
    ```

## Configuration

Edit `config.json` to specify:
- Source directories to monitor.
- Backup destination path.
- Backup schedule (interval in minutes/hours).
- Number of backup versions to keep.

## License

MIT License

---

Maintained by [acidball54](https://github.com/acidball54)