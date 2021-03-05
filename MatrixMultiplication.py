


def dotProduct(m1, m2):
    if len(m1) != len(m2):
        print("The matrices are not of the same length")
        raise IndexError
    else:
        count = 0
        for i in range(len(m1)):
            count += (m1[i] * m2[i])
        return count

class Matrix:
    def __init__(self, tdarray):
        self.rows = tdarray
        self.columns = [[] for i in range(len(tdarray[0]))]
        for i in range(len(tdarray)):
            for j in range(len(tdarray[0])):
                self.columns[j].append(tdarray[i][j])
    def num_rows(self):
        return len(self.rows)
    def num_colums(self):
        return len(self.columns)
    def get_row(self,n):
        return self.rows[n-1]
    def get_column(self,n):
        return self.columns[n-1]
    def get_el(self,r,c):
        return self.rows[r-1][c-1]
    def __str__(self):
        string = ""
        for i in self.rows:
            string = string + str(i) + "\n"
        return string
    def __mul__(self, other):
        if type(other) is Matrix:
            if len(self.columns) != other.num_rows():
                print("Matrix sizes are incompatible")
                raise IndexError
            else:
                ls = [[] for i in range(len(self.rows))]
                for i in range(len(self.rows)):
                    for j in other.columns:
                        ls[i].append(dotProduct(self.rows[i],j))
                return Matrix(ls)
        elif type(other) is int:
            ls = [[] for i in range(len(self.rows))]
            for i in range(len(self.rows)):
                for j in range(len(self.columns)):
                    ls[i].append(self.rows[i][j]*other)
            return Matrix(ls)
        else:
            raise TypeError
    def __add__(self,other):
        if type(other) is Matrix:
            if len(self.columns) == other.num_columns() and len(self.rows) == other.num_rows():
                ls = [[] for i in range(len(self.rows))]
                for i in range(len(self.rows)):
                    for j in range(len(self.columns)):
                        ls[i].append(self.rows[i][j] + other.rows[i][j])
                return Matrix(ls)
            else:
                print("Matrix sizes are incompatible")
                raise IndexError
        else:
            raise TypeError



