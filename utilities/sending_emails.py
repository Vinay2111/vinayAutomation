import smtplib

server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("vinay@eezylife.com","Vinay@4125")
server.sendmail("vinay@eezylife.com.com","vinay.jude.m@gmail.com","Hello this is vinay")
server.quit()
