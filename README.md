gatheryelinks
=============

Gather up links and submit to Wordpress for linkspam posts

= Setup =

```
$ cat .environ
FEEDS=http://feeds.delicious.com/v2/rss/tag/geekfeminism http://feeds.pinboard.in/rss/t:geekfeminism
DATABASE_URL=postgres://...
WORDPRESS_URL=http://geekfeminismdotorgtest.wordpress.com/
WORDPRESS_BLOGID=0
WORDPRESS_USER=gfspamspam
WORDPRESS_PASSWORD=12345678
$ foreman start
```
