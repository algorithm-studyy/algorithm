class Solution:
    def compare(self, x, y):
        if x[-1] > y[-1]:
            return 1
        elif x[-1] < y[-1]:
            return -1
        if x[-1] == y[-1] == '2':
            return 0

        for i in range(1, min(len(x), len(y))):
            for j in range(min(len(x[i]), len(y[i]))):
                if x[i][j] > y[i][j]:
                    return 1
                elif x[i][j] < y[i][j]:
                    return -1
            if len(x[i]) < len(y[i]):
                return -1
            elif len(x[i]) > len(y[i]):
                return 1
        return 1 if x[0] > y[0] else -1

    def is_digit_log(self, log: List[str]):
        for i in range(1, len(log)):
            if log[i].isalpha():
                return False
        return True

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        for i, log in enumerate(logs):
            log = log.split(' ')
            log.append('2' if self.is_digit_log(log) else '1')
            logs[i] = log
        logs.sort(key=cmp_to_key(self.compare))
        print(logs)
        return [' '.join(log[:-1]) for log in logs]


# class Solution:
#     def reorderLogFiles(self, logs: List[str]) -> List[str]:
#         def sorting_algorithm(log):
#             left_side, right_side = log.split(" ", 1)
#
#             if right_side[0].isalpha():
#                 return (0, right_side, left_side)
#             else:
#                 return (1,)
#
#         return sorted(logs, key=sorting_algorithm)


