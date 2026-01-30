import os
from dotenv import load_dotenv, find_dotenv

p = find_dotenv()
print('find_dotenv returned:', p)
if p:
    load_dotenv(p)
    print('.env loaded from', p)
else:
    print('No .env found')

print('MONGO_URL:', os.getenv('MONGO_URL'))
