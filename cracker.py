import hashlib

# Ye hash kisi system se mila (attacker ko sirf ye pata hota hai)
target_hash = "240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9"
# Ye admin123 ka SHA256 hash hai

with open("passwords.txt", "r") as file:
    for password in file:
        password = password.strip()

        # password ka hash banana
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        print(f"Trying: {password}")

        # compare
        if hashed_password == target_hash:
            print(f"\n[SUCCESS] Password cracked: {password}")
            break
        else:
            print("[FAILED] Password not found")
