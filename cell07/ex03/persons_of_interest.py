# กำหนดเมธอด famous_births ที่รับ Dictionary เป็นพารามิเตอร์
def famous_births(scientists):
    # ใช้ sorted() จัดเรียง Key ใน Dictionary โดยอ้างอิงค่าจาก "date_of_birth" ของแต่ละคน
    sorted_scientists = sorted(scientists.values(), key=lambda x: x["date_of_birth"])
    
    # วนลูปแสดงผลชื่อและปีเกิดตามรูปแบบในโจทย์
    for person in sorted_scientists:
        print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")

# ทดสอบเรียกใช้งานตามตัวอย่างในโจทย์
women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecilia Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)