
import mail_manager
import configparser

import interface


# Mail manager
    
config = configparser.ConfigParser()
config.read('config.ini')
    
host = 'imap.gmail.com'
user = config['DEFAULT']['Email']
password = config['DEFAULT']['Password']

mail_manager = mail_manager.MailManager(mail_user=user, mail_password=password)


# Interface graphique

interface = interface.Interface(mail_manager=mail_manager)
interface.mainloop()

