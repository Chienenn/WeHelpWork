# 發requests 取得原始碼
from bs4 import BeautifulSoup as bs
import requests

url = "https://www.ptt.cc/bbs/movie/index.html"
headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
}
# 文章標題[問片]xxx,推文數,詳細時間資料
res = requests.get(url, headers=headers)

# 利用 beautifulsoup 做html解析
soup = bs(res.text, "lxml")
data = soup.select("div.r-ent")
print(soup)
print("*" * 50)
# 取得分頁的語法
previous_page = soup.select("div#action-bar-container div.btn-group-paging a")[1][
    "href"
]
previous_page = "https://www.ptt.cc/" + previous_page
# print(previous_page)

page_num = previous_page.replace("https://www.ptt.cc//bbs/movie/index", "").replace(
    ".html", ""
)
# print(page_num)
for i in range(3):
    print("https://www.ptt.cc//bbs/movie/index{}.html".format(int(page_num) - i))


# 抓去前五頁文章列表資料
def get_parsing_data(soup):
    # def get_each_post_timestamp(url):

    data = soup.select("div.r-ent")
    result = []

    for sample in data:
        title = sample.select("div.title")[0].text.strip()

        if "刪除" in title:
            continue

        push_num = (
            sample.select("div.nrec")[0].text
            if len(sample.select("div.nrec")) > 0
            else 0
        )

        raw_link = sample.select("div.title a")[0]["href"]
        domain_name = "https://www.ptt.cc"
        link = domain_name + raw_link
        # print("連結：", link)

        result.append({"title": title, "push_num": push_num, "link": link})
    return result


get_parsing_data(soup)

# 解析首頁資料
output = []
result = get_parsing_data(soup)
output += result

# 抓取分頁資料
for i in range(3):
    url = "https://www.ptt.cc//bbs/movie/index{}.html".format(int(page_num) - i)
    res = requests.get(url, headers=headers)
    soup = bs(res.text, "lxml")

    result = get_parsing_data(soup)
    output += result

    print("{} is ok.".format(url))

print(output)

raw_link = soup.select("div.title a")[0]["href"]
domain_name = "https://www.ptt.cc"
link = domain_name + raw_link

rs = requests.session()
response = rs.get(link)
result = bs(response.text, "html.parser")

main_content = result.find("div", id="main-container")
article_info = main_content.find_all("span", class_="article-meta-value")

if len(article_info) != 0:
    author = article_info[0].string  # 作者
    title = article_info[2].string  # 標題
    time = article_info[3].string  # 時間
else:  # 避免有沒有資訊的狀況
    author = "無"  # 作者
    title = "無"  # 標題
    time = "無"  # 時間
print("*" * 50)
print(article_info)

for ele in soup:
    print(article_info)


# data = soup.select("div.r-ent")  # 抓取r-ent 裡面會有標題 推文數...
# print(data[1])

# for ele in data:
#     # print(ele)
#     title = ele.select("div.title")[0].text.strip()  # 去頭去尾,不然取出的資料有空格
#     print("標題", title)
#     print("-" * 100)


## 解析標題/時間/推文/連結
# sample = data[2]  # data0 是第一筆文章資料的全部（div的r-ent）

# for sample in data:
#     # 標題
#     title = sample.select("div.title")[0].text.strip()  # 取出的都是array
#     # print(sample)
#     print("標題", title)  # [新聞] xxxxx

#     # # 時間
#     # time = sample.select("div.date")[0].text.strip()
#     # print("時間", time)

#     # 推文數 (span class="hl f3")
#     push_num = sample.select("div.nrec")[0].text
#     if push_num:
#         print("推文數", push_num)
#     else:
#         print("推文數：無")

#     # 網址
#     raw_link = sample.select("div.title a")[0]["href"]
#     domain_name = "https://www.ptt.cc"
#     link = domain_name + raw_link
#     print(
#         "連結：", link
#     )  # /bbs/movie/M.1689609375.A.215.html 抓出的只有路徑值,要變成可以點下去的連接,需要自己加路徑值

#     print("-" * 100) 9607 9606


for sample in data:
    title = sample.select("div.title")[0].text.strip()
    push_num = sample.select("div.nrec")[0].text.strip()
    if push_num == "":
        print(title, ",", "無")
    else:
        print(title, ",", push_num)
    # print(title, ",", push_num)
