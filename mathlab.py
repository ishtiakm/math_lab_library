def smul(array,scalar):
  #scalar multiplication with each member of the array
  return [x*scalar for x in array]
def sdiv(array,scalar):
  #scalar division with each member of the array
  return [x/scalar for x in array]
def esum(array1,array2):
  #elementwise sum of two arrrays
  return [x+y for x,y in zip(array1,array2)]
def esub(array1,array2):
  #elementwise subtraction of two arrrays
  return [x-y for x,y in zip(array1,array2)]
def emul(array1,array2):
  #elementwise multiplication of two arrrays
  return [x*y for x,y in zip(array1,array2)]
def ediv(array1,array2):
  #elementwise division of two arrrays
  return [x/y for x,y in zip(array1,array2)]

def fnum(letter):
  #returns the index of a specific letter in an array; like- a=1; d=4; z=26
  letters="abcdefghijklmnopqrstuvwxyz"
  letters=list(letters)
  return letters.index(letter.lower())+1
def fltr(index):
  #assigning a to z with a number from 1 to 26.. It takes the number as an input and returns the respective letter; like 1=a; 3=c
  letters="abcdefghijklmnopqrstuvwxyz"
  letters=list(letters)
  return letters[index-1]
def ltrsub(letter1,letter2):
  #subtract a letter from the other and find the difference in sequence; like f-b=d
  i1=fnum(letter1.lower())
  i2=fnum(letter2.lower())
  return fltr(i1-i2)
def strsub(str1,str2):
  #subtracts a string from the other; and returns the element wise subtraction; string size must be same; "sub"-"aaa"="rta"
  if len(str1) is not len(str2):
    print("string size not same")
    return
  else:
    return "".join([ltrsub(x,y) for x,y in zip(list(str1),list(str2))])
def ltrcmp(ltr1,ltr2):
  #returns 1 if letter 1 comes first in alphabetic order;if both are the same return 0; else return -1
  if not fnum(ltr1)-fnum(ltr2):
    return 0

  return 1 if (fnum(ltr1)-fnum(ltr2))<0 else -1
def strcmp(str1,str2):
  #returns 1 if string 1 comes first in alphabetical order.return -1 if string 2 comes first.return 0 if both are the same. string size must be same
  if len(str1) is not len(str2):
    print("string size not same")
    return
  else:
    for i,_ in enumerate(str1):
      if ltrcmp(str1[i],str2[i])==1:
        return 1
      elif ltrcmp(str1[i],str2[i])==-1:
        return -1
    return 0
def strremove(string,letter):
  #remove a letter from a string. if the letter is present in multiple times.. all of it is removed
  string=list(string)
  letter=list(letter)
  for x in letter:
    while x in string:
      string.remove(x)
  return ("").join(string)

def rorone(array):
  #rotates an array or a string one step towards right
  check=isinstance(array,str)
  array=list(array)
  temp=array[-1]
  for i in range((len(array)-2),-1,-1):
    array[i+1]=array[i]
  array[0]=temp
  return array if check==0 else ("").join(array)
def ror(array,n):
  #rotates an array or a string n steps towards right
  check=isinstance(array,str)
  array=list(array)
  for i in range(n):
    array=rorone(array)
  return array if check==0 else ("").join(array)

def factorial(n):
  from functools import reduce
  multiply=lambda x,y:x*y
  return reduce(multiply,[a for a in range(1,n+1)])

def ncr(n,r):
  #n choose r
  return int(factorial(n)/factorial(n-r)/factorial(r))

def npr(n,r):
  return int(factorial(n)/factorial(n-r))

def matmul(mat1,mat2):
  #matrix multiplcation
  if len(mat1[0]) is not len(mat2):
    print("Matrices Dimension does not match for multiplication")
    return None
  else:
    row=[]
    for i in range(len(mat1)):
      column=[]
      temp1=mat1[i]
      for j in range(len(mat2[0])):
        store=0
        
        temp2=[x[j] for x in mat2]
        store=sum([x*y for x,y in zip(temp1,temp2)])
        column.append(store)
      row.append(column)
    return row

def transpose(matrix):
  row=[]
  for i in range(len(matrix[0])):
    column=[]
    column=[x[i] for x in matrix]
    row.append(column)
  return row

def matadd(matrix1,matrix2):
  
  if len(matrix1)== len(matrix2) and len(matrix1[0])==len(matrix2[0]):
    row=[]

    for i in range(len(matrix1)):
      row.append(esum(matrix1[i],matrix2[i]))
    return row
  else:
    print("Matrices Dimension does not match")
    return None
def matsub(matrix1,matrix2):
  if len(matrix1)== len(matrix2) and len(matrix1[0])==len(matrix2[0]):
    row=[]

    for i in range(len(matrix1)):
      row.append(esub(matrix1[i],matrix2[i]))
    return row
  else:
    print("Matrices Dimension does not match")
    return None

def findindex(array,element):
  #finds the index of an element inside an array; it will return list of index if the element is found multiple times
  return [i for i,x in enumerate(array) if x is element]

def matshow(matrix):
  #prints the matrix in matrix form
  for row in matrix:
    print (row)
