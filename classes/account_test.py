import unittest

import account as account

from classes import account


class AccountTest(unittest.TestCase):
    def test_that_account_can_be_created(self):
        account1 = account.Account()
        self.assertIsNotNone(account1)
        self.assertIsInstance(account1, account.Account)


    def test_that_account_has_a_name(self):
        """"
        GIVEN:
        WHEN:
        THEN:
        """

        account1 = account.Account("Tolani")
        name = account1.name
        self.assertEqual("Tolani", name)

    def test_that_account_can_deposit(self):

        """"
        GIVEN: An account class
        WHEN: when a deposit is made
        THEN: account balance should be reflected
        """
        account1 = account.Account("Tolani")
        account1.deposit(2000)


        self.assertEqual(1900,  account1.balance())



    def test_that_add_works(self):
        # account1 = account
        result = account.add( 2, 5)
        self.assertEqual(7, result)

    def test_that_sub_works(self):
        result = account.sub(10, 2)
        self.assertEqual(8, result)
