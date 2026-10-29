# รับค่าอายุจากผู้ใช้ และใช้ int() แปลงข้อความให้เป็นตัวเลขจำนวนเต็ม
age = int(input("Please tell me your age: "))

# แสดงอายุปัจจุบันของผู้ใช้
print(f"You are currently {age} years old.")

# คำนวณและแสดงอายุในอีก 10 ปี, 20 ปี และ 30 ปีข้างหน้า
print(f"In 10 years, you'll be {age + 10} years old.")
print(f"In 20 years, you'll be {age + 20} years old.")
print(f"In 30 years, you'll be {age + 30} years old.")