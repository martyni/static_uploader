import boto3
import datetime
import sys
from botocore.client import Config

client = boto3.client("s3", config=Config(signature_version='s3v4'))
cache = {}
time_format = "%Y-%M-%d %H:%M:%s"
s3_link = "https://s3-eu-west-1.amazonaws.com/{}/"

class static_uploader(object):
    def __init__(self):
        try:
            self.s3_bucket = sys.argv[1]
            self.project = sys.argv[2]
            self.env = sys.argv[3]
            self.key_prefix = "{}/{}/".format(self.project,self.env)
        except:
            self.help()
            sys.exit(0)

    def help(self):
        print('''
Usage: {}: <s3_bucket> <project> <env> <path>
'''.format(sys.argv[0]))

    def put_files(self):
        try:
            path = sys.argv[4]
        except:
            self.help()
            sys.exit(1)
        key = self.key_prefix + path
        content = None
        for c in "html", "css":
            if c in path:
                content = "text/{}".format(c)
        print("{bucket}.s3-website.eu-west-2.amazonaws.com/{key}".format(key = key, bucket=self.s3_bucket))
        client.upload_file(path, self.s3_bucket, key, ExtraArgs={'ACL': 'public-read','ContentType': content})


app = static_uploader()
