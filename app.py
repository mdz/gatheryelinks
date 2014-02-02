import os
import feedparser
from jinja2 import Template

from flask import Flask
app = Flask(__name__)

@app.route('/')
def dump():
  template = Template(open('template.html').read())
  return template.render(links=[{'href': 'http://www.example.com', 'title': 'Example'}])

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
