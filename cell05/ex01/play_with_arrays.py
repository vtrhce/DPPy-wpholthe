# กำหนดอาเรย์ตั้งต้น (Original array) ตามโจทย์
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# สร้างอาเรย์ใหม่ (New array) โดยนำแต่ละค่าในอาเรย์เดิมมาบวกเพิ่มด้วย 2
new_array = [x + 2 for x in original_array]

# แสดงผลอาเรย์ดั้งเดิมและอาเรย์ใหม่ทางหน้าจอตามรูปแบบที่กำหนด
print(f"Original array: {original_array}")
print(f"New array: {new_array}")