# bosszhipin
my project about BossZhipin
from selenium import webdriver
from lxml import etree
import time
def get_detail_url(driver):
    html = etree.HTML(driver.page_source)
    href = html.xpath('//div[@class="job-primary"]/div[1]/h3/a[1]/@href')
    hrefs = []
    for each in href:
        each = 'https://www.zhipin.com/' + each
        hrefs.append(each)
    return hrefs
def parse_detail_url(driver):
    career = {}
    html = etree.HTML(driver.page_source)
    job = html.xpath('//div[@class="name"]/h1/text()')[0]
    salary = html.xpath('//div[@class="name"]/span/text()')[0]
    welfare = html.xpath('//div[@class="job-tags"][1]/span/text()')
    i = len(welfare)
    i = (int(i)/2)
    welfares = welfare[0:int(i)]
    era =  html.xpath('//div[@class="info-primary"]/p[1]/text()')[0]
    year = html.xpath('//div[@class="info-primary"]/p[1]/text()')[1]
    education = html.xpath('//div[@class="info-primary"]/p[1]/text()')[2]
    career['job'] = job
    career['salary'] =salary
    career['welfare']=welfares
    career['era']=era
    career['year']=year
    career['education']=education
    descripe = html.xpath('//div[@class="job-sec"]/div[@class="text"]/text()')
    descripes = []
    for each in descripe:
        each = each.strip()
        descripes.append(each)
    career['job_descripe']=descripes
    introduction = html.xpath('//div[@class="job-sec company-info"]/div[@class="text"]/text()')
    introductions = []
    for each in introduction:
        each = each.strip()
        introductions.append(each)
    career['firm_introduction']=introductions
    print(career)
def spider():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.zhipin.com/?sid=sem_pz_bdpc_dasou_title')
    inputTag = driver.find_element_by_class_name('ipt-search')
    inputTag.send_keys('python')
    time.sleep(3)
    submitBtn = driver.find_element_by_xpath('//div[@class="search-form "]//button')
    submitBtn.click()
    time.sleep(3)
    submitBtn1 = driver.find_element_by_xpath('//dd[@class="city-wrapper"]//a[6]')
    submitBtn1.click()
    def parse_one_page():
        hrefs = get_detail_url(driver)
        for each in hrefs:
            driver.execute_script('window.open("https://www.baidu.com/")')
            driver.switch_to_window(driver.window_handles[1])
            time.sleep(2)
            driver.get(each)
            parse_detail_url(driver)
            time.sleep(1)
            driver.close()
            break
    print(1)
    parse_one_page()
    driver.switch_to_window(driver.window_handles[0])
    for x in range(2,6):
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        submitBtn2 = driver.find_element_by_xpath('//a[@ka="page-next"]')
        submitBtn2.click()
        time.sleep(1)
        print(x)
        parse_one_page()
        driver.switch_to_window(driver.window_handles[0])
    time.sleep(3)
    driver.close()

if __name__ == '__main__':
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("excludeSwitches", ['enable-automation'])
    # driver = webdriver.Chrome(options=options)
    # driver.get('https://www.zhipin.com/job_detail/5123950f3d1c20851nZz29-4EFc~.html?ka=search_list_1')
    # parse_detail_url(driver)
    # time.sleep(3)
    # driver.close()
    spider()
