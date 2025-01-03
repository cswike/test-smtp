import smtplib
from email.message import EmailMessage

def test_smtp(from_str, to_str, cc_str, subject_str, account, pw):
    msg = EmailMessage()
    msg['From'] = from_str
    msg['To'] = to_str
    msg['CC'] = cc_str
    msg['Subject'] = subject_str

    smtp = smtplib.SMTP('smtp.yoursever.net',587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(account, pw)

    print("Test socket - should NOT get None")
    print(smtp.sock)
    print("==============")
    print("Test noop - should get 250, '2.0.0 OK'")
    print(smtp.noop())
    print("==============")
    print("Sending message")
    smtp.send_message(msg)
    print("==============")
    print("Quit - should get 221 '2.0.0 closing connection'")
    print(smtp.quit()) 
    print("==============")
    print("Test socket - should get None")
    print(smtp.sock)
    print("==============")
    print('Tests complete')

test_smtp(from_str='from-address@yourserver.net',
          to_str='to-address@yourserver.net',
          cc_str='cc-address@yourserver.net',
          subject_str='test email via SMTP',
          account='from-account@yourserver.net',
          pw='email app password here')
