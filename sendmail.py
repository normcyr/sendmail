import yaml, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def load_config(config_file, text_file):

    with open(config_file, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    username = cfg['login']['username']
    password = cfg['login']['password']
    smtp_server = cfg['server']

    from_address = cfg['addresses']['from_address']
    to_address = cfg['addresses']['to_address']

    subject = cfg['msg_info']['subject']

    with open(text_file, 'r') as txtfile:
        announcement = txtfile.read()

    return(username, password, smtp_server, from_address, to_address, subject, announcement)

def build_message(announcement, subject, from_address, to_address):

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address

    body = announcement
    msg.attach(MIMEText(body, 'plain'))

    return(msg)

def send_message(username, password, smtp_server, msg, from_address, to_address):

    server = smtplib.SMTP(smtp_server, 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    send_mail_status = server.sendmail(from_address, to_address, msg.as_string())

    if send_mail_status != {}:
        print('There was a problem sending an email. Error: {}.'.format(send_mail_status))

    server.quit()

def main():

    config_file = 'config.yml'
    text_file = 'announcement.txt'

    username, password, smtp_server, from_address, to_address, subject, announcement = load_config(config_file, text_file)
    msg = build_message(announcement, subject, from_address, to_address)

    send_message(username, password, smtp_server, msg, from_address, to_address)

if __name__ == '__main__':
    main()
