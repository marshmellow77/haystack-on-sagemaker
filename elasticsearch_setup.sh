sudo yum install docker
(sudo) docker pull docker.elastic.co/elasticsearch/elasticsearch:7.9.2
sudo dockerd
sudo docker run -d -p 9200:9200 -e "discovery.type=single-node" elasticsearch:7.9.2
netstat -tulpn
curl -X GET 'http://localhost:9200/_cat/indices?v'