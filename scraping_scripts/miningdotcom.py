from bs4 import BeautifulSoup
from datetime import datetime
from utils.cleanse import unique
import re
import os


def miningdotcom(html_name):
    relative_path = os.path.abspath(os.path.dirname(__file__))
    source_html = os.path.join(relative_path, f"../html_bank/html_latest/{html_name}")
    soup = BeautifulSoup(open(source_html), "html.parser")
    html_selection = soup.findAll(class_="row")
    compiled_dictionary = {
        "heading": [],
        "sub_heading": [],
        "unique_text": [],
        "author": [],
        "pub_date": [],
        "url": [],
        "website": [],
    }

    ### Headers
    for tag in html_selection:
        sub_selection = tag.find_all(re.compile("^h[1-6]$"))
        for tag in sub_selection:
            sub_selection_string = tag.text
            if "SIGN UP FOR OUR DAILY NEWSLETTER" in sub_selection_string:
                pass
            else:
                compiled_dictionary["heading"].append(sub_selection_string.strip())

    ### Excerpts
    for tag in html_selection:
        sub_selection = tag.find_all("div", {"class": "post-excerpt"})
        for tag in sub_selection:
            sub_selection_string = tag.text
            compiled_dictionary["sub_heading"].append(sub_selection_string.strip())

    ### Author and Date
    for tag in html_selection:
        sub_selection = tag.find_all("div", {"class": "post-meta"})
        for tag in sub_selection:
            sub_selection_string = tag.text
            c_split = sub_selection_string.split("|")
            date_pre_formatted = []
            datetime_objects = []
            date = []
            date_pre_formatted.append(c_split[1])
            for i in date_pre_formatted:
                datetime_objects.append(datetime.strptime(i, " %B %d, %Y "))
            for i in datetime_objects:
                date.append(i.strftime("%Y-%m-%d"))

            compiled_dictionary["author"].append(str(c_split[0]).strip())
            compiled_dictionary["pub_date"].append(str(date[0]).strip())

    ### Link
    for tag in html_selection:
        sub_selection = tag.find_all("div", {"class": "img-content"}, "href")
        for tag in sub_selection:
            sub_sub_selection = tag.find("a")
            sub_sub_selection_string = sub_sub_selection.get("href")
            compiled_dictionary["url"].append(sub_sub_selection_string)

    ### Website
    website = ["www.mining.com" for x in compiled_dictionary["url"]]
    for entry in website:
        compiled_dictionary["website"].append(entry)

    ### Compiled Queryo
    query_list = list(
        zip(
            compiled_dictionary["heading"],
            compiled_dictionary["sub_heading"],
            compiled_dictionary["unique_text"],
            compiled_dictionary["author"],
            compiled_dictionary["pub_date"],
            compiled_dictionary["url"],
            compiled_dictionary["website"],
        )
    )

    return query_list
