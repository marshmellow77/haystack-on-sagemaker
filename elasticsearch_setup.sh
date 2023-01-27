# set up docker
sudo yum install docker -y
sudo dockerd &

# puller docker image for elasticsearch and run it
sudo docker pull docker.elastic.co/elasticsearch/elasticsearch:7.9.2
sudo docker run -d -p 9200:9200 -e "discovery.type=single-node" elasticsearch:7.9.2
