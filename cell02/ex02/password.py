# กำหนดรหัสผ่านที่ถูกต้องไว้ในตัวแปร password ตามโจทย์
password = "Python is awesome"

# รับค่าข้อความรหัสผ่านที่ผู้ใช้พิมพ์เข้ามาทางคีย์บอร์ด
user_input = input()

# ตรวจสอบว่ารหัสผ่านที่ผู้ใช้กรอกตรงกับตัวแปร password หรือไม่
if user_input == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")