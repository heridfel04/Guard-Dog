
import sqlite3
import os
from send_email import send_alert  # Import the email alert function
from fingerprint import get_file_hash

def check_files():
    conn = sqlite3.connect("file_hashes.db")
    cursor = conn.cursor()

    folder = r"C:\Users\leopa\OneDrive\Desktop"  # Your folder path

    # Check for new/modified files
    for file in os.listdir(folder):
        filepath = os.path.join(folder, file)
        if os.path.isfile(filepath):
            current_hash = get_file_hash(filepath)
            cursor.execute("SELECT hash FROM hashes WHERE filename=?", (filepath,))
            old_hash = cursor.fetchone()

            if not old_hash:
                # New file added
                send_alert(f" New file added: {filepath}")
            elif old_hash[0] != current_hash:
                # File modified
                send_alert(f" File modified: {filepath}")

    # Check for deleted files
    cursor.execute("SELECT filename FROM hashes")
    saved_files = [row[0] for row in cursor.fetchall()]
    for saved_file in saved_files:
        if not os.path.exists(saved_file):
            send_alert(f" File deleed: {saved_file}")

    conn.close()

# Run the check
check_files()