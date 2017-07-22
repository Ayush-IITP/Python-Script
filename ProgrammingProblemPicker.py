import requests
import bs4
import re
import random
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 '
                         'Safari/537.36'}

URL = ["https://www.codechef.com/problems/easy/", "https://www.codechef.com/problems/medium/",
       "https://a2oj.com/category?ID=409", "https://a2oj.com/category?ID=410", "https://a2oj.com/category?ID=411",
       "https://www.hackerearth.com/practice/notes/getting-started-with-the-sport-of-programming/"]
codechef = re.compile(r'codechef')
codeforces = re.compile(r'a2oj')
hackerearth = re.compile(r'hackerearth')
spoj_check = re.compile(r'http://www.spoj.com/problems/.+/')

codechef_problem = []
a2oj_problem = []
spoj_problem = []
Todays_problem = []


def visit_codechef(soup):
    global codechef_problem
    Problem_block = soup.findAll('div', class_="problemname")
    # random.shuffle(Problem_block)
    for i in range(len(Problem_block)):
        codechef_problem += ["https://www.codechef.com" + str(Problem_block[i].a.get("href"))]
    random.shuffle(codechef_problem)
    '''for i in range(len(codechef_problem)):
        print(codechef_problem[i])'''


def visit_codeforces(soup):
    global a2oj_problem
    Table_block = soup.tbody.findAll('a')
    for i in range(0, len(Table_block), 2):
        a2oj_problem += [Table_block[i].get("href")]
    random.shuffle(a2oj_problem)
    '''for i in range(len(a2oj_problem)):
        print(a2oj_problem[i])'''


def visit_hackerearth(soup):
    global spoj_problem
    Anchor_block = soup.findAll('a')
    for i in range(len(Anchor_block)):
        if spoj_check.match(str(Anchor_block[i].get("href"))):
            spoj_problem += [Anchor_block[i].get("href")]
    spoj_problem = list(set(spoj_problem))
    random.shuffle(spoj_problem)
    '''for i in range(len(spoj_problem)):
        print(spoj_problem[i])'''


def generate_random_problem():
    global codechef_problem, spoj_problem, a2oj_problem
    global Todays_problem
    Todays_problem += codechef_problem + spoj_problem + a2oj_problem
    random.shuffle(Todays_problem)
    Todays_problem = random.sample(Todays_problem, k=5)


def main():
    for Problem_URL in URL:
        res = requests.get(Problem_URL, headers=headers)
        soup = bs4.BeautifulSoup(res.text, "lxml")
        # print(Problem_URL)
        if codechef.search(Problem_URL):
            visit_codechef(soup)
        if codeforces.search(Problem_URL):
            visit_codeforces(soup)
        if hackerearth.search(Problem_URL):
            visit_hackerearth(soup)
    generate_random_problem()
    res = requests.get("http://www.eduro.com/", headers=headers)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    # print(soup.dailyquote.div.p)
    '''for i in range(len(Todays_problem)):
        print(Todays_problem[i])'''
    os.chdir("/home/darkmatter/Desktop/")
    # print(os.listdir())
    fw = open("Problem.txt","w")
    fw.write("\n" + " "*15 + "Quote Of The day : ")
    fw.write(soup.dailyquote.div.p.string+"\n"*2)
    fw.write("*" * 200 + "\n"*2)
    for i in range(len(Todays_problem)):
        fw.write(" "*25 + Todays_problem[i] + "\n"*2)
        fw.write("*"*150 + "\n"*2)
    fw.close()


if __name__ == '__main__':
    main()
