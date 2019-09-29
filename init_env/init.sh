# activate peopledata environment
export CODEPATH=$HOME/peopledata
export PYTHONPATH=$PYTHONPATH:$CODEPATH/lib/

echo """
# add peopledata repo path
export CODEPATH=$HOME/peopledata
export PYTHONPATH=$PYTHONPATH:$CODEPATH/lib/
""" >>  $HOME/.bashrc

source $HOME/.bashrc

# release crendential in environment
cat $CODEPATH/.credential >> $HOME/.bashrc

# install python requirements
pip install -r $CODEPATH/init_env/requirements.txt


source $HOME/.bashrc
