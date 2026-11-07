# MailManager

A small desktop app to clean up a Gmail inbox: it groups recent e-mails by sender and lets you delete everything from one sender in a single click.

## What it does
- Connects to Gmail over IMAP with your address and a Google app password.
- Scans the last N messages of the inbox (you choose N) and groups them by sender address.
- Lists senders sorted by number of e-mails, which quickly surfaces newsletters, notifications and spam.
- Deletes all scanned e-mails from a sender with one "Supprimer" (delete) button.
- Dark-mode interface built with customtkinter, with a progress bar during the scan.

## Tech stack
Python, `imaplib`, `email`, customtkinter.

## Run it locally
1. Create a Google [app password](https://myaccount.google.com/apppasswords) for your account.
2. Create a `config.ini` next to `main.py` (it is git-ignored) to pre-fill the login form:
   ```ini
   [DEFAULT]
   Email = you@gmail.com
   Password = your-app-password
   ```
3. Install and run:
   ```bash
   pip install customtkinter
   python main.py
   ```
The interface is in French.

## Context
Personal side project from January 2024, built to make occasional inbox clean-ups faster. Only Gmail is supported for now.
