** This is versace.com scraper

1. All products of all categories were collected by
two regions USA and France.
2. It was made a test of the scan result for% content filling,
 to some collection items
---

## Description, solving

- 1)Start pages were set for data extraction (any region can be selected)
- 2)All product categories presented on the site were extracted
- 3)In the categories on the page only 24 products are displayed (but in the product category there are more, for example, 100), if you scroll down, links will appear on the network, these links were -also extracted.
- 4)All links to all products from the given category were got.
- 5)Data from the product page was extracted

---

## Extracted Data

- name
- price
- currency (USD, EUR)
- category (hierarchy)
- product scan time
- color
- the size
- region
- product description (description)
- product url

---

## Extracted Data from versace.com stored at versace/versace.csv

---

## Clone a repository

git clone https://sanekua@bitbucket.org/sanekua/scrapy.git

- Install the requirements:

- pip install -r requirements.txt

- scrapy crawl versace_spider

- tests result saved at versace.json
