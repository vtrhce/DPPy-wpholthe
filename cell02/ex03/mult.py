# รับค่าตัวเลขที่หนึ่งจากผู้ใช้ และแปลงเป็นจำนวนเต็ม (Integer)
num1 = int(input("Enter the first number:\n"))

# รับค่าตัวเลขที่สองจากผู้ใช้ และแปลงเป็นจำนวนเต็ม (Integer)
num2 = int(input("Enter the second number:\n"))

# คำนวณผลคูณของตัวเลขทั้งสอง
result = num1 * num2

# แสดงผลลัพธ์ของการคูณตามรูปแบบในโจทย์
print(f"{num1} x {num2} = {result}")

# ตรวจสอบว่าผลคูณเป็นบวก, ลบ, หรือศูนย์ แล้วแสดงข้อความที่เหมาะสม
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")