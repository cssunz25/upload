
ant_input=`cat /dev/stdin`
a#!/bin/sh

mv /etc/init.d/bmminer.sh /home
chmod  777 /home/bmminer.sh

mv /www/pages/cgi-bin/minerStatus.cgi /home
chmod  777 /home/minerStatus.cgi

cp /config/x/bmminer.sh /etc/init.d/

cp /config/x/minerStatus.cgi /www/pages/cgi-bin/


rm /config/dropbear

rm /etc/default/dropbear

/etc/init.d/dropbear start

echo -e "toor\ntoor" | passwd root

reboot