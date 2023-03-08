class Solution:
    def findDiagonalOrder(self, mat):
        r = len(mat)
        c = len(mat[0])
        i = 0
        j = 0
        print_arr = []
        for k in range(r + c - 1):
            if k % 2 == 0:
                while i >= 0 and j < c:
                    print(i, j, 'u')
                    print_arr.append(mat[i][j])
                    i -= 1
                    j += 1
                if i + 1 < r:
                    i += 1
                j = c - 1 if j >= c else j
            else:
                while j >= 0 and i < r:
                    print(i, j, 'd')
                    print_arr.append(mat[i][j])
                    i += 1
                    j -= 1
                if j + 1 < c:
                    j += 1
                i = r - 1 if i >= i else i
        return print_arr

