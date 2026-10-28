# รับค่าข้อมูลจากผู้ใช้และแปลงเป็นตัวเลขจำนวนเต็ม (Integer)
number = int(input())

# ตรวจสอบเงื่อนไขว่าตัวเลขมีค่าน้อยกว่า 0 หรือไม่
if number < 0:
    print("This number is negative.")

# ตรวจสอบเงื่อนไขว่าตัวเลขมีค่ามากกว่า 0 หรือไม่
elif number > 0:
    print("This number is positive.")

# กรณีอื่นๆ ที่เหลือ (ซึ่งก็คือเลข 0)
else:
    print("This number is both positive and negative.")