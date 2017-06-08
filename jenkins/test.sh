url=$1
failed=0
python jenkins/test.py || failed=1
s3_static || echo success
