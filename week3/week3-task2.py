import urllib.request as req
import bs4


def getData(url, output_file):
    request = req.Request(
        url,
        headers={
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
        },
    )
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")
    push_nums = root.find_all("div", class_="nrec")

    for title, push_num in zip(titles, push_nums):
        if title.a != None and push_num != None:
            title_text = title.a.string
            push_text = push_num.text.strip()
            if push_text.isdigit():
                push_num_int = int(push_text)
            else:
                push_num_int = 0

            article_link = title.a["href"]
            full_link = "https://www.ptt.cc" + article_link
            date = get_article_date(full_link)
            with open(output_file, "a", encoding="utf-8") as file:
                file.write(f"{title_text}, {push_num_int}, {date}\n")
            # print(title_text, ",", push_num_int, ",", date)

    nextLink = root.find("a", string="‹ 上頁")
    return nextLink["href"]


def get_article_date(article_url):
    request = req.Request(
        article_url,
        headers={
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36"
        },
    )
    with req.urlopen(request) as response:
        article_data = response.read().decode("utf-8")

    article_root = bs4.BeautifulSoup(article_data, "html.parser")
    main_content = article_root.find("div", id="main-content")
    date_element = main_content.find_all("span", class_="article-meta-value")

    if date_element:
        date = date_element[3].string
    return date


output_file = "movie.txt"
url = "https://www.ptt.cc/bbs/movie/index.html"
count = 0
while count < 3:
    url = "https://www.ptt.cc" + getData(url, output_file)
    count += 1
