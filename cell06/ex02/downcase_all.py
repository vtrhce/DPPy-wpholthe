import sys

# กำหนดเมธอด downcase_it ที่รับพารามิเตอร์เป็นสตริง แล้วแปลงเป็นตัวพิมพ์เล็ก
def downcase_it(text):
    return text.lower()

# ดึงพารามิเตอร์ทั้งหมด (ไม่รวมชื่อไฟล์สคริปต์)
params = sys.argv[1:]

# ตรวจสอบว่ามีพารามิเตอร์ส่งเข้ามาหรือไม่
if len(params) == 0:
    print("none")
else:
    # วนลูปเรียกใช้ downcase_it กับพารามิเตอร์แต่ละตัวแล้วแสดงผลทีละบรรทัด
    for param in params:
        print(downcase_it(param))