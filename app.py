import os
import feedparser
import jinja2

# TODO:
# - only show links which are new since the last draft was posted
# - post the draft to Wordpress

from flask import Flask
app = Flask(__name__)

feed_urls = ['http://feeds.delicious.com/v2/rss/tag/geekfeminism',
             'http://feeds.pinboard.in/rss/t:geekfeminism']

@app.route('/')
def preview():
  template = jinja2.Template(open('preview.html').read())
  feeds = map(feedparser.parse, feed_urls)
  return template.render(feeds=feeds)

@app.route('/post-draft')
def post_draft(reset=False):
  template = jinja2.Template(open('wordpress.html').read())
  feeds = map(feedparser.parse, feed_urls)
  post_body = template.render(feeds=feeds)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
