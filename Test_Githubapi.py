import unittest
from Githubapi import *


class TestGithubApi(unittest.TestCase):
    def test_form_restful(self):
        self.assertEqual(form_restful("CapWailing"), "https://api.github.com/users/CapWailing")

    def test_get_commits(self):
        self.assertEqual(get_commits("https://api.github.com/repos/CapWailing/SSW567-Triangle/commits"), 11)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
