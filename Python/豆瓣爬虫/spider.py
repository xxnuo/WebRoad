# -*- coding=utf-8 -*-

from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import unicodedata


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 爬取网页 解析数据
    dataList = getData(baseurl)
    path = ".\\douban\\all.xls"
    # 保存数据
    saveData(path, dataList)

findNo = re.compile('<em class="">(\d*?)</em>')
findLink = re.compile(r'<a href="(.*?)">')
#让 '.' 特殊字符匹配任何字符，包括换行符；对应内联标记 (?s) 。
findImgSrc= re.compile(r'<img.*src="(.*?)"', re.S)
findTitle = re.compile(r'<span class="title">(.*?)</span>')
findRating = re.compile(r'class="rating_num".*>(.*?)</span>')
findJudge = re.compile(r'<span>(\d*?)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*?)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)

# 对获取到的html内容进行解析
def getData(baseUrl):
    datalist = []
    for i in range(0, 10):
        url = baseUrl + str(i * 25)
        html = getHtml(url)
        # 解析
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):
            #print(item)
            data = []
            #item = str(item)
            item = unicodedata.normalize("NFKC", str(item))

            no = re.findall(findNo, item)[0]
            data.append(no)

            link = re.findall(findLink, item)[0]
            data.append(link)

            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)

            titles = re.findall(findTitle, item)
            if(len(titles) == 2):
                ctitle  = titles[0].strip()
                data.append(ctitle)
                etitle = titles[1].replace("/","").strip()
                data.append(etitle)
            else:
                data.append(titles[0])
                data.append(" ")

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judge = re.findall(findJudge, item)[0]
            data.append(judge)

            inq = re.findall(findInq, item)
            if(len(inq) != 0):
                inq = inq[0].replace("。","")
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " / ", bd)
            #bd = re.sub("/", " ", bd)
            bd = bd.strip()
            #bd = unicodedata.normalize('NFKC', bd)
            data.append(bd)

            datalist.append(data)
    #print(datalist)
    return datalist


# 获取html内容
def getHtml(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"
    }
    req = urllib.request.Request(url, headers=headers)
    html = ""
    try:
        response = urllib.request.urlopen(req, timeout=5)
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

def saveData(path, datalist):
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)
    worksheet = workbook.add_sheet('top250',cell_overwrite_ok=True)
    col = ('No','电影详情链接','图片链接','中文名','外文名','评分','评价数','概况','相关信息')
    for i in range(0, 9):
        worksheet.write(0,i,col[i])
    for i in range(0, 250):
        #print("第%d条"%i)
        data = datalist[i]
        for j in range(0,9):
            worksheet.write(i+1,j,data[j])
    workbook.save('douban.xls')
    print('xls保存完毕')

    return


if __name__ == '__main__':
    main()
