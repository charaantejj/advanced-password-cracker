# modules/wordlist_attack.py

import hashlib
import time

def crack_hashes_with_wordlist(hash_file_path, wordlist_file_path):
    start_time = time.time()
    cracked = []
    not_found = []

    try:
        with open(hash_file_path, 'r') as f:
            hashes = [line.strip().lower() for line in f if line.strip()]

        with open(wordlist_file_path, 'r', encoding='latin-1') as f:
            words = [line.strip() for line in f if line.strip()]

        results = ["Starting password cracking...\n"]

        for h in hashes:
            match_found = False
            for word in words:
                for algo in [hashlib.md5, hashlib.sha1, hashlib.sha256, hashlib.sha512]:
                    hashed_word = algo(word.encode()).hexdigest()
                    if hashed_word == h:
                        results.append(f"Found:\n{word} for {algo.__name__.upper()} hash: {h}\n")
                        cracked.append(h)
                        match_found = True
                        break
                if match_found:
                    break
            if not match_found:
                results.append(f"No match found for hash: {h}\n")
                not_found.append(h)

        duration = round(time.time() - start_time, 2)
        results.append(f"\nPassword cracking completed in {duration} seconds.")
        results.append(f"Cracked passwords: {len(cracked)}")
        results.append(f"Passwords not found: {len(not_found)}")

        return "\n".join(results)

    except Exception as e:
        return f"Error: {str(e)}"
