import sys

# เมธอดสำหรับตัดข้อความให้เหลือ 8 ตัวอักษรแรกโดยใช้ Slice
def shrink(s):
    print(s[:8])

# เมธอดสำหรับเติมตัวอักษร 'Z' ต่อท้ายให้ครบ 8 ตัวอักษรโดยใช้ Concatenation
def enlarge(s):
    needed = 8 - len(s)
    print(s + 'Z' * needed)

# ดึงพารามิเตอร์ทั้งหมด (ไม่รวมชื่อไฟล์สคริปต์)
params = sys.argv[1:]

# ตรวจสอบจำนวนพารามิเตอร์
if len(params) == 0:
    print("none")
else:
    # วนลูปตรวจสอบพารามิเตอร์แต่ละตัว
    for param in params:
        length = len(param)
        if length > 8:
            shrink(param)
        elif length < 8:
            enlarge(param)
        else:
            print(param)