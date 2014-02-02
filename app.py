import os
import feedparser
import jinja2
import xmlrpclib

# TODO:
# - post the draft to Wordpress
# - only show links which are new since the last draft was posted

from flask import Flask
app = Flask(__name__)

wordpress_url = os.environ['WORDPRESS_URL']
wordpress_user = os.environ['WORDPRESS_USER']
wordpress_password = os.environ['WORDPRESS_PASSWORD']
feed_urls = os.environ['FEEDS'].split()

def get_feeds():
  return map(feedparser.parse, feed_urls)

@app.route('/')
def preview():
  template = jinja2.Template(open('preview.html').read())
  return template.render(feeds=get_feeds())

@app.route('/post-draft')
def post_draft(reset=False):
  template = jinja2.Template(open('wordpress.html').read())
  post_body = template.render(feeds=get_feeds())
  return ''

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
