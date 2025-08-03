import hashlib
import os

def hash_file(file_path):
    """Generate SHA-256 hash of the file at the given path."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        """Read the file in chunks to avoid memory issues with large files."""
        while chunk := file.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def hash_directory(directory_path):
    """Generate a combined SHA-256 hash of all files in the directory."""
    hashes = []
    for root, _, files in os.walk(directory_path):
        for file in sorted(files):
            file_path = os.path.join(root, file)
            try:
                hashes.append(hash_file(file_path))
            except Exception:
                pass
    combined = ''.join(hashes).encode('utf-8')
    return hashlib.sha256(combined).hexdigest()