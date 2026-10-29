import sys

# ดึงพารามิเตอร์ทั้งหมด (ไม่รวมชื่อไฟล์สคริปต์)
params = sys.argv[1:]

# ตรวจสอบว่าไม่มีพารามิเตอร์ส่งเข้ามาเลยหรือไม่
if len(params) == 0:
    print("none")
else:
    # แสดงจำนวนพารามิเตอร์ทั้งหมด
    print(f"parameters: {len(params)}")
    
    # ใช้ลูป for วนลูปทีละพารามิเตอร์เพื่อแสดงคำและนับความยาวด้วย len()
    for param in params:
        print(f"{param}: {len(param)}")