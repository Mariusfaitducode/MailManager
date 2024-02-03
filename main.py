
import mail_manager
import configparser

import interface
import email


# Mail manager
    
config = configparser.ConfigParser()
config.read('config.ini')
    
host = 'imap.gmail.com'
user = config['DEFAULT']['Email']
password = config['DEFAULT']['Password']

mail_manager = mail_manager.MailManager(mail_user=user, mail_password=password)

# mail_manager.login(mail_user=user, mail_password=password)
# mail_manager.get_mailbox()

# try:
#     status, data = mail_manager.mail.fetch(b'11766', '(RFC822)')
#     raw_email = data[0][1]

#     email_message = email.message_from_bytes(raw_email)

#     sender = email.utils.parseaddr(email_message['From'])

#     print(sender)
# except Exception as e:
#     print(e)

# Interface graphique

interface = interface.Interface(mail_manager=mail_manager)
interface.mainloop()

