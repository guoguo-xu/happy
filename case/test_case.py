import unittest
from api.student import Student
from tools.HTMLTestRunner import HTMLTestRunner

id = 0
class TestStudent(unittest.TestCase):

    def test_save(self):
        response = Student().save(json_data={"name": "王五", "age": 20, "address": "广东省深圳市"})
        print("test_save=" + response.text)
        print("test_save_status_code=" + str(response.status_code))
        global id
        id = response.json()["id"]
        self.assertTrue(200 == response.status_code)

    def test_get_by_id(self):
        response = Student().get_by_id(id)
        print("test_get_by_id=" + response.text)
        self.assertTrue(200 == response.status_code)

    def test_get(self):
        response = Student().get_all()
        print("test_get=" + response.text)
        self.assertTrue(200 == response.status_code)

    def test_update(self):
        response = Student().update(json_data={"id": 3, "name": "赵六", "age": 10, "address": "广东省"})
        print("test_update=" + response.text)
        print("test_update_status_code=" + str(response.status_code))
        self.assertTrue(200 == response.status_code)

    def test_get_by_id_after_update(self):
        response = Student().get_by_id(id)
        print("test_get_by_id=" + response.text)
        self.assertTrue(200 == response.status_code)

    def test_delete(self):
        response = Student().delete(id)
        print("test_delete=" + response.text)
        print("test_delete_status_code=" + str(response.status_code))
        self.assertTrue(200 == response.status_code)


if __name__ == '__main__':
    # 启动单元测试
    # unittest.main()

    # 获取TestSuite的实例对象
    suite = unittest.TestSuite()

    # 将测试用例添加到测试容器中
    suite.addTest(TestStudent('test_save'))
    suite.addTest(TestStudent('test_get_by_id'))
    suite.addTest(TestStudent('test_get'))
    suite.addTest(TestStudent('test_update'))
    suite.addTest(TestStudent('test_get_by_id_after_update'))
    suite.addTest(TestStudent('test_delete'))

    # 创建TextTestRunner类的实例对象
    file_path = open("C:/Users/许锦国/result.html", 'wb')
    runner = HTMLTestRunner(stream=file_path, title='测试报告', description='单元测试报告', tester='本人')
    runner.run(suite)
    file_path.close()
