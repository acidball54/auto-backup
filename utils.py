import os
import shutil
import datetime
import logging
import yaml


def load_config(config_path="config.yml"):
    """Load configuration from a YAML file."""
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)
    
def setup_logger(log_file):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        filemode='a',
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
def zip_folder(source_folder, output_folder):
    """Compress a folder into a zip file."""
    date_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = f"backup_{date_str}.zip"
    zip_path = os.path.join(output_folder, zip_name)
    shutil.make_archive(zip_path.replace('.zip', ''), 'zip', source_folder)
    return zip_path