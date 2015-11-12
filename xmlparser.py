# -*- coding: utf-8 -*-
from xml.etree.ElementTree import *

def xmlparser(filename):
    tree = parse(filename) # 返値はElementTree型
    elem = tree.getroot() # ルート要素を取得(Element型)

    ret = {}
    fulltext = ""
    for e in elem.findall(".//body.content/block[@class='full_text']/p"):
        fulltext = fulltext + " " + e.text
    ret["fulltext"] = fulltext

    ret["id"] = elem.find(".//docdata/doc-id").get("id-string")
    ret["title"] = elem.find(".//body.head/hedline/hl1").text

    return ret

#print xmlparser("1815430.xml")
