import os
import feedparser
import jinja2

from flask import Flask
app = Flask(__name__)

feed_urls = ['http://feeds.delicious.com/v2/rss/tag/geekfeminism',
             'http://feeds.pinboard.in/rss/t:geekfeminism']

@app.route('/')
def dump():
  template = jinja2.Template(open('template.html').read())
  feeds = map(feedparser.parse, feed_urls)
  return template.render(feeds=feeds)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
