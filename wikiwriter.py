def wikiGet(topic):
    import requests
    from bs4 import BeautifulSoup
    import re


    url = "https://en.wikipedia.org/wiki/" + topic
    print(url)

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    ps = soup.findAll('p')
    ps = [i.getText() for i in ps]
    ps = [re.sub("[\(\[].*?[\)\]]", "", x) for x in ps]
    ps.pop(0)
    ps.pop(0)
    ps.pop(0)
    ps = ' '.join([str(elem) for elem in ps])

    print(ps)
    return ps