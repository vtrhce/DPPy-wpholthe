import sys

# ตรวจสอบว่ามีพารามิเตอร์ส่งเข้ามาอย่างน้อย 1 ตัวหรือไม่ (ไม่รวมชื่อไฟล์สคริปต์)
if len(sys.argv) > 1:
    print(sys.argv[1])
else:
    print("none")