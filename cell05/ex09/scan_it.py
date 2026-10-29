import sys
import re

# ตรวจสอบว่ามีพารามิเตอร์ส่งมาพอดี 2 ตัวหรือไม่ (รวมชื่อไฟล์สคริปต์เป็น 3)
if len(sys.argv) == 3:
    keyword = sys.argv[1]
    text = sys.argv[2]
    
    # ใช้ re.findall() ค้นหา keyword ทั้งหมดที่พบใน text
    matches = re.findall(keyword, text)
    
    # ถ้าพบคำอย่างน้อย 1 ครั้ง ให้แสดงจำนวนครั้งที่พบ
    if len(matches) > 0:
        print(len(matches))
    else:
        print("none")
else:
    # ถ้าจำนวนพารามิเตอร์ไม่ใช่ 2 ตัว ให้แสดงคำว่า none
    print("none")