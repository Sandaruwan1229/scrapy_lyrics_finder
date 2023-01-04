from scrapy.spiders import SitemapSpider
import re


class LyricsSpider(SitemapSpider):
    name = "lyrics"
    allowed_domains = ['sinhalasonglyrics.com']
    sitemap_urls = [
        "https://sinhalasonglyrics.com/sitemap-index-1.xml",
        "https://sinhalasonglyrics.com/sitemap-2.xml"
    ]
    artists = ["centigradz"]
    # artists = ["dhanith-sri", "supun-perera", "ridma-weerawardana", "kanchana-anuradhi", "dinesh-gamage", "dinupa-kodagoda", "yasas-madagedara", "charitha-attalage", "bashi-devanga", "sadara-bandara"]
    sitemap_rules = [(".*" + artist + ".*", 'parse') for artist in artists]

    def parse(self, response):
        ## retrieve lyrics
        song_lines = response.xpath('//div[@class="entry-content e-content"]/p').getall()
        song = ''
        for line in song_lines:
            line = line.replace("<p>", "")
            line = line.replace("</p>", "")
            line = line.replace("<br>", "")
            line = re.sub("<strong>.*</strong>", "" , line)
            line = re.sub("<a href.*</a>", "" , line)
            song = song + " " + line

        ## retrieve song title and singer
        url = response.request.url
        metadata_start = url.index(self.allowed_domains[0])
        metadata_end = metadata_start + len(self.allowed_domains[0])
        metadata = url[metadata_end + 1: -1]
        title, singer = metadata.split("-by-")
        singer = singer.replace("-", " ")
        title = title.replace("-", " ")
        yield {
            'title': title,
            'singer': singer,
            'song' : song,
        }
