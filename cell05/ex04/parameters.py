import sys

# คำนวณจำนวนพารามิเตอร์ที่ส่งเข้ามา โดยหักชื่อไฟล์สคริปต์ (sys.argv[0]) ออก 1 ตัว
num_params = len(sys.argv) - 1

# แสดงผลจำนวนพารามิเตอร์ตามรูปแบบที่โจทย์กำหนด
print(f"Number of parameters: {num_params}.")