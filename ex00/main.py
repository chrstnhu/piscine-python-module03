from NumPyCreator import NumpyCreator

npc = NumpyCreator()

result = npc.from_list([[1,2,3],[6,3,4]])
print(f"from list: \narray{repr(result)}\n")
# Output :
# array([[1, 2, 3],
        # [6, 3, 4]])


result = npc.from_list([[1,2,3],[6,4]])
print(f"from list: \n{repr(result)}\n")
# Output :
# None


result = npc.from_list([[1,2,3],['a','b','c'],[6,4,7]])
print(f"from list: \n{repr(result)}\n")
# Output :
# array([[’1’,’2’,’3’],
#         [’a’,’b’,’c’],
#         [’6’,’4’,’7’], dtype=’<U21’])


result = npc.from_list(((1,2),(3,4)))
print(f"from list: \n{repr(result)}\n")
# Output :
# None


result = npc.from_tuple(("a", "b", "c"))
print(f"from tuple: \narray{repr(result)}\n")
# Output :
# array([’a’, ’b’, ’c’])


result = npc.from_tuple(["a", "b", "c"])
print(f"from tuple: \n{repr(result)}\n")
# Output :
# None


result = npc.from_iterable(range(5))
print(f"from iterable: \n{repr(result)}\n")
# Output :
# array([0, 1, 2, 3, 4])


shape=(3,5)
result = npc.from_shape(shape)
print(f"from shape: \n{repr(result)}\n")
# Output :
# array([[0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0]])

result = npc.random(shape)
print(f"from random: \n{repr(result)}\n")
# Output :
# array([[0.57055863, 0.23519999, 0.56209311, 0.79231567, 0.213768 ],
        # [0.39608366, 0.18632147, 0.80054602, 0.44905766, 0.81313615],
        # [0.79585328, 0.00660962, 0.92910958, 0.9905421 , 0.05244791]])


result = npc.identity(4)
print(f"from identity: \n{repr(result)}\n")
# Output :
# array([[1., 0., 0., 0.],
#         [0., 1., 0., 0.],
#         [0., 0., 1., 0.],
#         [0., 0., 0., 1.]])