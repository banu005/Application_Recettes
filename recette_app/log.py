import logging
import os

LOG_FILE = "recette_app.log"

def configurer_logging():
    """Configure le logging pour écrire dans un fichier et sur la console."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(LOG_FILE, encoding='utf-8'),
            logging.StreamHandler() # Affiche aussi dans la console
        ]
    )
    return logging.getLogger("ApplicationRecettes")
