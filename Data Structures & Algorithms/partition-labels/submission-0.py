class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # GOAL: Returning a list of integers of substrings ensuring that each letter appears in atmost one substring

        # Populate a hash map with the chars and the indices of their last occurrence
        last_index = {}
        for i, c in enumerate(s):
            last_index[c] = i 
        
        result = []
        size = end = 0
        
        for i, c in enumerate(s):
            size += 1
            # if last_index[c] > end:
            #     end = last_index[c]
            end = max(end, last_index[c])
            
            if i == end:
                result.append(size)
                size = 0
                
        return result
    
# test_cases = [
#     ("xyxxyzbzbbisl", [5, 5, 1, 1, 1]),
#     ("abcabc", [6])
# ]

# for i, (string, expected_partition) in enumerate(test_cases, start=1):
#     res = partition_labels(string)
#     assert res == expected_partition, f"Test case {i} failed. Got {res} instead of {expected_partition}"
    
# print("All test cases passed.")