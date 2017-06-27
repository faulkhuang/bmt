# encoding: utf-8

import os

def scan_local_ip():
	

if __name__ == "__main__":
	server_port = os.getenv('PORT', '8080')
	server_ip = os.getenv('IP', '0.0.0.0')
	print server_port
	print server_ip
