# รับค่าตัวเลขจากผู้ใช้และแปลงเป็นจำนวนเต็ม (Integer)
number = int(input("Enter a number less than 25\n"))

# ตรวจสอบว่าตัวเลขมีค่ามากกว่า 25 หรือไม่
if number > 25:
    print("Error")
else:
    # ใช้ลูปแสดงตัวเลขตั้งแต่ค่าที่ผู้ใช้กรอกจนถึง 25
    while number <= 25:
        print(f"Inside the loop, my variable is {number}")
        number += 1