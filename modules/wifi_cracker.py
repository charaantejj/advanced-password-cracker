# modules/wifi_cracker.py

import subprocess
import re

def get_saved_wifi_profiles():
    """
    Retrieve all saved Wi-Fi profiles from the system.
    Only works on Windows.
    """
    try:
        output = subprocess.check_output("netsh wlan show profiles", shell=True, text=True)
        profiles = re.findall(r"All User Profile\s*:\s*(.*)", output)
        return [p.strip() for p in profiles]
    except subprocess.CalledProcessError as e:
        return []

def get_wifi_password(profile_name):
    """
    Get the password of a specific Wi-Fi profile.
    """
    try:
        output = subprocess.check_output(
            f'netsh wlan show profile name="{profile_name}" key=clear',
            shell=True,
            text=True
        )
        password_match = re.search(r"Key Content\s*:\s*(.*)", output)
        return password_match.group(1).strip() if password_match else "(Password not found)"
    except subprocess.CalledProcessError:
        return "(Access denied or profile error)"

def crack_wifi():
    """
    Main function that lists all profiles and their passwords.
    """
    profiles = get_saved_wifi_profiles()
    if not profiles:
        return "❌ No saved Wi-Fi profiles found or access denied."

    results = []
    for profile in profiles:
        password = get_wifi_password(profile)
        results.append(f"📶 SSID: {profile}\n🔑 Password: {password}\n{'-' * 40}")

    return "\n".join(results)
