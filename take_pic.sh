
raspistill -vf -hf -o /var/www/html/pics/pic_`date "+%Y%m%d%H%M"`.jpg
/home/pi/makepage.py > /var/www/html/picpage.html
