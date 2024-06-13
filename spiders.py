
import requests
import csv
import os
from lxml import etree
import re
import json
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:209708@localhost:3306/douban')
class spider(object):
    def __init__(self):
        self.spiderUrl = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/109.0.0.0 Safari/537.36 SLBrowser/9.0.0.10191 SLBChan/33'
        }
        self.page_limit = 10
    def init(self):
        if not os.path.exists("./tempData.csv"):
            with open("./tempData.csv", 'w', newline='') as writer_f:
                csv_writer = csv.writer(writer_f)
                csv_writer.writerow(
                    ['directors', 'rate', 'title', 'cover', 'detailLink', 'casts', 'year', 'type', 'country', 'lang',
                     'time', 'moveTime', 'comment_len', 'starts', 'summary', 'comments', 'imgList', 'movieUrl'])

        if not os.path.exists('./spidersPage.txt'):
            with open("./spidersPage.txt", 'w', encoding='utf-8') as writer_f:
                writer_f.write('0\n')

    def get_spiderPage(self):
        with open('./spidersPage.txt', 'r') as f:
            return f.readlines()[-1].strip()

    def set_spiderPage(self, newPage):
        with open('./spidersPage.txt', 'a') as f:  # 'a'追加模式，在文件末尾添加数据，不覆盖原有数据
            f.write(str(newPage)+'\n')  # 添加内容为：newPage + '\n'

    def spidermain(self):
        page_start = self.get_spiderPage()
        params = {
            'page_limit': self.page_limit,
            'page_start': int(page_start) * 10
        }
        print("正在爬取第%d页" % (int(page_start) + 1))

        respJson = requests.get(self.spiderUrl, params=params, headers=self.headers).json()

        # print(respJson)
        respJson = respJson['subjects']
        resultList = []
        # try:
        for index, movieData in enumerate(respJson):
            print("正在爬取第%d条信息" % (index + 1))
            print(movieData['url'])
            resultData = []
            # 电影评分（rate）
            resultData.append(movieData['rate'])
            # 电影标题（title）
            resultData.append(movieData['title'])
            # 电影封面（cover）
            resultData.append(movieData['cover'])
            # 电影详情链接（detailLink）
            resultData.append(movieData['url'])

            respDetailHTML = requests.get(movieData['url'], headers=self.headers)
            ree = respDetailHTML.text
            respDetailHTMLXpath = etree.HTML(respDetailHTML.text)  # respDetailHTML.tex抓取网页源代码

            # 电影导演(directors)
            directors = respDetailHTMLXpath.xpath('//*[@id="info"]/span[1]/span/a/text()')
            resultData.insert(0, directors[0])

            # 电影演员（casts）
            casts = respDetailHTMLXpath.xpath('//*[@id="info"]/span[3]/span/a/text()')
            resultData.append(','.join(casts))

            # 电影年份（year）
            year = re.search(r'\d+', respDetailHTMLXpath.xpath('//*[@id="content"]/h1/span[2]/text()')[0]).group()
            resultData.append(year)

            # 电影类型（type）
            types = []
            for i in respDetailHTMLXpath.xpath('//*[@id="info"]/span[@property="v:genre"]'):
                types.append(i.text)
            resultData.append(','.join(types))

            # 电影制片国家 country
            country = re.findall('<span class="pl">制片国家/地区:</span>(.*?)<br/>', str(ree))
            resultData.append(','.join(country))

            # 电影语言 lang
            lang = re.findall('<span class="pl">语言:</span>(.*?)<br/>', str(ree))
            resultData.append(','.join(lang))

            # 电影上映时间 time
            time = respDetailHTMLXpath.xpath('//*[@id="info"]/span[@property="v:initialReleaseDate"]/text()')[0][:10]
            resultData.append(time)

            # 电影片长 movieTime
            try:
                movieTime = re.search(r'\d+', respDetailHTMLXpath.xpath(
                    '//*[@id="info"]/span[@property="v:runtime"]/text()')[0]).group()
                resultData.append(movieTime)
            except:
                resultData.append(0)

            # 短评个数 comment_len
            comment_len = re.search(r'\d+', respDetailHTMLXpath.xpath(
                '//*[@id="comments-section"]/*[@class="mod-hd"][1]/h2//a/text()')[0]).group()
            resultData.append(comment_len)

            # 电影星级 starts
            starts = []
            for i in respDetailHTMLXpath.xpath(
                    '//*[@id="interest_sectl"]//*[@class="ratings-on-weight"]/*[@class="item"]'):
                starts.append(i.xpath('./span[@class="rating_per"]/text()')[0])
            resultData.append(','.join(starts))

            # 电影信息介绍 summary
            '''
            summary2 = ''.join(respDetailHTMLXpath.xpath(
                '//*[@id="link-report-intra"]/span[@property="v:summary"]/text()'))
            summary = summary2.strip()
            '''
            try:
                summary = respDetailHTMLXpath.xpath('//*[@id="link-report-intra"]/span[@property="v:summary"]/text()')[
                    0].strip()
                resultData.append(summary)
            except:
                summary = respDetailHTMLXpath.xpath('//*[@id="link-report-intra"]/span/span[@property="v:summary"]/text'
                                                    '()')[0].strip()
                resultData.append(summary)

            # 电影评论 comments
            comments = []
            comments_list = respDetailHTMLXpath.xpath('//*[@id="hot-comments"]')
            for i in comments_list:
                user = i.xpath('.//h3/span[2]/a/text()')[0]
                star = re.search(r'\d+', i.xpath('.//h3/span[2]/span[2]/@class')[0])
                if star is not None:
                    star = star.group()
                time = ''.join(i.xpath('.//h3/span[2]/span[3]/text()')[0]).strip()
                content = i.xpath('.//p/span/text()')[0]
                comments.append({
                    'user': user,
                    'star': star,
                    'time': time,
                    'content': content
                })
            resultData.append(json.dumps(comments))

            # 电影图片 imgList
            imgList = respDetailHTMLXpath.xpath('//*[@id="related-pic"]/ul/li/a/img/@src')
            resultData.append(','.join(imgList))

            # 预告片链接
            movieUrl = respDetailHTMLXpath.xpath('//*[@id="related-pic"]/ul/li[1]/a/@href')[0]
            # 预告片视频
            movieHTML = requests.get(movieUrl, headers=self.headers)
            movieHTMLXpath = etree.HTML(movieHTML.text)
            haveMovie = movieHTMLXpath.xpath('//video/source/@src')
            if len(haveMovie) != 0:
                movie = movieHTMLXpath.xpath('//video/source/@src')[0]
                resultData.append(movie)
            else:
                resultData.append("暂无预告片，敬请期待！")
            # print(resultData)
            resultList.append(resultData)


        # except:
        #     pass

        self.save_to_csv(resultList)
        self.set_spiderPage(int(page_start) + 1)
        self.spidermain()

    def save_to_csv(self, resultList):
        with open('./tempData.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for rowData in resultList:
                writer.writerow(rowData)






if __name__ == '__main__':
    spiderObj = spider()
    spiderObj.init()
    spiderObj.spidermain()

