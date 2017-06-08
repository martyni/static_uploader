source env/bin/activate
env=$1
failed=0
python jenkins/test.py $env|| failed=1

#Check help text is there
if [ "$(s3_static | grep Usage)" ]
   then echo success
   else echo fail && failed=1	   
fi

#Upload file and check it's contents is accessible
echo $RANDOM > upload.html
url=$(s3_static martyni-static jenkins $env upload.html)
file_contents=$(curl $url)
if [ $file_contents=="$(cat upload.html)" ]
   then echo success && echo $file_contents $url
   else echo fail && failed=1
fi

echo $failed>/tmp/EXIT 
exit $(cat /tmp/EXIT)
