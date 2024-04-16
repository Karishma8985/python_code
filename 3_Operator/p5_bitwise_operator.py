# bitwise operator works on binary bits(0/1)
# binary formation:
# 1. and(&): when both bits r one then ans is 1
# 12 & 24
 #        16 8 4 2 1
# 12       0 1 1 0 0
# 24     & 1 1 0 0 0
#          __________
#          0 1 0 0 0  ==> 8

# 2. or(|): at least one bit should be 1
# 12 | 24
 #        16 8 4 2 1
# 12       0 1 1 0 0
# 24     | 1 1 0 0 0
#          __________
#          1 1 1 0 0  ==> 28

# 3. xor(^): when opposite bits are meet then ans is 1
# 12 ^ 24
 #        16 8 4 2 1
# 12       0 1 1 0 0
# 24     ^ 1 1 0 0 0
#          __________
#          1 0 1 0 0  ==> 20

# 4. complement (~) (tilt) (unary op) -(var+1)
# ~ 12 ==  -(12+1)  ==-13

# 5. shift operator (<</>>)
# 5.1: left shift (<<)  ex 12 << 1 == 12 * 2^1
#                          12 << 2 == 12 * 2^2
# bits moves toward left
#         16 8 4 2 1
# # 12       0 1 1 0 0
# #        0 1 1 0 0 0  == 24

# 12<<2 64 32 16 8 4 2 1
# 12           0 1 1 0 0
#        0  1  1 0 0 0 0 == 48

# 5.2: rightshift( >>)  ex  12 >> 1 == 12 / 2 ^ 1
#                           12 >> 2 == 12 / 2 ^ 2
# bits moves toward left
#         16 8 4 2 1
# 12       0 1 1 0 0
#            0 1 1 0   == 6

a = int(input("enter no"))
b = int(input("enter no"))
c= a&b
print(f" a & b: {c}")
c= a|b
print(f" a | b: {c}")
c= a^b
print(f" a ^ b: {c}")

c= ~a
print(f" ~a : {c}")
c= a<<1
print(f" a << 1: {c}")
c= a>>1
print(f" a >> 1: {c}")

