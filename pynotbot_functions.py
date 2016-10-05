import urllib.request
import time
import smtplib
import re

def error():
    print("""
Usage:
        python3.5 pynotbot.py <url> <interval (in seconds)> <receiver email for notification> <bot's email> <bot's email password>

Example:
        python3.5 pynotbot.py google.com 5 someone@somewhere.com pynotbot@somewhere.com password

    Supports only gmail for now.""")
    quit()

def check_args(args):

    if len(args) != 6:
        error()

    try:
        float(args[2])
    except:
        print("[!] Error: Intervals must be numbers.")
        error()

    if not re.match(r"^([a-z0-9_-]+)(@[a-z0-9-]+)(\.[a-z]+|\.[a-z]+\.[a-z]+)?$", args[3]):
        print("[!] Error: Receiver email not valid.")
        error()

    if not re.match(r"^([a-z0-9_-]+)(@[a-z0-9-]+)(\.[a-z]+|\.[a-z]+\.[a-z]+)?$", args[4]):
        print("[!] Error: Bot email not valid.")
        error()


def notify(from_addr, to_addr, url, server):
    msg = "\r\n".join([
    "From: "+from_addr,
    "To: "+to_addr,
    "Subject: "+url+" updated.",
    "",
    "The website on " + url + " has been updated."
    ])
    server.sendmail(from_addr, to_addr, msg)

def notifier(from_addr, to_addr, url, interval, server):
    print("Notifier started on: " + url + ". Checking every " + str(interval) + " seconds.")
    page_source = urllib.request.urlopen(url).read()

    while True:
        new_page_source = urllib.request.urlopen(url).read()
        if page_source != new_page_source:
            page_source = new_page_source
            notify(from_addr, to_addr, url, server)

        time.sleep(interval)
