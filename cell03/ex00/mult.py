#
# รับค่าตัวเลขที่ 1 และ 2 จากผู้ใช้
num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))

# คำนวณผลคูณ
result = num1 * num2

# แสดงสมการและผลลัพธ์
print(f"{num1} x {num2} = {result}")

# ตรวจสอบว่าผลลัพธ์เป็นบวก, ลบ, หรือศูนย์ ตามตัวอย่างโจทย์
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
