FROM ubuntu

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 627220E7; \
    echo 'deb http://archive.scrapy.org/ubuntu scrapy main' | sudo tee /etc/apt/sources.list.d/scrapy.list; \
    apt-get update && apt-get install -qy scrapy-0.24

RUN useradd -m shoebank
ADD . /home/shoebank
USER shoebank
WORKDIR /home/shoebank/shoebank

CMD scrapy crawl shoebank
