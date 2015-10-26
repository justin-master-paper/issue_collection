import scrapy
import json
from werkzeug.urls import Href
from urlparse import urlparse, parse_qs

from issue_collection.items import IssueItem

per_page = 100
#auth_token = '517119d1f57cd208bd68da1f7869dd1374bb8f48'
auth_token = 'c1730619372d3306343d67a16e748b4bfaa31fd9'
user = 'justin-sunflower'
password = 'yeyuangithub217'

headers = {
    "Authorization": "Basic %s:%s" % (user, password)
}

class IssueCollectionSpider(scrapy.Spider):
    name = "issue_collection"
    allowed_domains = ["api.github.com"]
    start_urls = [
        'https://api.github.com/repos/ecomfe/echarts/issues?page=%s&per_page=%s&access_token=%s' % (1, per_page,auth_token)
        #'https://api.github.com/repos/ecomfe/echarts/issues?page=%s&per_page=%s' % (1, per_page)
    ]

    def parse(self, response):
        issues = json.loads(response.body)
        for issue in issues:
            issue_url = Href(issue['url'])({'access_token': auth_token})
            #issue_url = Href(issue['url'])()
            yield scrapy.Request(issue_url, callback=self.parse_issue)
            #yield scrapy.Request(issue_url, callback=self.parse_issue, headers=headers)
        if len(issues) < per_page:
            return
        parsed_url = urlparse(response.url)
        query_params = parse_qs(parsed_url.query)
        query_params['page'] = [int(query_params['page'][0]) + 1]
        base_url = response.url.split("?")[0]
        url = Href(base_url)(query_params)
        print 'url:',url
        yield scrapy.Request(url, callback=self.parse)
        #yield scrapy.Request(url, callback=self.parse, headers=headers)

    def parse_issue(self, response):
        issue = json.loads(response.body)
        issue['repo'] = issue['url'][::-1].split('/issues'[::-1],1)[1][::-1]
        yield IssueItem(issue)

"""
{
  "id": 22174854,
  "url": "https://api.github.com/authorizations/22174854",
  "app": {
    "name": "issue fetch (API)",
    "url": "https://developer.github.com/v3/oauth_authorizations/",
    "client_id": "00000000000000000000"
  },
  "token": "6feedee5cb0fcca40f1043f96ff54f5fde874804",
  "hashed_token": "9f5ccafee8bdb8c94fe31ee82c740a332ccc27a914d09e67e1e75f2b08ed3afe",
  "token_last_eight": "de874804",
  "note": "issue fetch",
  "note_url": null,
  "created_at": "2015-09-16T07:18:05Z",
  "updated_at": "2015-09-16T07:18:05Z",
  "scopes": [
    "public_repo"
  ],
  "fingerprint": null
}
"""
