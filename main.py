import smtplib
my_email = "saransh.shankar@gmail.com"
password = "ppnhfilfnhvkqfom"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs=my_email, msg="Subject:Hello\n\nThis is my new program")
connection.close()
