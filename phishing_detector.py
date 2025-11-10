def detect_phishing(email_text):
    phishing_keywords = ["password", "bank", "urgent", "verify", "click", "login", "account", "update"]
    score = 0
    for word in phishing_keywords:
        if word.lower() in email_text.lower():
            score += 1

    if score >= 2:
        return "⚠ Suspicious Email Detected"
    else:
        return "✅ Email Seems Safe"

if __name__ == "__main__":
    print("Paste email content (press Enter twice when done):")
    email_lines = ["""
                   From: newsletter@techupdates.com
Subject: Weekly Technology Roundup

Hello Reader,

Here is your weekly roundup of the latest trends in technology.
We have included articles on AI, cybersecurity, programming, and cloud computing.
Hope you enjoy reading!

Regards,
Tech Updates Team


"""]
    try:
        while True:
            line = input()
            if line == "":
                break
            email_lines.append(line)
    except EOFError:
        pass
    email_text = "\n".join(email_lines)
    print(detect_phishing(email_text))
