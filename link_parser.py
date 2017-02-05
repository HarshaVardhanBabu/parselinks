import os
import urllib2
from HTMLParser import HTMLParser
# from html.entities import name2codepoint
url = r'https://ece.uwaterloo.ca/~dwharder/aads/Lecture_materials/'
class MyHTMLParser(HTMLParser):
    # links=[]
    link_dict={'.pdf':[],'.pptx':[]}
    def handle_starttag(self, tag, attrs):
    	# self.links=[]
        if(tag == "a"):
        	for attr in attrs:
        		if(attr[0]=="href"):
        			link = attr[1]
        			# self.links.append(link)
        			name,ext = os.path.splitext(link)
        			if(ext in self.link_dict.keys()):
        				self.link_dict[ext].append(os.path.join(url,link))

        			# for keys in self.link_dict.keys():

        			# if(ext == ".pdf"):
        			# 	self.link_dict['pdf'].append(os.path.join(url,link))
        			# elif(ext == '.pptx'):
        			# 	self.link_dict['pptx'].append(os.path.join(url,link))



    def handle_endtag(self, tag):
    	pass
        # print("End tag  :", tag)

    def handle_data(self, data):
    	pass
        # print("Data     :", data)

    def handle_comment(self, data):
    	pass
        # print("Comment  :", data)

    def handle_entityref(self, name):
    	pass
        pass
        # c = chr(name2codepoint[name])
        # print("Named ent:", c)

    def handle_charref(self, name):
    	pass
        # if name.startswith('x'):
            # c = chr(int(name[1:], 16))
        # else:
            # c = chr(int(name))
        # print("Num ent  :", c)

    def handle_decl(self, data):
    	pass
        # print("Decl     :", data)


def loadhtml(url):	
	response = urllib2.urlopen(url)
	html = response.read()
	return html
# def get_inks(html):
# 	pass
# def sep_links(links):
# 	pass
# def main(url):
# 	html = loadhtml(url)
# 	# links = get_links(html)
# 	# sep_links(links)
if __name__ == '__main__':
	# url = r'https://ece.uwaterloo.ca/~dwharder/aads/Lecture_materials/'
	parser = MyHTMLParser()
	outfile = r'Links.txt'
	html = loadhtml(url)
	parser.feed(html)
	# print(parser.link_dict)
	with open(outfile,'w') as writer:
		for key in parser.link_dict.keys():
			writer.write('\r\n'.join(parser.link_dict[key]))
			writer.write('\r\n')
	print("Links are avilable in %s"%(outfile))
	#main(url)
