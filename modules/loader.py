# loader.py
def load_list(filepath):
    """
    Loads a text file and returns a clean list of lines.
    Removes extra spaces and empty lines.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f.readlines() if line.strip()]
    except Exception as e:
        raise RuntimeError(f"Could not load file: {filepath}\n{e}")
