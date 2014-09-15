# -*- coding: utf-8 -*-

# Scrapy settings for shoebank project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'shoebank'

SPIDER_MODULES = ['shoebank.spiders']
NEWSPIDER_MODULE = 'shoebank.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'shoebank (+http://www.yourdomain.com)'

FEED_URI = 'file:///tmp/shoebank.csv'
FEED_FORMAT = 'csv'
