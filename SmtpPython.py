import smtplib

user = 'email address'
de = 'username'
usr = 'email address or user name'
paswd = 'your password'

sent_from = de
to = ['recipient email', 'recipient email']
subject = 'le 10 fevrier'
body = 'Bonne journee en ce 10 fevrier'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP('address of smtp server', 587)
    smtp_server.ehlo()
    smtp_server.login(usr, paswd)
    smtp_server.sendmail(de, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)
