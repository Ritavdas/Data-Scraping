import pprint

import requests
from bs4 import BeautifulSoup

for i in range(1, 100):
    res = requests.get("https://news.ycombinator.com/news?p={pagenum}".format(pagenum=i))
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup.find(id="score_22873298"))
    links = soup.select('.storylink')
    subtext = soup.select('.subtext')


    # print(votes[0])
    def sort_stories_by_votes(hnList):
        return sorted(hnList, key=lambda k: k['votes'], reverse=True)


    def create_custom_hackerNews(links, subtext):
        HackerNews = []
        for idx, item in enumerate(links):
            title = links[idx].getText()
            href = links[idx].get('href', None)
            vote = subtext[idx].select('.score')
            if len(vote):
                points = int(vote[0].getText().replace(' points', ''))
                if points > 99:
                    # print(points)
                    HackerNews.append({'title': title, 'link': href, 'votes': points})
        return sort_stories_by_votes(HackerNews)


    pprint.pprint(create_custom_hackerNews(links, subtext))
