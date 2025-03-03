import hashlib

def get_file_hash(filepath):
    with open(filepath, "rb") as f:
        file_data = f.read()
        hash = hashlib.sha256(file_data).hexdigest()  # Generate unique fingerprint
    return hash

# Test it!
file_hash = get_file_hash(r"C:\Users\leopa\OneDrive\Desktop\backend-roadmap.docx")
print("Fingerprint of backend-roadmap.docx:", file_hash)