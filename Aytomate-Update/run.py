#! /usr/bin/env python3
import os
import requests

fruits=[]
fruit={}
path = "supplier-data/descriptions/"
files = os.listdir(path)
for file_name in files:
    print(path+file_name)
    fruit_data = open(path+file_name, 'r')
    name = fruit_data.readline().strip()
    weight = int(fruit_data.readline().strip()[:4])
    description = fruit_data.read()
    fruit = {"name": name,
            "weight": weight,
            "description": description,
            "image_name": file_name[:-4]+".jpeg"}
#    print(fruit)
    fruits.append(fruit)

for fruit in fruits:
    response = requests.post("http://35.238.56.174/fruits/", json=fruit)
    print(response.status_code)

