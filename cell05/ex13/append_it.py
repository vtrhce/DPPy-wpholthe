import sys

# ดึงพารามิเตอร์ทั้งหมด (ไม่รวมชื่อไฟล์สคริปต์)
params = sys.argv[1:]

# ตรวจสอบว่าไม่มีพารามิเตอร์ส่งเข้ามาเลยหรือไม่
if len(params) == 0:
    print("none")
else:
    # วนลูปตรวจสอบพารามิเตอร์แต่ละตัว
    for param in params:
        # หากพารามิเตอร์ไม่ได้ลงท้ายด้วย "ism" ให้ต่อท้ายด้วย "ism" แล้วแสดงผล
        if not param.endswith("ism"):
            print(param + "ism")