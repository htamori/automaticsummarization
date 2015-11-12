from xml.dom import minidom

doc = minidom.parse("1815430.xml")

def getNodeText(node):

    nodelist = node.childNodes
    result = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            result.append(node.data)
    return ''.join(result)

title = doc.getElementsByTagName("title")[0]
print("Node Name : %s" % title.nodeName)
print("Node Value : %s \n" % getNodeText(title))


#bodycontents = doc.getElementsByTagName("body")
headline = doc.getElementsByTagName("hl1")[0]
print("Headline : %s \n" % getNodeText(headline))

blockcontents = doc.getElementsByTagName("full_text")
print len(blockcontents)
for blockcontent in blockcontents:
    print blockcontent
    #fulltext = blockcontent.attributeName
    print fulltext
    #texts = fulltext.getElementsByTagName("p")[0]
    #for text in texts:
        #print text
#for bodycontent in bodycontents:
#       headline = bodycontent.getAttribute("hl1")
        #sid = staff.getAttribute("id")
        #nickname = staff.getElementsByTagName("nickname")[0]
        #salary = staff.getElementsByTagName("salary")[0]
        #print("id:%s, nickname:%s, salary:%s" %
              #(sid, getNodeText(nickname), getNodeText(salary)))
#        print headline