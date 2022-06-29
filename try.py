import requests, time, json
from bs4 import BeautifulSoup


def req_func(link):
    r = requests.get(link, timeout=60)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "lxml")

    return soup


start_time = time.time()

dataset = {"data" : list()}
item = dict()

#main
soup = req_func("https://htf.mddirectsupply.com/shop-htf/")
# print(soup.prettify())
table = soup.find("table", id="wcpt_0fafa1e7552c1ad9_1")
# print(table.prettify())

# finding all thead values for data incoming testing
tr = table.thead.find('tr')
th_all = tr.find_all("th")
th_list = list()
for th in th_all:
    # print(th)
    th_list.append(th.text)
# removing last item as its empty
th_list.pop()
# print(th_list)

# navigating & extracting table datam row wise
tr_all = table.tbody.find_all('tr')
for tr_row in tr_all:
    tr_row.find_all('td')
    raw_data = list()
    for td in tr_row:
        # print(td)
        raw_data.append(td.text.strip())

    raw_data.pop() # removing last col
    raw_data[-1] = raw_data[-1].split(" ")[0] # taking only number string for stock
    # print(raw_data)
    item["name"] = raw_data[0]
    item["sku"] = raw_data[1]
    item["summary"] = raw_data[2]
    item["price"] = raw_data[3]
    item["stock"] = raw_data[4]
    # print(item)
    dataset["data"].append(item)

print(dataset)

file_name = 'table_dataset.json'

with open(file_name, 'w') as file:
        json.dump(dataset, file, indent=2)


print('total table row scraped: ' + str(len(dataset['data'])))
print(f'{file_name} is created on current working directory')

print("\n[Finished in %s s]" % (time.time() - start_time))
