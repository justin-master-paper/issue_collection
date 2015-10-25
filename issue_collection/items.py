# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IssueItem(scrapy.Item):
    url = scrapy.Field()
    labels_url = scrapy.Field()
    comments_url = scrapy.Field()
    events_url = scrapy.Field()
    html_url = scrapy.Field()
    repo = scrapy.Field()
    id = scrapy.Field()
    number = scrapy.Field()
    title = scrapy.Field()
    user = scrapy.Field()
    labels = scrapy.Field()
    state = scrapy.Field()
    locked = scrapy.Field()
    assignee = scrapy.Field()
    milestone = scrapy.Field()
    comments = scrapy.Field()
    created_at = scrapy.Field()
    updated_at = scrapy.Field()
    closed_at = scrapy.Field()
    pull_request = scrapy.Field()
    body = scrapy.Field()
    closed_by = scrapy.Field()

