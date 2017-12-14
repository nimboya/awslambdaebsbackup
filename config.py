import os
 # Environment Variables to Handle Local and Production
environment = os.getenv('environment')
mongousername = os.getenv('mongousername')
mongopassword = os.getenv('mongopassword')
mongohost = os.getenv('mongohost')
mongoport = os.getenv('mongoport')