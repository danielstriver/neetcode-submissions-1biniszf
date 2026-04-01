from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        This function takes an integer array and then returns the maximum number of fruit types you can fit into 2 baskets

        THE CHALLENGE FALLS UNDER THE FOLLOWING TOPICS
        1. Array
        2. Hash Map
        3. Slidiwing window

        """

        # Initializing pointes, vars and the window


        start = 0
        max_number = float('-inf')
        fruits_count = defaultdict(int)

        # Expand window
        for end in range(len(fruits)):
            fruits_count[fruits[end]] += 1
            # Rewriting the line above if the defaultdict container hadn't been used
            # fruits_count[fruits[end]] = fruits_count.get([fruits[end]], 0) + 1

            # if the map has more than 2 fruit types
            while len(fruits_count) > 2:
                # Decrement that key count
                fruits_count[fruits[start]] -= 1

                # if this fruit count reaches zero, remove it
                if fruits_count[fruits[start]] == 0:
                    del fruits_count[fruits[start]]

                # Increment the start pointer
                start += 1

            max_number = max(max_number, (end - start + 1))

        # Return the maximum number of fruits we can get.
        return max_number

        # Returning lens(fruits) - start as the max window size
        # return (len(fruits) - start)