import requests
from company_info import Company
from lxml import etree
from lib.log import LogHandler

log = LogHandler(__name__)


class LagouForce:
    def __init__(self):
        self.source = '拉钩'
        self.url = 'https://www.lagou.com/gongsi/'
        proxy = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {"host": "http-dyn.abuyun.com",
                                                                "port": "9010",
                                                                "user": "HRH476Q4A852N90P",
                                                                "pass": "05BED1D0AF7F0715"}
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Cookie': 'JSESSIONID=ABAAABAAAFCAAEGF4C9B5389EE98C2E7DD54C8B8A1414A2; _ga=GA1.2.1366137308.1528449246; user_trace_token=20180608171516-75154e69-6afc-11e8-971a-525400f775ce; LGUID=20180608171516-7515518f-6afc-11e8-971a-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1529485519,1531191370; _gid=GA1.2.54377118.1531191370; index_location_city=%E5%8C%97%E4%BA%AC; LGSID=20180711150540-d1b43320-84d8-11e8-9a69-5254005c3644; TG-TRACK-CODE=index_navigation; SEARCH_ID=f9a229196ecf4bb9af91c7d37da83415; X_MIDDLE_TOKEN=0f7d2e0e5bed168eb564c8f8e97a9ded; X_HTTP_TOKEN=969ab535c830dee41a704cd5e7b48e80; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1531296958; LGRID=20180711161559-a4a4402d-84e2-11e8-9a69-5254005c3644'
        }
        self.proxies = {
            'http': proxy,
            'https': proxy,
        }

    def start_crawler(self):
        for i in range(3596, 300000):
            try:
                r = requests.get(self.url + str(i) + '.html', proxies=self.proxies, headers=self.headers)
                print(r.url)
                if 'login' in r.url:
                    print('登陆')
                elif '本网站的Coder和PM私奔啦~~~具体范围团结湖附近，想八卦请看' in r.text:
                    print('私奔啦')
                elif '这个公司的主页还在建设中…' in r.text:
                    print('建设中')
                else:
                    self.analyze_detail(r.text, str(i), r.url)
            except Exception as e:
                log.error('url = {}'.format(self.url + str(i) + '.html'))

    def analyze_detail(self, html, company_id, url):
        xpath_html = etree.HTML(html)
        company = Company(company_id=company_id, company_source=self.source)
        company.address = xpath_html.xpath('string(//*[@id="location_container"]/div[2]/div[2])').strip()
        company.company_info = xpath_html.xpath('string(//*[@id="company_intro"])').strip()

        company.company_short_info = xpath_html.xpath('/html/body/div[2]/div/div/div[1]/div/text()')[0].strip()
        company.city = xpath_html.xpath('//*[@id="basic_container"]/div[2]/ul/li[4]/span/text()')[0].strip()
        company.business = xpath_html.xpath('//*[@id="basic_container"]/div[2]/ul/li[1]/span/text()')[0].strip()
        company.development_stage = xpath_html.xpath('//*[@id="basic_container"]/div[2]/ul/li[2]/span/text()')[
            0].strip()
        company.company_name = xpath_html.xpath('/html/body/div[2]/div/div/div[1]/h1/a/text()')[0].strip()
        company.company_size = xpath_html.xpath('//*[@id="basic_container"]/div[2]/ul/li[3]/span/text()')[0].strip()
        company.url = url
        company.insert_db()
