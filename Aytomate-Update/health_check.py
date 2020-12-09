#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails
import os, sys


def check_cpu_usage():
	usage = psutil.cpu_percent(1)
	return usage>80

def check_memory_space():
	vmem = psutil.virtual_memory()
	return vmem.available/(1024*1024)<500

def check_disc_usage(disk):
	du = shutil.disk_usage(disk)
	free = du.free/du.total*100
	return free<20


def hostname_check():
	local_host_ip = socket.gethostbyname('localhost')
	return local_host_ip == "127.0.0.1"


def email_warning(error):
	sender = "automation@example.com"
	receiver = "{}@example.com".format(os.environ["USER"])
	subject = error
	body = "Please check your system and resolve the issue as soon as possible."
	message = emails.generate_email(sender, receiver, subject, body)
	emails.send_email(message)

if check_cpu_usage():
	subject = "Error - CPU usage is over 80%"
	email_warning(subject)

if check_disc_usage():
	subject = "Error - Available disk space is less than 20%"
	email_warning(subject)

if check_memory_space():
	subject = "Error - Available memory is less than 500MB"
	email_warning(subject)

if not hostname_check():
	subject = "Error - localhost cannot be resolved to 127.0.0.1"
	email_warning(subject)


