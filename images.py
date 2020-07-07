import smtplib
smtp_object = smtplib.SMTP('smtp.gmail.com',587)  //port 587 tls encryption create object that will meet domain thrugh tls encryption port 587
smtp_object.ehlo()  //this should be right after the above code. The objct will esablish communication with the server
smtp_object.starttls()  // initiate by running the starttls() command if server ggreeting thoorugh 587 port

import getpass
result = getpass.getpass("Type something here and it will be hidden: ")  //input text will be hidden.good for passwords
email = getpass.getpass("Enter your email: ")
password = getpass.getpass("Enter your password: ")
smtp_object.login(email,password)

from_address = getpass.getpass("Enter your email: ")
to_address = getpass.getpass("Enter the email of the recipient: ")
subject = input("Enter the subject line: ")
message = input("Type out the message you want to send: ")
msg = "Subject: " + subject + '\n' + message
smtp_object.sendmail(from_address,to_address,msg)

smtp_object.quit()


