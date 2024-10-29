if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
!git clone https://github.com/AJAYBOTS/autofilter.git/autofilter
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /autofilter
fi
cd /Opleech-Filter-Bot 
pip3 install -U -r requirements.txt
echo "Starting autofilter 😎...."
python3 bot.py    
