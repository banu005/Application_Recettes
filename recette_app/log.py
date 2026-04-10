import logging

LOG_FILE = "recette_app.log"

def configurer_logging(verbose=False):
    """
    Configure le logging pour écrire dans un fichier et sur la console.
    Si verbose=True (option --verbose), le niveau console passe en DEBUG.
    """
    logger = logging.getLogger("ApplicationRecettes")
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Handler fichier : toujours en INFO
    file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # Handler console : DEBUG si verbose, WARNING sinon
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG if verbose else logging.WARNING)
    console_handler.setFormatter(formatter)

    # Évite d'ajouter plusieurs handlers si la fonction est appelée plusieurs fois
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger