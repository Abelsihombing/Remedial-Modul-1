## Soal 1
# def find_short(s):
#     kata = s.split()
#     jumlah_kata = []
#     for i in kata :
#         jumlah_kata.append(len(i))
    
#     jumlah_kata.sort()
#     print(jumlah_kata[0])

# find_short('Many People get up early in the morning')
# find_short('Every office would getting newest monitor')
# find_short('Create new file after this morning')

# Soal 2 
# def persistence(n):
#     a = str(n)
#     x = 0
#     while (len(a) > 1) :
#         angka = int(a[0])
#         # num = 1
#         for item in range(1, len(a)):
#             angka *= int(a[item])
#         x += 1
#         a = str(angka)
#     return print(x)

# persistence(39)
# persistence(999)
# persistence(4)

## Soal 3
# def multiplication_table(row,col):
#     for i in range(1, row+1):
#         loop = ''
#         loop += str(i)
#         for j in range(1, col):
#             loop += ' '
#             loop += str(i*(j+1))
#         print(loop)

# multiplication_table(3,3)
# print('\n')
# multiplication_table(5,3)
# print('\n')
# multiplication_table(3,5)

## Soal 4
# import string
# def alphabet_position(text):
#     group = list(string.ascii_lowercase)
#     kata = list(text.lower())
#     z = ''
#     for word in kata:
#         for i in range(len(group)):
#             if group[i] == word:
#                 z += str(i+1)
#                 z += ' '
#     return print(z)

# alphabet_position("The sunset sets at twelve o'clock")
# alphabet_position("It's never too late to try")
# alphabet_position("Have you done your homework")





