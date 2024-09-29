import unittest


def max_product_subarray(nums):
    max_prod = nums[0]
    min_prod = nums[0]
    result = nums[0]
    for i in range(1, len(nums)):
        temp = max(nums[i], max_prod * nums[i], min_prod * nums[i])
        min_prod = min(nums[i], max_prod * nums[i], min_prod * nums[i])
        max_prod = temp
        result = max(result, max_prod)
    return result


class TestMaxProductSubarray(unittest.TestCase):
    def testMPS1(self):
        nums = [2, 3, -2, 4]
        self.assertEqual(6, max_product_subarray(nums))

    def testMPS2(self):
        nums = [-2, 0, -1]
        self.assertEqual(0, max_product_subarray(nums))

    def testMPS3(self):
        nums = [6, -3, -10, 0, 2]
        self.assertEqual(180, max_product_subarray(nums))
