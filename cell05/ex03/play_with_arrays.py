# กำหนดอาเรย์ตั้งต้น (Original array) ตามโจทย์
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# สร้าง Set ว่างขึ้นมาเพื่อเตรียมเก็บข้อมูล
new_array = set()

# วนลูปอ่านค่าทีละตัวใน original_array
for x in original_array:
    # ตรวจสอบเงื่อนไขว่าค่ามากกว่า 5 หรือไม่
    if x > 5:
        # นำค่ามาบวก 2 แล้วใส่เข้าไปใน Set ด้วยฟังก์ชัน .add()
        new_array.add(x + 2)

# แสดงผลลัพธ์
print(original_array)
print(new_array)