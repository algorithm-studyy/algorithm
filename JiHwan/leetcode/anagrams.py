class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = []
        answer = [][]
        for i in range(len(strs)):
            sorted_str = sorted(strs[i])
            arr.append(sorted_str)
            if arr[i] in arr:
                answer.append

        print(arr)


