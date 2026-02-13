  Hash-Based Password Cracker (Python)

  Project Overview
This project demonstrates how attackers attempt to crack passwords when only the hashed value is available. 
Instead of knowing the actual password, a wordlist-based brute force technique is used to compare hashes.

  What I Learned
- How password hashing works using SHA-256
- Why systems store hashes instead of plaintext passwords
- How wordlist attacks are performed
- Importance of strong passwords and hashing

  Technologies Used
- Python
- hashlib (SHA-256)

 How It Works
1. A target SHA-256 hash is provided
2. Passwords are read from a wordlist
3. Each password is hashed and compared
4. If hashes match, the password is cracked

 Usage
```bash
python hash_cracker.py
