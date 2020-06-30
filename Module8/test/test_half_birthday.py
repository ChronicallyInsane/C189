from Module8.more_fun_with_collections import timedatectl
from datetime import datetime, timedelta
import unittest as ut


class TestList(ut.TestCase):
    def test_half_birthday(self):
        self.assertNotEqual(timedatectl.half_birthday(datetime.now()), datetime.now()+timedelta(days=365/2))


if __name__ == '__main__':
    ut.main()
