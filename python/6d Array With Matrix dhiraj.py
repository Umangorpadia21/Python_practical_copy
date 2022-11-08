import numpy as np
mat1=np.array([[10,20],[30,40]])
print(mat1)
print("This is ",mat1.ndim,"D Array Matrix")
print ("//"*20)
mat2=np.array([[70,80],[50,30]],ndmin=3)
print(mat2)
print("This is ",mat2.ndim,"D Array Matrix")
