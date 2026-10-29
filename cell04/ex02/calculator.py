# รับค่าตัวเลขตัวแรกจากผู้ใช้และแปลงเป็นจำนวนเต็ม
num1 = int(input("Give me the first number: "))

# รับค่าตัวเลขตัวที่สองจากผู้ใช้และแปลงเป็นจำนวนเต็ม
num2 = int(input("Give me the second number: "))

# แสดงข้อความขอบคุณตามรูปแบบในโจทย์
print("Thank you!")

# แสดงผลลัพธ์การบวก ลบ หาร และคูณ
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} / {num2} = {int(num1 / num2)}")
print(f"{num1} * {num2} = {num1 * num2}")