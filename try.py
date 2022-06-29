import requests, time, json
from bs4 import BeautifulSoup


def req_func(link):
    r = requests.get(link, timeout=60)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "lxml")

    return soup


start_time = time.time()


soup = req_func("https://htf.mddirectsupply.com/shop-htf/")
# print(soup)
table = soup.find("table", id="wcpt_0fafa1e7552c1ad9_1")
# print(table.prettify())

a = table.find("thead")
a = a.find("tr")
a = a.find_all("th")
for x in a:
    print(x)


#     # insertion_sorting
# sorted_ncbi_dataset = {}
# list_a = ncbi_dataset['species']
# sorted_ncbi_dataset.setdefault("species", insertion_sort(list_a))
# file_name = 'ncbi_dataset_sorted_final.json'

# with open(file_name, 'w') as file:
#         json.dump(sorted_ncbi_dataset, file, indent=2)


# print('total species scraped: ' + str(len(sorted_ncbi_dataset['species'])))
# print(f'{file_name} is created on current working directory')

print("\n[Finished in %s s]" % (time.time() - start_time))
