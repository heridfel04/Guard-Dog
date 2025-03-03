import os
import sqlite3
from fingerprint import get_file_hash

# 1. Connect to a database
conn = sqlite3.connect("file_hashes.db")
cursor = conn.cursor()

# 2. Create a table to store hashes
cursor.execute('''CREATE TABLE IF NOT EXISTS hashes 
                  (filename TEXT, hash TEXT)''')

# 3. Scan a folder and save hashes
folder = r"C:\Users\leopa\OneDrive\Desktop"
for file in os.listdir(folder):
    filepath = os.path.join(folder, file)
    if os.path.isfile(filepath):
        hash = get_file_hash(filepath)
        cursor.execute("INSERT INTO hashes VALUES (?, ?)", (filepath, hash))

conn.commit()
conn.close()
print("Baseline saved!")