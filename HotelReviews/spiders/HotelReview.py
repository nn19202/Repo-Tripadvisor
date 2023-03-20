import scrapy
from ..items import HotelreviewsItem

from selenium import webdriver
from scrapy.selector import Selector
from selenium.webdriver.common.by import By
from scrapy.utils.project import get_project_settings
import time

class HotelreviewSpider(scrapy.Spider):
    name = 'HotelReview'
    allowed_domains = ['tripadvisor.com.vn']
    start_urls = ['https://www.tripadvisor.com.vn/Hotel_Review-g298085-d302750-Reviews-Furama_Resort_Danang-Da_Nang.html']

    def parse(self, response):
        settings = get_project_settings()
        driver_path = settings['CHROME_DRIVER_PATH']
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('disable-popup-blocking')
        options.add_argument('--log-level=1')
        driver = webdriver.Chrome(driver_path,options=options)
        driver.get(response.url)
        time.sleep(3)

        #Duyệt toàn bộ trang web
        while True:
            h_url = driver.current_url
            h_reviewer_name = 'NA'
            #h_reviewer_id = 'NA'
            h_comment_date = 'NA'
            h_rating = 'NA'
            h_title_comment = 'NA'
            h_content_comment = 'NA'
            h_reviewer_staydate = 'NA'
            h_trip_type = 'NA'
            #click vào expand
            try:
                driver.find_element(By.XPATH, '//div[@data-test-target="expand-review"]').click()
                time.sleep(3)
            except:
                item = HotelreviewsItem()
                item['h_url'] = h_url
                item['h_reviewer_name'] = h_reviewer_name
                #item['h_reviewer_id'] = h_reviewer_id
                item['h_comment_date'] = h_comment_date
                item['h_rating'] = h_rating
                item['h_title_comment'] = h_title_comment
                item['h_content_comment'] = h_content_comment
                item['h_reviewer_staydate'] = h_reviewer_staydate
                item['h_trip_type'] = h_trip_type
                yield item
            #lấy thông tin đưa vào các biến
            #lấy thống tin của các comment
            try:
                comments = driver.find_elements(By.XPATH, '//div[@data-test-target="HR_CC_CARD"]')
                num_comment_items = min(len(comments),5)

            except:
                item = HotelreviewsItem()
                item['h_url'] = h_url
                item['h_reviewer_name'] = h_reviewer_name
                #item['h_reviewer_id'] = h_reviewer_id
                item['h_comment_date'] = h_comment_date
                item['h_rating'] = h_rating
                item['h_title_comment'] = h_title_comment
                item['h_content_comment'] = h_content_comment
                item['h_reviewer_staydate'] = h_reviewer_staydate
                item['h_trip_type'] = h_trip_type
                yield item

            #duyệt tát cả các comment => đưa giá trị vào các biến
            for j in range(num_comment_items):
                try:
                    h_reviewer_name = comments[j].find_element(By.XPATH, './/a[@class="ui_header_link uyyBf"]').text

                except:
                    h_reviewer_name = 'NA'
                # try:
                #     h_reviewer_id = comments[j].find_element(By.XPATH, './/')
                # except:
                #     h_reviewer_id = 'NA'
                try:
                    h_comment_date = comments[j].find_element(By.XPATH, './/div[@class="cRVSd"]/span').text
                    h_comment_date = h_comment_date.replace("đã viết đánh giá vào","")
                except:
                    h_comment_date = 'NA'
                try:
                    h_rating = comments[j].find_element(By.XPATH, './/div[@class="Hlmiy F1"]/span').get_attribute('class')
                    h_rating = h_rating.replace('ui_bubble_rating bubble_','')
                except:
                    h_rating = 'NA'
                try:
                    h_title_comment = comments[j].find_element(By.XPATH, './/a[@class="Qwuub"]/span').text
                except:
                    h_title_comment = 'NA'
                try:
                    h_content_comment = comments[j].find_element(By.XPATH, './/q[@class="QewHA H4 _a"]/span').text
                except:
                    h_content_comment = 'NA'
                try:
                    h_reviewer_staydate = comments[j].find_element(By.XPATH, './/span[@class="teHYY _R Me S4 H3"]').text
                    h_reviewer_staydate = h_reviewer_staydate.replace("Ngày lưu trú:","")
                except:
                    h_reviewer_staydate = 'NA'
                try:
                    h_trip_type = comments[j].find_element(By.XPATH, './/span[@class="TDKzw _R Me"]').text
                    h_trip_type = h_trip_type.replace("Loại chuyến đi:","")
                except:
                    h_trip_type = 'NA'

                item = HotelreviewsItem()
                item['h_url'] = h_url
                item['h_reviewer_name'] = h_reviewer_name
                #item['h_reviewer_id'] = h_reviewer_id
                item['h_comment_date'] = h_comment_date
                item['h_rating'] = h_rating
                item['h_title_comment'] = h_title_comment
                item['h_content_comment'] = h_content_comment
                item['h_reviewer_staydate'] = h_reviewer_staydate
                item['h_trip_type'] = h_trip_type
                yield item

            #nhấn nút tiếp theo
            try:
                driver.find_element(By.XPATH, '//a[@class="ui_button nav next primary "]').click()
                time.sleep(3)
            except:
                break
        #khi việc crawl hoàn tất
        driver.quit()

        
        pass
