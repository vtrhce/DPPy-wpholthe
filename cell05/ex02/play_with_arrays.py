# กำหนดอาเรย์ตั้งต้น (Original array) ตามโจทย์
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# สร้างอาเรย์ใหม่โดยเลือกเฉพาะค่าที่มากกว่า 5 แล้วนำมาบวกเพิ่มด้วย 2
new_array = [x + 2 for x in original_array if x > 5]

# แสดงผลอาเรย์ดั้งเดิมและอาเรย์ใหม่ทางหน้าจอตามรูปแบบที่กำหนด
print(original_array)
print(new_array)