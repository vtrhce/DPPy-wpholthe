import math

# รับค่าตัวเลขจากผู้ใช้และแปลงเป็นทศนิยม (Float)
number = float(input("Give me a number: "))

# ใช้ math.ceil() เพื่อปัดเศษขึ้นเป็นจำนวนเต็มถัดไป แล้วแสดงผลลัพธ์
print(int(math.ceil(number)))