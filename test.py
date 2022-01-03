# a = [137, 80, 78, 71, 13, 10, 26, 10, 255, 255, 255, 13, 73, 72, 68, 82,
#      255, 255, 4, 255, 255, 255, 3, 66, 8, 6, 255, 255, 255, 248, 42, 0, 228]
# key = 27
# print(a)
# for x in range(len(a)):
#     b = a[x]+key
#     if a[x] == 0:
#         a[x] = 255
#     elif b >= 255:
#         a[x] = b-255
#     else:
#         a[x] = b
# print(a)
# for x in range(len(a)):
#     if a[x] == 255:
#         a[x] = 0
#     elif a[x] <= key:
#         a[x] = 255+a[x]-key
#     else:
#         a[x] -= key
# print(a)
# # print([137, 80, 78, 71, 13, 10, 26, 10, 0, 0, 0, 13, 73, 72,
# #       68, 82, 0, 0, 4, 0, 0, 0, 3, 66, 8, 6, 0, 0, 0, 248, 42])


# # with open('fzzl.png', 'rb')as f1:
# #     f1 = f1.read()
# # with open(r'source\fzzl.png', 'rb')as f2:
# #     f2 = f2.read()
# # with open('t1.ext','w')as t1:
# #     t1.write(str(list(f1)))
# # with open('t2.ext','w')as t2:
# #     t2.write(str(list(f2)))
# with open('cover.gif', 'rb')as cover:
#     with open('transcendence.zip', 'rb')as file:
#         with open('transcendence.png', 'wb')as final:
#             final.write(file.read()+cover.read())
