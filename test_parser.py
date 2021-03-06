import unittest
from unittest.mock import patch
from apis import getdata, getfiles
from apis import getcolumns
from test_data import data as d


class Test_Parser(unittest.TestCase):

    # Testing the getFiles method
    def test_getFiles(self):

        # Creating mock api for success scenario
        with patch('apis.getfiles.getFiles') as mocked_get:
            mocked_get.return_value.status_code = 200
            mocked_get.return_value.text = d.FILES_DATA_PASS
            data = getfiles.getFiles('http://127.0.0.1:5000/getFiles')
            mocked_get.assert_called_with('http://127.0.0.1:5000/getFiles')
            self.assertEqual(data.text, d.FILES_DATA_PASS)

        # Creating mock api for failure scenario
        with patch('apis.getfiles.getFiles') as mocked_get:
            mocked_get.return_value.status_code = 400
            mocked_get.return_value.text = 'NO Files Found'
            data = getfiles.getFiles('http://127.0.0.1:5000/getFiles')
            mocked_get.assert_called_with('http://127.0.0.1:5000/getFiles')
            self.assertEqual(data.text, 'NO Files Found')

    # Testing the getColumns method
    def test_getColumns(self):

        # Creating mock api for success scenario
        with patch('apis.getcolumns.getColumns') as mocked_get:
            mocked_get.return_value.status_code = 200
            mocked_get.return_value.text = d.COLUMNS_DATA_PASS
            data = getcolumns.getColumns('http://127.0.0.1:5000/getColumns')
            mocked_get.assert_called_with('http://127.0.0.1:5000/getColumns')
            self.assertEqual(
                data.text, d.COLUMNS_DATA_PASS)

        # Creating mock api for failure scenario
        with patch('apis.getcolumns.getColumns') as mocked_get:
            mocked_get.return_value.status_code = 400
            mocked_get.return_value.text = 'NO Files Found'
            data = getcolumns.getColumns('http://127.0.0.1:5000/getColumns')
            mocked_get.assert_called_with('http://127.0.0.1:5000/getColumns')
            self.assertEqual(data.text, 'NO Files Found')

    # Testing the getData method
    def test_getData(self):
        mock_json = {'a': [1],
                     'b': [2],
                     'c': [3]}

        # Creating mock api for success scenario
        with patch('apis.getdata.getData') as mocked_get:
            mocked_get.return_value.status_code = 200
            mocked_get.return_value.json.return_value = mock_json
            data = getdata.getData()
            self.assertEqual(data.status_code, 200)
            self.assertEqual(data.json(), mock_json)

        # Creating mock api for failure scenario
        with patch('apis.getdata.getData') as mocked_get:
            mocked_get.return_value.status_code = 400
            data = getdata.getData()
            self.assertEqual(data.status_code, 400)


if __name__ == '__main__':
    unittest.main()
