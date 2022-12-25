# scrapy_lyrics_finder

1. Install Scrapy
   As a prerequisites you need to have install python2.7 or above, pip/anaconda package manager

To install Scrapy using conda:

conda install -c conda-forge scrapy

To install Scrapy using pip:

pip install Scrapy

2. Create a new Scrapy project

Navigate where you want to create the project, open a terminal and issue

scrapy startproject lyrics

Here “lyrics” is the project name.

This commands create a new Scrapy project called “lyrics” and it contains a folder as “lyrics” and a file called “scrapy.cfg” .

3. Run the created spider

Navigate to the project’s top level directory and run:

scrapy crawl lyrics -o output.json

Here “lyrics” is the name used at the spider class.

class LyricsSpider(SitemapSpider):
name = “lyrics”
The extracted data will be written into “output.json” file.
