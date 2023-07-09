from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            dic[key].append(s)
        return list(dic.values())


# 파이썬의 defaultdict은 일반적인 dict와 비슷하게 동작하지만, 한 가지 차이점이 있습니다. defaultdict는 존재하지 않는 키에 접근할 때, 해당 키를 기준으로 기본값을 생성합니다.
#
# 이 코드에서 defaultdict(list)은 값이 리스트인 딕셔너리를 생성합니다. 만약 딕셔너리에 존재하지 않는 키에 접근하면, 빈 리스트가 생성됩니다. 따라서 dic[key].append(s)는 리스트를 반환하고 해당 리스트에 s를 추가합니다.
#
# 딕셔너리의 values() 메서드는 딕셔너리의 모든 값들을 리스트로 반환합니다. 이때, 딕셔너리의 값들은 추가된 순서대로 유지됩니다. 따라서 list(dic.values())는 딕셔너리의 값들을 리스트로 반환하며, 이 값들은 dic[key].append(s)의 호출 순서에 따라 정렬됩니다. 즉, 같은 키에 대해 여러 개의 값을 가진 경우, 추가된 순서대로 값들이 정렬됩니다.