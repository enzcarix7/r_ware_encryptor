# 🔐 AES File Encryptor

Simple Python script to **encrypt and decrypt `.*` files** in a given folder using **AES-256 in CBC mode**.  
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
### 🔐 Encrypt all `.*` files in a folder
```
python3 rwarev2.py encrypt <folder_path>
```
Decrypt all .* files in a folder
```
python3 rwarev2.py decrypt <folder_path>
```

🛠️ Requirements
Install dependencies via pip:
```
pip install pycryptodome
```

```
⚠️ Notes
• The script stores the IV and Salt directly in the encrypted file.
• Original files are NOT deleted by default. If you want to auto-remove original files after encryption/decryption, just uncomment the remove() lines in the script.
• Decrypted files will have the .dec extension, original names are not restored.
• The script encrypts all files except those with the .enc extension.
```

📁 Example
Given this folder structure:

```
Before running:
/docs
  ├── test1.txt
  ├── test2.txt
  └── test.png.enc

After running (enc):
/docs
  ├── test1.txt.enc
  ├── test2.txt.enc
  └── test3.png.enc

After running (dec):
/docs
  ├── test1.txt.enc
  ├── test2.txt.enc
  └── test.png.enc
```


⚠️ DISCLAIMER
This project is provided for educational and research purposes only.
The author does not take any responsibility for:
• Misuse of the script
• Data loss
• Encrypted files being unrecoverable due to forgotten passwords
• Any damages caused by running or modifying this code

By using this software, you agree to use it at your own risk.
No guarantees are made regarding security, performance, or suitability for any specific task.

Do not use this tool on systems or data you do not own or have explicit permission to access.

```
Made with ❤️
```
