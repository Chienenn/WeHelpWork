import json
import urllib.request
import csv
import re


url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
response = urllib.request.urlopen(url)
data = json.load(response)


station_dict = {}

for item in data["result"]["results"]:
    mrt = item.get("MRT")
    name = item["stitle"]

    if mrt in station_dict:
        station_dict[mrt].append(name)
    else:
        station_dict[mrt] = [name]

station_dict = {key: value for key, value in station_dict.items() if key is not None}

mrt_data = []
for area in station_dict:
    # attractions = ",".join(station_dict[area])
    attractions = station_dict[area]

    mrt_data.append([area, attractions])

print(mrt_data)

attraction_data = []
for item in data["result"]["results"]:
    name = item["stitle"]
    address = item["address"][5:8]
    longitude = item["longitude"]
    latitude = item["latitude"]
    picture = item["file"]

    pattern = r"https://[\w./-]+\.jpg"
    first_url = re.search(pattern, picture, re.IGNORECASE)
    first_url = first_url.group()

    attraction_data.append([name, address, longitude, latitude, first_url])


def j_attractions(attractions):
    return ",".join(attractions).replace(" ", "").replace('"', "")


with open("mrt.csv", mode="w", encoding="utf-8", newline="") as mrt_file:
    mrt_writer = csv.writer(mrt_file, csv.QUOTE_NONE, escapechar="")
    mrt_writer.writerow(["捷運站", "景點名稱"])
    for area, attractions in mrt_data:
        attractions_str = j_attractions(attractions)
        mrt_file.write(f"{area},{attractions_str}\n")


with open("attraction.csv", mode="w", encoding="utf-8", newline="") as attraction_file:
    attraction_writer = csv.writer(attraction_file)
    attraction_writer.writerow(["景點名稱", "區域", "經度", "緯度", "圖片網址"])
    attraction_writer.writerows(attraction_data)
