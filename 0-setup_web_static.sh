#!/usr/bin/env bash
#Script that Set up nginx;
apt-get -y update
apt-get -y install nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared
echo -e "<html>\n\t<head>\n\t\t<title>Best School</title>\n\t</head>\n\t<body>\n\t\t<h2>Best School</h2>\n\t</body>\n</html>" > /data/web_static/releases/test/index.html
rm -f /data/web_static/current > /dev/null
ln -s /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "s/server_name _;/\tserver_name _;\n\tlocation /hbnb_static/ {\n\t\talias /data/webstatic/current;\n\t\ttry_files \$uri \$uri/ =404;\n\t}"
