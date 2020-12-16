# overblog-to-hugo

## Motivation

I wrote this piece of code to migrate my former blog hosted on Over-Blog.com to a self-hosted blog with hugo. 
Over-Blog.com export capabilities are limited. It create an XML document export.xml 

## Pre-requisites

Install dependencies:

```$ pip install -r requirements.txt```

## Use

```$ python oblog2hugo.py -i <overblog XML export file> [-o <output folder>]```

By default, a directory named ```hugo``` will be created unless specified with ```-o <output folder>```

## Limitations

Over-blog.com's does not export the pictures from your blog. The tool cool download images and rewrite the url. 