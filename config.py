import logging
import os
import sys

#Logger
logger = logging.getLogger('query_resolver')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

#DB
HOST=os.environ.get('RDS_HOST')
PORT=os.environ.get('RDS_PORT')
USER=os.environ.get('RDS_USER')
PASSWORD=os.environ.get('RDS_PASSWORD')
DB=os.environ.get('RDS_DB_NAME')

# s3 bucket
BUCKET_NAME =os.environ.get('S3_BUCKET_NAME')
