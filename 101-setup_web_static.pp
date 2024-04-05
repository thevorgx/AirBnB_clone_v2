# Install nginx and create a symbolic link

exec { 'Puppet_for_setup':
  command  => 'apt-get -y update &&
              apt-get -y install nginx &&
              sudo mkdir -p /data/web_static/releases/test/ &&
              echo "Hello Vorg" | sudo tee /data/web_static/releases/test/index.html &&
              sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current &&
              sudo chown -R ubuntu:ubuntu /data/ &&
              service nginx restart',
  provider => shell,
}
