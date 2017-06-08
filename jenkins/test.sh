source env/bin/activate
url=$1
failed=0
python jenkins/test.py $url|| failed=1
s3_static || echo success
echo $failed>/tmp/EXIT 
exit $(cat /tmp/EXIT)
