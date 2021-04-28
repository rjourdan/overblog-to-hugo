#!/usr/bin/python3

# Copyright (c) 2020, Romain Jourdan
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. 

import sys, getopt, os
import xml.etree.ElementTree as ET
from markdownify import markdownify as md


def write_post(post,output_folder):
    title = post.find('title').text
    slug = post.find('slug').text
    str_tags = post.find('tags').text
    tags = None
    if str_tags:
        tags_list = str_tags.split(',')
        tags =  '\',\''.join([str(item) for item in tags_list])
        tags = '[\''+tags+'\']' 
    
    publication = post.find('published_at').text
    author = post.find('author').text
    #retrieve post content in HTML
    html_content= post.find('content').text
    # convert HMTL content in Markdown
    md_content = md(html_content)

    #from the slug, we are going to create the folder
    slug_split = slug.split('/')
    foldername = slug_split[-1]
    #remove html
    foldername = foldername[0:-5]
    #check if output_folder has a / at the end
    if(output_folder[-1]=='/'):
        output_folder = output_folder[0:-1]
    #create the folder
    os.mkdir(output_folder+'/'+foldername)

    filename = output_folder+'/'+foldername +'/index.md' 
    
    f = open(filename, "w")
    f.write('---\n')
    title = "title: \'"+title+"\'\n"
    f.write(title)
    date = "date: \'"+publication+"\'\n"
    f.write(date)
    author = "author: \'"+author+"\'\n"
    f.write(author)
    if tags:
        f.write("tags: "+tags+"\n")
    f.write('---\n')
    f.write(md_content)
    f.close

    

def main(argv):
    inputfile = ''
    # by default we export to a directory called hugo.
    outputfolder = 'hugo'
    # retrieve and interpret the arguments
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofolder="])
    except getopt.GetoptError:
        print('oblog2hugo.py -i <overblog XML export file> [-o <output folder>]')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('oblog2hugo.py -i <overblog XML export file> [-o <output folder>]')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofolder"):
            outputfolder = arg

    # check whether the output folder exists, if not create one
    if not os.path.exists(outputfolder):
        os.makedirs(outputfolder)

    #parse XML and convert to blogs
    xml_file = ET.parse(inputfile)
    root = xml_file.getroot()
   
    #for blog in root.iter('blog'):
    #    for child in blog:
    #        print(child.tag, child.text)

    for posts in root.findall('posts'):
        for post in posts:
            write_post(post,outputfolder)
            
if __name__ == "__main__":
   main(sys.argv[1:])