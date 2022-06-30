from lib2to3.pgen2 import driver
from tkinter import SEL
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep

class craigslist_crawler(object):
    def __init__(self, url):
        self.url = url
        self.browser = webdriver.Chrome("./chromedriver")

    def load_page(self,name):
        name = name + '.txt'
        file_data = open(name, "a") 
        #mo trang web
        browser = self.browser
        browser.get(self.url)
        sleep(1)

        #mo cac comment
        comment_links = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/div/div[2]/div/div[3]/div[2]/div[1]/div[2]/div/div[2]/div[2]/div[7]")
        comment_links.click()
        title = comment_links.text
        title = title.split("(")[1]
        num_comment = int(title.split(")")[0])
        sleep(1)

        i = 0 

        while(i<num_comment):

            if(i != 0):
                next_button = browser.find_element_by_xpath("//button[@class='shopee-icon-button shopee-icon-button--right ']")
                next_button.click()
                sleep(1)


            commnent_list = browser.find_elements_by_xpath("//div[@class='shopee-product-rating__main']")
            for comment in commnent_list:
                i = i+1
                stars = comment.find_elements_by_css_selector('.icon-rating-solid')
                content_list = comment.find_element_by_class_name("Em3Qhp")
                file_data.write(len(stars), content_list.text)
                print(i)

        file_data.close()
        browser.close()                    
        

if __name__ == "__main__":
    urls = [
        # Thoi trang nam
        ["ao_khoac_nam", f"https://shopee.vn/-Si%C3%AAu-nh%E1%BA%B9_-C%C3%B3-m%C5%A9-th%C3%A1o-r%E1%BB%9Di-%C3%81o-Phao-Nam-Si%C3%AAu-Nh%E1%BA%B9-2-m%E1%BA%B7t-kho%C3%A1c-nam-si%C3%AAu-nh%E1%BA%B9-%C3%81o-Kho%C3%A1c-L%C3%B4ng-V%C5%A9-pha-Tr%E1%BA%A7n-B%C3%B4ng-C%C3%B3-4-t%C3%BAi-i.177129862.3506879259?sp_atk=9af18542-9eba-454d-b654-17aedf6e823e&xptdk=9af18542-9eba-454d-b654-17aedf6e823e"],
        ["ao_vest_nam", f"https://shopee.vn/%C3%81o-blazer-nam-chumi-2-l%E1%BB%9Bp-d%C3%A0y-d%E1%BA%B7n-form-r%E1%BB%99ng-d%C3%A1ng-unisex-ad006-i.423838298.8075652768?sp_atk=166c972c-075e-41f6-878a-2d36e5f05979&xptdk=166c972c-075e-41f6-878a-2d36e5f05979"],
        ["ao_hoodie_nam", f"https://shopee.vn/%C3%81o-Hoodie-Th%E1%BB%9Di-Trang-Thu-%C4%90%C3%B4ng-Full-Size-Nhi%E1%BB%81u-M%C3%A0u-T%C3%B9y-Ch%E1%BB%8Dn-Cho-Nam-V%C3%A0-N%E1%BB%AF-Shop-B%E1%BA%A2O-B%E1%BA%A2O-MAN-i.474518696.12862316254?sp_atk=f6e44b01-afb2-405c-a83b-063720c3d34b&xptdk=f6e44b01-afb2-405c-a83b-063720c3d34b"],
        ["quan_jeans_nam", f"https://shopee.vn/Qu%E1%BA%A7n-shorts-jeans%E2%9D%A4FREESHIP-%E2%9D%A4qu%E1%BA%A7n-short-chu%E1%BA%A9n-tem-m%C3%A1c-big-size-c%E1%BB%B1c-%C4%91%E1%BA%B9p-cao-c%E1%BA%A5p-i.17014332.4153779491?sp_atk=050d9141-6a5d-4cb5-851b-3c454c2cbad1&xptdk=050d9141-6a5d-4cb5-851b-3c454c2cbad1"],
        ["quan_au_nam", f"https://shopee.vn/Qu%E1%BA%A7n-Th%E1%BB%83-Thao-Nam-3-S%E1%BB%8Dc-Qu%E1%BA%A7n-Nam-Thu-%C4%90%C3%B4ng-Co-Gi%C3%A3n-%E1%BB%90ng-Su%C3%B4ng-%E1%BB%90ng-C%C3%B4n-i.45702547.2844240480?sp_atk=d7f53767-7a8a-4530-aa06-69077111ba7d&xptdk=d7f53767-7a8a-4530-aa06-69077111ba7d"],
        ["quan_short_nam", f"https://shopee.vn/Qu%E1%BA%A7n-%C4%90%C3%B9i-Nam-Th%E1%BB%83-Thao-M%E1%BA%B7c-Nh%C3%A0-Cao-C%E1%BA%A5p-Gi%C3%A1-R%E1%BA%BB-V%E1%BA%A3i-Gi%C3%B3-M%E1%BA%B7c-M%C3%B9a-H%C3%A8-M%C3%A1t-M%E1%BA%BB-VESCA-H5-i.364598436.8554759064?sp_atk=d6b7efa0-87e1-4180-b075-5e303f819e88&xptdk=d6b7efa0-87e1-4180-b075-5e303f819e88"],
        ["ao_nam", f"https://shopee.vn/%C3%81o-s%C6%A1-mi-gi%C3%A1-r%E1%BA%BB-h%C3%A0n-qu%E1%BB%91c-cao-c%E1%BA%A5p-tr%E1%BA%BB-trung-tr%C6%A1n-nam-SINO-SM08-i.98173977.7803585798?sp_atk=c8dbd27c-5dc9-4d3d-b5e1-9a00fddcb01a&xptdk=c8dbd27c-5dc9-4d3d-b5e1-9a00fddcb01a"],
        ["ao_ba_lo_nam", f"https://shopee.vn/%C3%81O-L%C3%93T-NAM-BA-L%E1%BB%96-CAO-C%E1%BA%A4P-TL010110-i.13105846.4847805933?sp_atk=51102d1f-f757-4dac-bbc9-c8b805f5aad7&xptdk=51102d1f-f757-4dac-bbc9-c8b805f5aad7"],
        ["do_lot_nam", f"https://shopee.vn/Qu%E1%BA%A7n-l%C3%B3t-nam-tam-gi%C3%A1c-s%E1%BB%8Bp-l%C6%B0%E1%BB%9Bi-th%C3%B4ng-h%C6%A1i-tho%C3%A1ng-kh%C3%AD-kh%C3%A1ng-khu%E1%BA%A9n-co-gi%C3%A3n-h%C3%A0ng-%C4%91%E1%BA%B9p-i.162885508.3229327876?sp_atk=75f97d0a-d4b3-4d05-a6e8-abe64b5e1da5&xptdk=75f97d0a-d4b3-4d05-a6e8-abe64b5e1da5"],
        ["do_ngu_nam", f"https://shopee.vn/B%E1%BB%99-Pijama-%C3%81o-D%C3%A0i-Tay-C%E1%BB%95-B%E1%BA%BB-Qu%E1%BA%A7n-D%C3%A0i-i.290961182.3949962481?sp_atk=6c75af0f-a502-48e2-9ad1-0282e87e3124&xptdk=6c75af0f-a502-48e2-9ad1-0282e87e3124"],
        ["do_bo_nam", f"https://shopee.vn/%C3%81O-C%E1%BA%B6P-M%C3%80U-%C4%90EN-L%C3%94NG-V%C5%A8-%C4%90%E1%BA%B8P-i.85331313.4867431811?sp_atk=7a3b1b84-ef89-433e-9770-9894224f1a9e&xptdk=7a3b1b84-ef89-433e-9770-9894224f1a9e"],
        ["tat_nam", f"https://shopee.vn/-lo%E1%BA%A1i-1-t%E1%BA%A5t-nam-c%E1%BB%95-ng%E1%BA%AFn-h%C3%A0ng-d%C3%A0y-%C4%91%E1%BA%B9p-i.28744924.1349534856?sp_atk=27d3b3f2-2532-4f46-a6b3-b986f5ea25dd&xptdk=27d3b3f2-2532-4f46-a6b3-b986f5ea25dd"],
        ["truyen_thong_nam", f"https://shopee.vn/B%E1%BB%99-PIZAMA-hoa-qu%E1%BA%A3-ZXU728-i.7782867.2136765052?sp_atk=eca14596-f587-403c-ba0a-e06bc30ed367&xptdk=eca14596-f587-403c-ba0a-e06bc30ed367"],
        ["hoa_trang_nam", f"https://shopee.vn/M%C5%A9-Bucket-Adidas-Full-Tag-Code-Ch%E1%BA%A5t-V%E1%BA%A3i-Kali-D%E1%BA%A7y-D%E1%BA%B7n-Th%E1%BA%A5m-M%E1%BB%93-H%C3%B4i-T%E1%BB%91t-Freesize-i.15655336.6936893141?sp_atk=37b4c635-2bfc-4a6b-b39e-1dcd0b650926&xptdk=37b4c635-2bfc-4a6b-b39e-1dcd0b650926"],
        ["nganh_nam", f"https://shopee.vn/Qu%E1%BA%A7n-%C3%81o-B%E1%BA%A3o-H%E1%BB%99-Lao-%C4%90%E1%BB%99ng-C%C3%B4ng-Nh%C3%A2n-Qu%E1%BA%A7n-%C3%81o-Kaki-Nam-%C4%90%E1%BB%8Bnh-i.144103267.2180779041?sp_atk=9c6d0c1f-162d-48d6-a218-5f4f0434ecef&xptdk=9c6d0c1f-162d-48d6-a218-5f4f0434ecef"],
        ["trang_suc_nam", f"https://shopee.vn/Set-2-V%C3%B2ng-Tay-Cho-C%E1%BA%B7p-%C4%90%C3%B4i-C%C3%B3-Kh%C3%B3a-T%E1%BB%AB-T%C3%ADnh-i.164772488.7478312242?sp_atk=88625514-7ae0-40b6-a2d3-dcccbc4b825f&xptdk=88625514-7ae0-40b6-a2d3-dcccbc4b825f"],
        ["kinh_mat_nam", f"https://shopee.vn/-K%C3%8DNH-NAM-K%C3%8DNH-M%C3%81T-R%C3%82M-CHO-NAM-D%C3%81NG-VU%C3%94NG-NH%E1%BB%8E-C%C3%81-S%E1%BA%A4U-VU%C3%94NG-i.96120292.6009752676?sp_atk=abb8779b-ed2a-4d6e-89b6-682f8ad4b504&xptdk=abb8779b-ed2a-4d6e-89b6-682f8ad4b504"],
        ["that_lung_nam", f"https://shopee.vn/Th%E1%BA%AFt-l%C6%B0ng-nam-Vicenzo-cao-c%E1%BA%A5p-D%C3%A2y-l%C6%B0ng-da-nam-Kh%C3%B3a-t%E1%BB%B1-%C4%91%E1%BB%99ng-d%C3%A2y-r%C4%83ng-c%C6%B0a-i.279899189.7640638439?sp_atk=5f27fb4e-c059-46ad-9144-78d07c0ab5bd&xptdk=5f27fb4e-c059-46ad-9144-78d07c0ab5bd"],
        ["ca_vat_nam", f"https://shopee.vn/C%C3%A0-v%E1%BA%A1t-nam-b%E1%BA%A3n-nh%E1%BB%8F-5cm-cavat-h%E1%BB%8Dc-sinh-sinh-vi%C3%AAn-(-l%E1%BA%BB-b%E1%BA%B1ng-s%E1%BB%89-)-i.26993521.1835043730?sp_atk=3dd6dcf6-f6e5-4862-96a8-02d99b32fe60&xptdk=3dd6dcf6-f6e5-4862-96a8-02d99b32fe60"],
        ["phu_kien_nam", f"https://shopee.vn/M%C5%A9-Beret-Nam-trung-ni%C3%AAn-ch%E1%BA%A5t-v%E1%BA%A3i-N%E1%BB%89-c%C3%B3-che-tai-M%C3%B3n-qu%C3%A0-%E1%BB%B9-ngh%C4%A9a-t%E1%BA%B7ng-%C3%94ng-B%E1%BB%91-MCT-i.22586620.874498179?sp_atk=b67d50dc-0265-44b1-b03c-aa6fe075a826&xptdk=b67d50dc-0265-44b1-b03c-aa6fe075a826"],
        ["thoi_trang_nam_khac", f"https://shopee.vn/M%C3%B3c-Kh%C3%B3a-Silicon-Ho%E1%BA%A1t-H%C3%ACnh-HALEY-Nhi%E1%BB%81u-M%E1%BA%ABu-M%C3%B3c-Kho%C3%A1-Nh%E1%BB%B1a-D%E1%BA%BBo-Xinh-X%E1%BA%AFn-D%E1%BB%85-Th%C6%B0%C6%A1ng-i.297841912.3195862573?sp_atk=b9ad3523-e468-4b24-aabe-ebd6c10ae070&xptdk=b9ad3523-e468-4b24-aabe-ebd6c10ae070"],

    ]
    i = 0
    for url in urls:
        i = i+1
        try:
            crawler = craigslist_crawler(url[1])
            commnent_list = crawler.load_page(url[0])
            print("----------Het trang {} -------------".format(i))
        except:
            continue

