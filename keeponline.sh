while true
do
	if timeout 0.4s ping6 2a11:: -c1
	then 
		echo "Connected"
	else
		python login.py
	fi
	sleep 2s
done
