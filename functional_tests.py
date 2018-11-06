from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/Users/zoro/Documents/PycharmProjects/Test-driven-Development/chromedriver')

    def teatDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 打开应用首页
        self.browser.get('http://localhost:8000')

        # 注意到网页的标题和头部包括了“todo”这个词
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')

        # 输入一个待办事项

        # 在文本框中输入“Buy peacock feathers"

        # 按回车后页面更新 待办表格显示上述内容

        # 页面中又显示一个文本框
        # 输入“Use peacock feathers to make a fly"

        # 页面更新 显示两个待办事项

        # 网站是否会记住清单
        # 生成一个唯一的url
        # 页面中有一些文字解说这个功能

        # 访问URL 待办事项列表还在

        # 满意离开


if __name__ == '__main__':
    unittest.main(warnings='ignore')
