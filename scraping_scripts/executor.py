from miningdotcom import miningdotcom
from utils.db_toolbox import db_toolbox, db_con
from utils.raw_html_getter import HtmlParser
from utils.config import config_dict
from utils.website_list import website_list
import os

# GET
insta = HtmlParser(website_list)
insta.html_getter()

relative_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(relative_path, "../html_bank/html_latest/")
html_bank = os.listdir(f"{path}")

scripts = [miningdotcom]
table = "articles"
columns = [
    "heading",
    "sub_heading",
    "author",
    "pub_date",
    "url",
    "website",
]

# WRITE
for func in scripts:
    for html in html_bank:
        if func.__name__ in html:
            values = func(html)
            con = db_con(config_dict)
            con.multiple_insert(table, columns, values)
            print("Executed:" + func.__name__)
