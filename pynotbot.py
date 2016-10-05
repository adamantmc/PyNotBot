import sys
from pynotbot_functions import *

check_args(sys.argv)

email = sys.argv[3]

botmail = sys.argv[4]
password = sys.argv[5]

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(botmail, password)

notifier(botmail, email, sys.argv[1], float(sys.argv[2]), server)
