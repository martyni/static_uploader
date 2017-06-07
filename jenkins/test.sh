url=$1
failed=0
python jenkins/test.py $url || failed=1
if [ "$(curl $url/test)" == "OMG" ]
  then  
     echo success
  else
     echo failure
     failed=1
fi
if [ "$(curl $url/| grep ballface)" ]
  then  
     echo failure
     failed=1
  else
     echo success
fi
echo $failed >/tmp/EXIT
