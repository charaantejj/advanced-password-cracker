# modules/ntlm_cracker.py

import hashlib

def crack_ntlm_hash(hash_value, wordlist_path):
    try:
        with open(wordlist_path, 'r', encoding='utf-8') as f:
            passwords = f.read().splitlines()

        for password in passwords:
            ntlm_hash = hashlib.new('md4', password.encode('utf-16le')).hexdigest()
            if ntlm_hash.lower() == hash_value.lower():
                return f"Password found: {password}"

        return "Password not found in wordlist."

    except Exception as e:
        return f"Error: {e}"
