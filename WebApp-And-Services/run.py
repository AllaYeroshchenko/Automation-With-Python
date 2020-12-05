#! /usr/bin/env python3

import os
import requests

feedbacks=[]
feedback={}

files = os.listdir("data/feedback/")
for file_name in files:
	if not file_name.startswith('.'):
		feedback_data = open("data/feedback/"+file_name, 'r')
		title = feedback_data.readline().strip()
		name = feedback_data.readline().strip()
		dat = feedback_data.readline().strip()
		comment = feedback_data.read()
		feedback = {"title": title,
					"name": name,
					"date": dat,
					"feedback": comment}
		feedbacks.append(feedback)
					
print(feedbacks)

for feedback in feedbacks:
	response = requests.post("http://<corpweb-external-IP>/feedback", data=feedback)
	print(response.status_code)


## Linux
#! /usr/bin/env python3

# import os
# import requests

# feedbacks=[]
# feedback={}

# files = os.listdir("/data/feedback/")
# for file_name in files:
#         if not file_name.startswith('.'):
#                 feedback_data = open("/data/feedback/"+file_name, 'r')
#                 title = feedback_data.readline().strip()
#                 name = feedback_data.readline().strip()
#                 dat = feedback_data.readline().strip()
#                 comment = feedback_data.read()
#                 feedback = {"title": title,
#                                         "name": name,
#                                         "date": dat,
#                                         "feedback": comment}
#                 feedbacks.append(feedback)
#                 print(feedback)
# #print(feedbacks)

# for feedback in feedbacks:
#         response = requests.post("http://34.72.84.167/feedback/", json=feedback)
#         print(response.status_code)

