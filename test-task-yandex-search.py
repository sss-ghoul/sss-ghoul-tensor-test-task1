import pytest
import time
from selenium import webdriver

link = "https://yandex.ru/"

@pytest.fixture(scope="class")
def browser():
    print("start browser for test...")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


class Test_search_in_yandex():

    def test_guest_can_go_to_login_page(self, browser):
        browser.get(link)

    def test_check_the_search_field(self, browser):
        iinput = browser.find_element_by_id("text")
        iinput.send_keys("тензор")

    def test_table_with_hints(self, browser):
        suggest = browser.find_element_by_class_name("mini-suggest__popup-content")

    def test_button_to_find(self, browser):
        button = browser.find_element_by_tag_name("button")
        button.click()

    def test_search_result(self, browser):
        time.sleep(10)
        search_result_tenzor = browser.current_url
        assert search_result_tenzor == "https://yandex.ru/search/?lr=16&text=%D1%82%D0%B5%D0%BD%D0%B7%D0%BE%D1%80", "The search results table did not appear!"

    def test_link_to_the_tensor(self, browser):
        links =[]
        linkt1 = browser.find_element_by_css_selector("a[accesskey='1']")
        links.append(linkt1)
        linkt2 = browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div/ul/li[2]/div/h2/a")
        links.append(linkt2)
        linkt3 = browser.find_element_by_css_selector("a[accesskey='3']")
        links.append(linkt3)
        linkt4 = browser.find_element_by_css_selector("a[accesskey='4']")
        links.append(linkt4)
        linkt5 = browser.find_element_by_css_selector("a[accesskey='5']")
        links.append(linkt5)
        count = 0
        for tensor_link in links:
            count += 1
            href = tensor_link.get_attribute("href")
            assert "tensor.ru" in href, \
                f"The result {count} does not contain a link to tensor.ru"