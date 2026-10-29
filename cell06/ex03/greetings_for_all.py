# กำหนดเมธอด greetings โดยกำหนดค่าเริ่มต้น (Default Parameter) เป็น "noble stranger"
def greetings(name="noble stranger"):
    # ตรวจสอบว่าอาร์กิวเมนต์ที่ส่งเข้ามาเป็นสตริง (String) หรือไม่
    if not isinstance(name, str):
        print("Error! It was not a name.")
    else:
        print(f"Hello, {name}.")

# ทดสอบเรียกใช้งานเมธอดตามตัวอย่างในโจทย์
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)