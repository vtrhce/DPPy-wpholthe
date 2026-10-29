import sys

# ตรวจสอบว่ามีพารามิเตอร์ส่งมาพอดี 1 ตัวหรือไม่ (รวมชื่อไฟล์สคริปต์เป็น 2)
if len(sys.argv) == 2:
    target_param = sys.argv[1]
    
    # ให้ผู้ใช้กรอกคำทางหน้าจอ
    user_word = input("What was the parameter? ")
    
    # ตรวจสอบว่าคำที่ผู้ใช้กรอกตรงกับพารามิเตอร์หรือไม่
    if user_word == target_param:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    # ถ้าจำนวนพารามิเตอร์ไม่ใช่ 1 ตัว ให้แสดงคำว่า "none"
    print("none")