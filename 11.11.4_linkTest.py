# to check seek out <a href='xxx'> which are 'not Found 404' in certificated url

import bs4, requests
# todo: use beautifulsoup4 to seek out all <a> in url page ; (or use webdriver)
url = 'http://www.scut.edu.cn/new/'
res = requests.get(url)
res.raise_for_status()
res_soup = bs4.BeautifulSoup(res.text)
res_soup_a = res_soup.select('a[href]')
print('There are %d <a href=""> in %s' % (len(res_soup_a), url))

# todo: use requests to test the href in <a>; (or use webdriver.find_element)
for i in range(len(res_soup_a)):
    a_href_url = res_soup_a[i].get('href')
    if a_href_url.startswith("http:") or a_href_url.startswith('https:'):
        a_href_url_fullname = a_href_url
    else:
        a_href_url_fullname = 'http://www.scut.edu.cn/new/' + a_href_url.replace('/new/','')
    try:
        a_res = requests.get(a_href_url_fullname, timeout=0.1)
# if status_code == 404, write the url and tag_text in txt
        if a_res.status_code == 404:
            print('This url(%s) link to 404 not found... \n %s' % (res_soup_a[i].getText(),a_href_url))
    except requests.exceptions.Timeout:
        print('A url request over time...')

print('Done!')
