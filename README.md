# 🔐 Cybersecurity Mini Projects

A collection of beginner-friendly cybersecurity projects built using Python.  
These projects demonstrate foundational security concepts through short, practical examples.

---

## ✅ Projects Included

### 1. Password Strength Checker  
**Folder:** Project-1-Password-Checker  
**Tech Used:** Python  
- Evaluates password strength based on length and character complexity.  
- Run to check password rules (length, uppercase, lowercase, digits, special chars).

### 3. Simple Port Scanner  
**Folder:** Project-3-Port-Scanner  
**Tech Used:** Python (sockets)  
- Scans a small range of ports on a target machine (use localhost or machines you own).  
- Reinforces TCP/IP and port-scanning basics.

### 5. Phishing Email Detector  
**Folder:** Project-5-Phishing-Detector  
**Tech Used:** Python  
- Detects suspicious emails using keyword scoring.  
- Includes sample safe and phishing email text for quick testing.

---

## ✅ How to Run Any Project (Windows 10, VS Code)

1. Open this project folder in VS Code: `File → Open Folder → C:\Users\Shivam Sharma\OneDrive\Desktop\CyberProject`.
2. Open the integrated terminal: `Terminal → New Terminal` (or press `` Ctrl+` ``).
3. (Optional but recommended) Create and activate a virtual environment:
   - Run: `python -m venv venv`
   - Activate: `venv\Scripts\activate`
4. Change to the project folder you want to run, for example:
   - `cd Project-1-Password-Checker`
5. Run the Python script in that folder:
   - `python password_checker.py`
6. For Port Scanner:
   - `cd ..\Project-3-Port-Scanner`
   - `python port_scanner.py`
   - **Important:** Use `127.0.0.1` (localhost) or a machine you own for scanning.
7. For Phishing Detector:
   - `cd ..\Project-5-Phishing-Detector`
   - `python phishing_detector.py`
   - Paste the email text into the terminal and press Enter twice to finish input (or follow on-screen instructions).

---

## ✅ Sample email texts you can use to test the Phishing Detector

**Safe email (expected: Email Seems Safe):**

From: newsletter@techupdates.com

Subject: Weekly Technology Roundup

Hello Reader,

Here is your weekly roundup of the latest trends in technology.
We have included articles on AI, cybersecurity, programming, and cloud computing.

Hope you enjoy reading!

Regards,
Tech Updates Team

**Phishing-style email (expected: Suspicious Email Detected):**

From: security-alert@bankinfo.com

Subject: Urgent: Verify your account now

Dear Customer,

We detected unusual activity on your bank account. Please click the secure link below to verify your login details and update your password immediately to avoid suspension.

Link: http://fakebank.verify/secure

Regards,
Bank Security Team


---

## ✅ Notes & Safety
- Do **not** scan IPs or servers you don't own or have permission to test. Use `127.0.0.1` or test VMs.
- Keep your repository organized: each project in its own folder (as listed above).
- After saving README, you can run `git add README.md && git commit -m "Update README" && git push` to push the change.

---

If you’ve pasted this and saved the file, tell me “Done” and I’ll give you the **exact next single step** (commit + push commands tailored to your repo and username `sharmashivam21`).  
(If anything in the README copy/paste looks wrong on your screen, paste the top 6 lines of your `README.md` here and I’ll correct it.)
