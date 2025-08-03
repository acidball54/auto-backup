import os
import json
from utils import load_config, setup_logger, zip_folder
from file_hasher import hash_directory
import logging

HASH_RECORD_FILE = 'hash_record.json'

def load_previous_hashes():
    """Load previous hashes from a JSON file."""
    if os.path.exists(HASH_RECORD_FILE):
        with open(HASH_RECORD_FILE, 'r') as file:
            return json.load(file)
    return None

def save_current_hashes(hashes):
    """Save current hashes to a JSON file."""
    with open(HASH_RECORD_FILE, 'w') as file:
        json.dump(hashes, file)
        
        
def main():
    config = load_config()
    setup_logger(config['log_file'])
    
    src_dir = config['source_folder']
    dest_dir = config['backup_folder']
    os.makedirs(dest_dir, exist_ok=True)
    
    logging.info(f"checking for changes in {src_dir}")
    current_hash = hash_directory(src_dir)
    last_hashes = load_previous_hashes()
    
    if current_hash == last_hashes:
        logging.info("No changes detected, skipping backup.")
        return
    else:
        zip_path = zip_folder(src_dir, dest_dir)
        save_current_hashes(current_hash)
        logging.info(f"Backup created at {zip_path}")

if __name__ == "__main__":
    main()
    