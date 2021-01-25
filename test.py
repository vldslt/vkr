from typing import List

class Matrix:
    def __init__(self, matrix_data: List[List]):
        self.__matrix = matrix_data

        m_rows = len(self.__matrix)
        self.__matrix_size = frozenset([(m_rows, len(row)) for row in self.__matrix])

        if len(self.__matrix_size) != 1:
            raise ValueError("Invalid matrix size")

    def __add__(self, other: "Matrix") -> "Matrix":
        if not isinstance(other, Matrix):
            raise TypeError(f"'{other.__class__.__name__}' "
                            f"incompatible object type")
        if self.__matrix_size != other.__matrix_size:
            raise ValueError(f"Matrix sizes difference")

        result = []

        for item in zip(self.__matrix, other.__matrix):
            result.append([sum([j, k]) for j, k in zip(*item)])

        return Matrix(result)


#        def __init__(self, list1, list2, list3):
#            self.list1 = list1 #[[31, 22], [37, 43], [51, 86]]
#            self.list2 = list2 #[[3, 5, 32], [2, 4, 6], [-1, 64, 8]]
#            self.list3 = list3 #[[3, 5, 8, 3], [8, 3, 7, 1]]
#    def __add__(self):
#        list1 = [[31, 22], [37, 43], [51, 86]]
#        list2 = [[3, 5, 32], [2, 4, 6], [-1, 64, 8]]
#        list3 = [[3, 5, 8, 3], [8, 3, 7, 1]]
#        def __str__(self) -> str:
#            return '\n'.join(['\t'.join(map(str, row)) for row in self.__matrix])


if __name__ == '__main__':
    matrix1 = Matrix([[31, 22], [37, 43], [51, 86]])
    print(matrix1, '\n')

    matrix2 = Matrix([[10, 20], [30, 40]])
    print(matrix2, '\n')

    print(matrix1 + matrix2)
