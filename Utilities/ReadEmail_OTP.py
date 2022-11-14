#modules
import imaplib
import email

#credentials
username ="qc.phdv@gmail.com"

#generated app password
app_password= "nymjwpwfpmrcxlca"

# https://www.systoolsgroup.com/imap/
gmail_host= 'imap.gmail.com'

#set connection
mail = imaplib.IMAP4_SSL(gmail_host)

#login
mail.login(username, app_password)

#select inbox
mail.select("INBOX")

#select specific mails
_, selected_mails = mail.search(None, '(FROM "noreply@noreply.pizzahut.io" SUBJECT "Pizza Hut Fusion OTP")')

#total number of mails from specific user
print("Total Messages from noreply@noreply.pizzahut.io: " , len(selected_mails[0].split()))

_, data = mail.fetch(selected_mails[0].split()[0] , '(RFC822)')
_, bytes_data = data[0]

#convert the byte data to message
email_message = email.message_from_bytes(bytes_data)
print("\n===========================================")

#access data
print("Subject: ",email_message["subject"])
print("To:", email_message["to"])
print("From: ",email_message["from"])
print("Date: ",email_message["date"])
for part in email_message.walk():
    if part.get_content_type()=="text/plain" or part.get_content_type()=="text/html":
        message = part.get_payload(decode=True)
        #print("Message: \n", message.decode())
        print("==========================================\n")
        break
content = str(message.decode()).split("<body>")[1].split("</body>")[0]
print(content)