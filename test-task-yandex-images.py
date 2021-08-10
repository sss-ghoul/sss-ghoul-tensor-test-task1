import pytest
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

class Test_yandex_images():

    def test_guest_can_go_to_login_page(self, browser):
        browser.get(link)

    def test_image_link(self, browser):
        imageslink = browser.find_element_by_css_selector("a[href='https://yandex.ru/images/?utm_source=main_stripe_big']")
        imageslink.click()

    def test_window_images(self, browser):
        windowimages = browser.window_handles[1]
        browser.switch_to.window(windowimages)
        assert browser.current_url == "https://yandex.ru/images/?utm_source=main_stripe_big", "The URL does not match the desired one"

    def test_the_first_category_of_images(self, browser):
        categoryfirst = browser.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/div/div/div[1]/a/img")
        categoryfirst = categoryfirst.get_attribute("alt")
        categoryfirstclick = browser.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/div/div/div[1]/a/div[1]")
        categoryfirstclick.click()
        inputtext = browser.find_element_by_class_name("input__control")
        inputtext = inputtext.get_attribute("value")
        assert categoryfirst == inputtext, "Invalid text in the search"

    def test_first_image(self, browser):
        imagefirst = browser.find_element_by_xpath("/html/body/div[4]/div[1]/div[1]/div[1]/div/div[1]/div/a")
        imagefirst.click()
        browser.find_element_by_xpath("/html/body/div[12]/div[1]/div/div/div[3]/div/div[2]/div[1]/div[3]/div/img")

    def test_the_forward_button(self, browser):
        image1 = browser.find_element_by_css_selector("body > div.Popup2.Popup2_visible.Modal.Modal_visible.Modal_theme_normal.MMViewerModal.ImagesViewer.Theme.Theme_color_yandex-default.Theme_root_legacy > div.Modal-Table > div > div > div.MediaViewer.MediaViewer_theme_fiji.ImagesViewer-Container > div > div.MediaViewer-LayoutMain.MediaViewer_theme_fiji-LayoutMain > div.MediaViewer-LayoutScene.MediaViewer_theme_fiji-LayoutScene > div.MediaViewer-View.MediaViewer_theme_fiji-View > div > img")
        image1 = image1.get_attribute("src")
        buttonforward = browser.find_element_by_xpath("/html/body/div[12]/div[1]/div/div/div[3]/div/div[2]/div[1]/div[4]/i")
        buttonforward.click()
        image2 = browser.find_element_by_css_selector("body > div.Popup2.Popup2_visible.Modal.Modal_visible.Modal_theme_normal.MMViewerModal.ImagesViewer.Theme.Theme_color_yandex-default.Theme_root_legacy > div.Modal-Table > div > div > div.MediaViewer.MediaViewer_theme_fiji.ImagesViewer-Container > div > div.MediaViewer-LayoutMain.MediaViewer_theme_fiji-LayoutMain > div.MediaViewer-LayoutScene.MediaViewer_theme_fiji-LayoutScene > div.MediaViewer-View.MediaViewer_theme_fiji-View > div > img")
        image2 = image2.get_attribute("src")
        assert image2 != image1, "The image has not changed"
        global src
        src = image1

    def test_the_back_button(self, browser):
        buttonback = browser.find_element_by_xpath("/html/body/div[12]/div[1]/div/div/div[3]/div/div[2]/div[1]/div[1]/i")
        buttonback.click()
        image1 = browser.find_element_by_css_selector("body > div.Popup2.Popup2_visible.Modal.Modal_visible.Modal_theme_normal.MMViewerModal.ImagesViewer.Theme.Theme_color_yandex-default.Theme_root_legacy > div.Modal-Table > div > div > div.MediaViewer.MediaViewer_theme_fiji.ImagesViewer-Container > div > div.MediaViewer-LayoutMain.MediaViewer_theme_fiji-LayoutMain > div.MediaViewer-LayoutScene.MediaViewer_theme_fiji-LayoutScene > div.MediaViewer-View.MediaViewer_theme_fiji-View > div > img")
        image1 = image1.get_attribute("src")
        print(src, image1)
        assert src == image1, "The image has not changed to the previous image"