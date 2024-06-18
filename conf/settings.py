import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ALLOWED_HOSTS = ["127.0.0.1"]

MONGODB_URL = "mongodb://localhost:27017/" #"mongodb+srv://diegopasti:P8HBWl0FU3lS5PfI@entitylookup.zafw6lg.mongodb.net/?retryWrites=true&w=majority&appName=EntityLookup"
REDIS_URL = "redis://default:YOMUfqOnjACxBtaml3sUwDkt6b5VYUXi@redis-11711.c239.us-east-1-2.ec2.redns.redis-cloud.com:11711"
REDIS_HOST = "redis-11711.c239.us-east-1-2.ec2.redns.redis-cloud.com"
REDIS_PORT = 11711
REDIS_USER = "default"
REDIS_PASS = "YOMUfqOnjACxBtaml3sUwDkt6b5VYUXi"