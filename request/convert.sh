sudo apt-get install libmagickwand-dev
pip3 install wand
FILE=/etc/ImageMagick-6/policy_backup.xml
if [ -f "$FILE" ]; then
    echo "$FILE back up exists."
else 
    echo "$FILE back up does not exist."
    sudo cp /etc/ImageMagick-6/policy.xml /etc/ImageMagick-6/policy_backup.xml
fi

sudo sed -i 's/<policy domain="coder" rights="none" pattern="PDF"/<policy domain="coder" rights="read|write" pattern="PDF"/g' /etc/ImageMagick-6/policy.xml





