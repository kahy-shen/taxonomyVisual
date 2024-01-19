echo  
echo Launching a local Web Server to host the interactive visualizations...
echo 
echo Go to http://localhost:4080/ .
echo Terminate this process using Ctrl-C when done.
echo 

PYTHON_VERSION=`python -c 'import platform; print(platform.python_version().replace(".", ""))'`


if [ $PYTHON_VERSION -ge '350' ]; then 
   python -m http.server 4080
else
   echo "Python 3.5 required"
fi


echo
echo "Local Web Server terminated."
echo

