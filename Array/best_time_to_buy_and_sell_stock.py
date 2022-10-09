"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

Answer: Use two pointers to traverse the array. The first pointer is the buy pointer. The second pointer is the sell pointer. The buy pointer starts at the first element of the array. The sell pointer starts at the second element of the array. Compare the value of the element pointed by the buy pointer with the value of the element pointed by the sell pointer. If the value of the element pointed by the buy pointer is less than the value of the element pointed by the sell pointer, calculate the profit. If the profit is greater than the maximum profit, update the maximum profit. Move the sell pointer to the next element. If the value of the element pointed by the buy pointer is greater than or equal to the value of the element pointed by the sell pointer, move the buy pointer to the sell pointer. Move the sell pointer to the next element. Repeat until the sell pointer reaches the end of the array. Return the maximum profit.
"""
from typing import List

# Two pointer solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Create a variable to store the maximum profit
        max_profit = 0

        # Create a variable to store the buy pointer
        buy_pointer = 0

        # Create a variable to store the sell pointer
        sell_pointer = 1

        # While the sell pointer is less than the length of the array
        while sell_pointer < len(prices):
            # If the value of the element pointed by the buy pointer is less than the value of the element pointed by the sell pointer
            if prices[buy_pointer] < prices[sell_pointer]:
                # Calculate the profit
                profit = prices[sell_pointer] - prices[buy_pointer]

                # If the profit is greater than the maximum profit
                if profit > max_profit:
                    # Update the maximum profit
                    max_profit = profit

                # Move the sell pointer to the next element
                sell_pointer += 1

            # If the value of the element pointed by the buy pointer is greater than or equal to the value of the element pointed by the sell pointer
            else:
                # Move the buy pointer to the sell pointer
                buy_pointer = sell_pointer

                # Move the sell pointer to the next element
                sell_pointer += 1

        # Return the maximum profit
        return max_profit


# Brute Force Solution
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         lowest_price = None
#         highest_selling = 0
#         index = 0
#         for price in prices:
#             if index == 0:
#                 lowest_price = price
#                 index += 1
#             if price < lowest_price:
#                 lowest_price = price
#             price_diff = price - lowest_price
#             if price_diff > highest_selling:
#                 highest_selling = price_diff
#         return highest_selling
