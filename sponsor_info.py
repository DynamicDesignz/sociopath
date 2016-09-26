import sys, os
from lxml import html
import requests
import unicodedata

#url = "http://www.thestudentroom.co.uk/showthread.php?t=2426280"
url = "https://www.google.com/?gws_rd=ssl#q="
related = []
queries = [
"Petco",
"Rita's",
"Dunkin Donuts",
"Farmer's Market",
"C2 Education"
]
for query in queries:
    print("[+] Requesting "+query+"...",end="")
    query = query.replace(' ','+')
    page = requests.get(url+query+"+livingston+nj")
    tree = html.fromstring(page.content)
    posts = tree.xpath('//a')
    for post in posts:
        body = post.text_content().encode('ascii','ignore').decode(sys.stdout.encoding)
        if "(" in body and ")" in body and "-" in body:
            related.append(body)
    print("Found "+len(posts)+" phone number(s).")
f = open("sponsor_results.html",'w')
body = ""
for post in related:
    body = body + post + "<br />"
f.write(body.encode('ascii','ignore').decode(sys.stdout.encoding))
f.close()