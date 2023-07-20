import urllib.request as req


def getData(url):
    request = req.Request(
        url,
        headers={
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
        },
    )
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    import bs4

    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")
    # push_num = root.find("div", class_="nrec").text.strip()

    push_nums = root.find_all("div", class_="nrec")

    for title, push_num in zip(titles, push_nums):
        if title.a != None and push_num != None:
            # title_text = title.a.string
            # articles_info.append({"title": title_text, "push_num": push_num})
            print(title.a.string, ",", push_num.text)

    nextLink = root.find("a", string="‹ 上頁")
    return nextLink["href"]


url = "https://www.ptt.cc/bbs/movie/index.html"
count = 0
while count < 3:
    url = "https://www.ptt.cc" + getData(url)
    count += 1
