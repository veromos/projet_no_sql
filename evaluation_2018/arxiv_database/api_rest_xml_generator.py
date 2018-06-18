import urllib.request
url = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=100'
data = urllib.request.urlopen(url).read()
with open("arxiv_small_dataset.xml",'wb') as f :
    f.write(data)
