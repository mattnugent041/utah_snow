import smtplib

carriers ={
  'att': '@mms.att.net',
  'tmobile': '@tmomail.net',
  'verizon': '@vtext.com',
  'sprint': '@page.nextel.com'
}

#SMTP Setup
# Verify 'less secure apps' are able to access your Gmail
def send(message,numbers,cell_company,gmail_address,gmail_password):
  to_number=numbers.format(carriers[cell_company])
  auth= (gmail_address, gmail_password) 
  server= smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login(auth[0], auth[1])
  server.sendmail(auth[0], to_number, message)
