
import imaplib
import email
import configparser

class MailManager:

    def __init__(self, mail_host='imap.gmail.com', mail_user='', mail_password=''):
        self.mail_host = mail_host
        self.mail_user = mail_user
        self.mail_password = mail_password
        pass


    def login(self, mail_user, mail_password):
        
        print(f"Logging in as {mail_user}")
        
        self.mail_user = mail_user
        self.mail_password = mail_password

        self.mail = imaplib.IMAP4_SSL(self.mail_host)

        self.mail.login(mail_user, mail_password)

        print("Login successful!")


    def logout(self):
        print("Logging out")
        self.mail.logout()
        print("Logged out successfully!")


    def get_mailbox(self):
        print("Getting mailbox")
        self.mail.select("inbox")
        print("Mailbox retrieved successfully!")

        status, messages = self.mail.search(None, "ALL")

        self.messages = messages[0].split()

        print(f"Found {len(self.messages)} messages")

        return self.messages
    

    def analyse(self, count=50):

        messages = self.get_mailbox()

        list = {}

        print(f"Analyzing {count} messages")
        for num in messages[-count:]: 

            # print(f"Analyzing message {num}")
            status, data = self.mail.fetch(num, '(RFC822)')
            raw_email = data[0][1]

            email_message = email.message_from_bytes(raw_email)
            
            sender = email.utils.parseaddr(email_message['From'])

            print(sender)
            sender = sender[1]

            if sender not in list:
                list[sender] = []

            list[sender].append(num)

        return list