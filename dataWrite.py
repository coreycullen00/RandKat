
import requests

# Catching errors
try:
    from bs4 import BeautifulSoup
except ImportError:
    sys.exit("""You need BeautifulSoup. run \'pip install bs4\'""")

try:
    from fake_useragent import UserAgent
except ImportError:
    sys.exit("""You need UserAgent. run \'pip install fake-useragent\'""")

file = open("data.txt", "wb")



end = False

pages = 0

while end is False and pages <= 27:
    url = 'https://open.kattis.com/problems?page=' + str(pages) + '&order=problem_difficulty'
    print(pages)
    pages = pages + 1

    usa = UserAgent()
    page = requests.get(url, headers={'User-Agent': str(usa.random)})
    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find('table', attrs={
                      'class': 'problem_list table sortable table-responsive table-kattis center table-hover table-multiple-head-rows table-compact'})

    if table is None:
        end = True
        break

    tbody = table.find('tbody')
    questions = tbody.find_all('tr')

    for tr in questions:
        tds = tr.find_all('td')

        dif = str(tds[8].text)
        dif = dif[-3:]
        diff =float(dif)
        upbound = 9.9
        problemId = (tds[0].find('a')['href'])


        def find_2nd(string, substring):
            return string.find(substring, string.find(substring) + 1)



        secondOccur = find_2nd(problemId,'/')


        

        scale = len(problemId)-secondOccur -1

        
        problemId = problemId[-scale:]

        if diff >= upbound:
            end = True
            break

        else:
            title = (tds[0].text.strip())
            dif = dif.strip()
            line =title + "," + dif + "," + problemId + "\n"
            file.write(line.encode('utf-8'))


file.close()
print("finished")


