"""
    author: Zituo Yan
    description: test of github api
    date: 26/02/2020
"""
import unittest
from unittest import mock
from control.github_api import form_restful, get_repos, get_commits


class TestGithubApi(unittest.TestCase):
    """
        test case of testing github api
    """

    def test_form_restful(self):
        """
            test form restful
        :return:
        """
        self.assertEqual(form_restful("CapWailing"), "https://api.github.com/users/CapWailing")

    @mock.patch('control.github_api.requests.get')
    @mock.patch('control.github_api.get_commits')
    def test_get_repos(self, mock_commit, mock_request):
        """
            test get repos
        :param mock_commit:
        :param mock_request:
        :return:
        """
        class MockResponse:
            def __init__(self, json_data):
                self.json_data = json_data

            def json(self):
                return self.json_data
        mock_request.return_value = MockResponse([{"name": "test123"}])
        mock_commit.return_value = 3
        for i in get_repos("http//1"):
            print(i)
        self.assertEqual(list(get_repos("http://1")), [("test123", 3)])

    @mock.patch('control.github_api.requests.get')
    def test_get_commits(self, mock_request):
        """
            test get commits
        :param mock_request:
        :return:
        """
        class MockResponse:
            def __init__(self, json_data):
                self.json_data = json_data

            def json(self):
                return self.json_data
        mock_request.return_value = MockResponse([{'sha': '1'}, {'sha': '2'}, {'sha': '3'}])
        result = get_commits("http://1")
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
