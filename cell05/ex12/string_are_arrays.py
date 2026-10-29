import sys

# ตรวจสอบว่ามีพารามิเตอร์ส่งมาพอดี 1 ตัวหรือไม่ (รวมชื่อไฟล์สคริปต์เป็น 2)
if len(sys.argv) == 2:
    text = sys.argv[1]
    
    # วนลูปตรวจสอบทีละตัวอักษรในสตริง ถ้าเจอตัวอักษร 'z' ให้พิมพ์ 'z' ออกมา
    result = "".join(['z' for char in text if char == 'z'])
    
    # ถ้าพบตัวอักษร 'z' อย่างน้อย 1 ตัว ให้แสดงผลลัพธ์ แต่ถ้าไม่พบให้แสดง "none"
    if len(result) > 0:
        print(result)
    else:
        print("none")
else:
    # ถ้าจำนวนพารามิเตอร์ไม่ใช่ 1 ตัว ให้แสดงคำว่า "none"
    print("none")