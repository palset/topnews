import urllib
response = urllib.urlopen('http://www.ndtv.com/latest')
html = response.read()
base="nstory_header"
links_list=[]
links_name=[]
while html.find(base)!= -1:
	html=html[html.find(base):]
	hrefend=html.find('title')
	hrefend=hrefend-2
	hrefstart=html.find(base)+24
	links_list.append("<a href=\""+html[hrefstart:hrefend]+'\">')
	links_name.append(html[hrefstart:hrefend])
	html=html[hrefend:]
html_str="""
<html>
<body>
"""
while links_list != []:
	link=links_list.pop()
	html_str=html_str+link+links_name.pop()+'<//a><br>'
html_str=html_str+"</body></html>"
Html_file= open("\index.html","w")
Html_file.write(html_str)
Html_file.close()