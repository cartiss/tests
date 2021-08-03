from app import check_document_existance, get_doc_shelf
from api import YandexDiskAPI
import unittest

class TestAppFunctions(unittest.TestCase):
    def setUp(self):
        print('Начало проверки функции')

    def test_check_document_existance_10006(self):
        self.assertEqual(check_document_existance('10006'), True)
        print('Проверка функции check_document_existance')

    def test_get_doc_shelf_10006(self):
        self.assertEqual(get_doc_shelf('10006'), '2')
        print('Проверка функции get_doc_shelf')

    def test_create_folder_pytest(self):
        yandex = YandexDiskAPI('QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ')
        self.assertEqual(yandex.create_folder('pytest'), 201)

    def tearDown(self):
        print('Конец проверки функции', end="\n\n")


if __name__ == '__main__':
    unittest.main()