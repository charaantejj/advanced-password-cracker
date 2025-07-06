# modules/rainbow_table.py

import json
import hashlib

def rainbow_crack(hash_value, rainbow_file='rainbow_table.json'):
    try:
        with open(rainbow_file, 'r') as f:
            rainbow_table = json.load(f)
    except FileNotFoundError:
        return "Rainbow table not found."
    except json.JSONDecodeError:
        return "Rainbow table file is corrupted."

    for algo in ['md5', 'sha1', 'sha256']:
        for password, hash_dict in rainbow_table.items():
            hashed = hash_dict.get(algo)
            if hashed and hashed.lower() == hash_value.lower():
                return f"Password found: {{'original_password': '{password}', 'hash_algorithm': '{algo.upper()}'}}"

    return "Password not found in rainbow table."
