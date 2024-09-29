import unittest


def product_except_self(nums):
    res = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res


class TestProduct(unittest.TestCase):
    def test_product1(self):
        nums = [1, 2, 3, 4]
        self.assertEqual([24, 12, 8, 6], product_except_self(nums))

    def test_product2(self):
        nums = [-1, 1, 0, -3, 3]
        self.assertEqual([0, 0, 9, 0, 0], product_except_self(nums))
