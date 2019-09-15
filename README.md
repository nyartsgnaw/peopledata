# peopledata

initialize environment:
```
# install phantonjs for requirements: https://pythonspot.com/selenium-phantomjs/  
export PATH=$PATH:$CODEPATH/init_env/phantomjs-2.1.1-linux-x86_64/bin

# activate peopledata environment
export CODEPATH=$HOME/peopledata
export PYTHONPATH=$PYTHONPATH:$CODEPATH/lib/

# install python requirements
pip install -r $CODEPATH/init_env/requirements.txt
```