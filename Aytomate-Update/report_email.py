
#!/usr/bin/env python3
from datetime import date
import os
import reports
import emails




if __name__ == "__main__":
  
  fruits=""
  path = "supplier-data/descriptions/"
  files = os.listdir(path)
  for file_name in files:
    print(path+file_name)
    fruit_data = open(path+file_name, 'r')
    name = fruit_data.readline().strip()
    weight = fruit_data.readline().strip()
    fruits += "name: " + name + "<br/>" + "weight: " + weight + "<br/><br/>"

  attachment = "/tmp/processed.pdf"
  title = "Processed Update on "+ str(date.today().strftime("%d %B, %Y"))
  paragraph = fruits
  reports.generate_report(attachment, title, paragraph)

  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

  message = emails.generate_email(sender, receiver, subject, body, attachment)
  emails.send_email(message)