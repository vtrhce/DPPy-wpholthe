# กำหนดเมธอด find_the_redheads ที่รับพารามิเตอร์เป็น Dictionary
def find_the_redheads(family_dict):
    # ใช้ filter() ร่วมกับ lambda เพื่อคัดเลือก Key (ชื่อ) ที่มี Value (สีผม) เป็น "red"
    redheads = filter(lambda name: family_dict[name] == "red", family_dict)
    
    # แปลง filter object ให้เป็น List แล้วส่งคืนค่ากลับ
    return list(redheads)

# ทดสอบเรียกใช้งานตามตัวอย่างในโจทย์
dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))