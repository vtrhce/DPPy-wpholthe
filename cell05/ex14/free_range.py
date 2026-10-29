import sys

# ตรวจสอบว่ามีพารามิเตอร์ส่งมาพอดี 2 ตัวหรือไม่ (รวมชื่อไฟล์สคริปต์เป็น 3)
if len(sys.argv) == 3:
    # แปลงค่าพารามิเตอร์จากสตริงเป็นจำนวนเต็ม (Integer)
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    
    # ใช้ range() สร้างช่วงตัวเลขจาก start ถึง end (บวก 1 เพื่อให้รวมค่าสุดท้ายด้วย) แล้วแปลงเป็น List
    result_array = list(range(start, end + 1))
    
    # แสดงผลอาเรย์ทางหน้าจอ
    print(result_array)
else:
    # ถ้าจำนวนพารามิเตอร์ไม่ใช่ 2 ตัว ให้แสดงคำว่า "none"
    print("none")