# 🔐 AES File Encryptor

Simple Python script to **encrypt and decrypt `.txt` files** in a given folder using **AES-256 in CBC mode**.  
Password-based key derivation with PBKDF2 ensures strong protection.

## 💡 Features
- AES-256 encryption (CBC mode)
- Random IV and Salt for every file
- Password-based key derivation using PBKDF2
- Chunked file processing (safe for large files)
- Only `.txt` files are encrypted
- Encrypted files get `.enc` extension
- Decrypted files get `.dec` extension

## 🚀 Usage
### 🔐 Encrypt all `.txt` files in a folder
```bash
python3 encryptor.py encrypt <folder_path>
```
Decrypt all .txt files in a folder
```bash
python3 decrypt.py encrypt <folder_path>
```

🛠️ Requirements

Install dependencies via pip:
pip install pycryptodome

⚠️ Notes
	•	The script stores the IV and Salt directly in the encrypted file.
	•	Original files are NOT deleted by default. If you want to auto-remove original files after encryption/decryption, just uncomment the remove() lines in the script.
	•	Decrypted files will have the .dec extension — original names are not restored.
	•	Only files ending in .txt will be encrypted (you can modify this behavior easily in the code).

📁 Example

Given this folder structure:
```bash
/docs
  ├── secret1.txt
  ├── secret2.txt
  └── image.png

After running:
/docs
  ├── secret1.txt.enc
  ├── secret2.txt.enc
  └── image.png
```


⚠️ DISCLAIMER

This project is provided for educational and research purposes only.

The author does not take any responsibility for:
	•	Misuse of the script
	•	Data loss
	•	Encrypted files being unrecoverable due to forgotten passwords
	•	Any damages caused by running or modifying this code

By using this software, you agree to use it at your own risk.
No guarantees are made regarding security, performance, or suitability for any specific task.

Do not use this tool on systems or data you do not own or have explicit permission to access.

⸻

Made with ❤️
