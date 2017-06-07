export PID=$(ps aux | grep -v awk |awk /boop/'{print $2}')
echo killing $PID
echo $PID >/tmp/PID
