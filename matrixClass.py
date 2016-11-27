#Mehmet Tugrul Savran

# test for a number use isinstance(x,numbers.Number)
import numbers

# a 2D numeric matrix
class Matrix(object):
    def __init__(self,nrows,ncols,fill=None):
        """ build nrows-by-ncols matrix, initial contents 0 """
        self.nrows = nrows 
        self.ncols = ncols
        self.swapcount = 1
        self.initargs = str((self.nrows,self.ncols,fill))

        if type(nrows) != int or type(ncols) != int:
            raise TypeError('matrix number of rows and columns must be ints')
        if nrows <= 0 or ncols <= 0:
            raise ValueError('matrix number of rows and columns must be positive')
        
        self.matrix = [[0 for i in range(self.ncols)] for j in range(self.nrows)]
        if fill != None:
            self.fill(fill)
        

    def __getitem__(self,key):
        """ support A[r,c] """
        for element in key:
            if type(element) != int:
                raise TypeError('matrix indices should be integers')
        if not(type(key) == tuple and len(key) == 2):
            raise TypeError('key is not a 2-length tuple')
        i = key[0]
        j = key[1]
        if not((i>=0 and i<=self.nrows-1) or (j>=0 and j<=self.ncols-1)):
            raise IndexError('matrix index out of range')
        return self.matrix[i][j]

    def __setitem__(self,key,v):
        """ support A[r,c] = v """
        for element in key:
            if type(element) != int:
                raise TypeError('matrix indices should be integers')
        if not(type(key) == tuple and len(key) == 2):
            raise TypeError('key is not a 2-length tuple')
        if not(isinstance(v,numbers.Number)):
            raise TypeError('matrix value must be numeric')
        i = key[0]
        j = key[1]
        if not((i>=0 and i<=self.nrows-1) or (j>=0 and j<=self.ncols-1)):
            raise IndexError('matrix index out of range')

        self.matrix[i][j] = v

    def __iter__(self):
        """ iterate over contents: makes list(matrix) work! """
        for i in xrange(self.nrows):
            for j in xrange(self.ncols):
                yield self.matrix[i][j]

    def fill(self,value):
        """ fill matrix from a number or list of numbers """
        if value is None:
            return
        if isinstance(value,numbers.Number):
            for i in range(self.nrows):
                for j in range(self.ncols):
                    self.matrix[i][j] = value
        elif isinstance(value,list):
            if len(value) != self.nrows*self.ncols:
                raise ValueError('matrix fill value has incorrect number of elements')

            if not all(isinstance(item,numbers.Number) for item in value):
                raise TypeError('matrix fill value not a list of numbers')
            index = 0
            for i in range(self.nrows):
                for j in range(self.ncols):
                    self.matrix[i][j] = value[index]
                    index += 1 
        else:
            raise TypeError('matrix fill value not a number')


    def __repr__(self):
        """ return string representation """
        return 'Matrix'+ str((self.nrows,self.ncols,list(self)))

    @staticmethod
    def I(n):
        """ static method to construct nxn identity matrix """
        identity = Matrix(n,n)
        print identity.matrix
        index = 0 
        for i in range(identity.nrows):
            for j in range(identity.ncols):
                identity.matrix[i][index] = 1
            index += 1


        flat = []
        for i in range(identity.nrows):
            for j in range(identity.ncols):
                flat.append(identity.matrix[i][j])


        return identity
         

    def _shape(self):
        """ return dimensions of matrix as (nrows,ncols) """
        return (self.nrows,self.ncols)
    shape = property(_shape)

    def copy(self):
        """ return new matrix which is a copy of self """
        new = self
        return new

    def getCols(self):
        self.acc = []
        for c in range(len(self.matrix[0])):
            self.acc.append([self.matrix[r][c] for r in range(len(self.matrix))])
        return self.acc

    def __mul__(self,m):
        """ returns new matrix which is the matrix product of self and m """
        if type(m) != Matrix:
            raise TypeError('The second argument is not a matrix lol')
        if self.ncols != m.nrows:
            raise ValueError('matrix dot argument has incorrect number of rows')
        new = Matrix(self.nrows,m.ncols)
        columns = m.getCols()
        rowindex = 0
        colindex = 0 
        for row in self.matrix:
            colindex = 0 
            for col in columns:
                summ = 0
                for i,j in zip(row,col):
                    summ+= i*j 
                new.matrix[rowindex][colindex] = summ
                print new.matrix
                colindex += 1 
            rowindex+=1
        return new

    def transpose(self):
        """ return new matrix which is the transpose of self """
        trans = Matrix(self.ncols,self.nrows)
        for i in range(self.nrows):
            for j in range(self.ncols):
                trans.matrix[j][i] = self.matrix[i][j]
        return trans

    def gaussianelimination(self):
        
        for k in range(self.nrows):
            maxi = self.matrix[k][0]
            i_max = k 
            for i in range(k,self.nrows):
                if abs(self.matrix[i][k])>maxi:
                    maxi = abs(self.matrix[i][k])
                    i_max = i 
            self.swapcount += 1 
            self.matrix[i_max], self.matrix[k] = self.matrix[k], self.matrix[i_max]
            
            pivotval = self[k,k]
            if pivotval == 0:
                raise ValueError ('Singular Matrix')

            for j in range(k,self.ncols):
                self[k,j] = self[k,j]/float(pivotval)
            for row in range(self.nrows):
                if k != row:
                    f = float(self[row,k])
                    for j in range(k,self.ncols):
                        self[row,j] -= f*self[k,j]

    def solve(self,b):
        """ return new matrix x such that self*x = b """
        nrows = self.nrows
        ncols = self.ncols
        newmatrix = Matrix(nrows,ncols+b.ncols) #Account for b not being just a column vector
        for i in range(nrows):
            for j in range(ncols):
                newmatrix[i,j]= self[i,j]
            for j in range(b.ncols):
                newmatrix[i,ncols+j] = b[i,j]
        newmatrix.gaussianelimination()
        x = Matrix(nrows,b.ncols)
        for i in range(x.nrows):
            for j in range(b.ncols):
                x[i,j] = newmatrix[i,j+ncols]
        return x

    def inverse(self):
        """ return new matrix which is the inverse of self """
        return self.solve(Matrix.I(self.nrows))
        
    def det(self):
        """ compute determinant """
        nrows = self.nrows
        ncols = self.ncols
        factor = self.shape[0] * self.shape[1]
        newmatrix = Matrix(nrows,ncols) #Account for b not being just a column vector
        for i in range(nrows):
            for j in range(ncols):
                newmatrix[i,j]= self[i,j]
        newmatrix.gaussianelimination()
        swaps = newmatrix.swapcount
        diags = []
        index = 0
        for row in range(newmatrix.nrows):
            diags.append(newmatrix.matrix[row][index])
            index += 1 
        product = 0 
        for i in range(1,len(diags)):
            product = diags[i-1]*diags[i]
        product = 2*factor * product
        determinant = product * (-1)**swaps
        return determinant