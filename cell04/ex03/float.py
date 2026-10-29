# รับค่าตัวเลขจากผู้ใช้และแปลงเป็นทศนิยม (Float)
number = float(input("Give me a number: "))

# ตรวจสอบว่าตัวเลขนั้นเป็นจำนวนเต็ม (ไม่มีเศษ) หรือไม่
if number.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")