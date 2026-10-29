# กำหนดเมธอด array_of_names ที่รับ Dictionary เป็นพารามิเตอร์
def array_of_names(persons):
    full_names = []
    
    # วนลูปดึง Key (ชื่อจริง) และ Value (นามสกุล) จาก Dictionary
    for first_name, last_name in persons.items():
        # ใช้ capitalize() เพื่อปรับตัวอักษรตัวแรกของชื่อและนามสกุลให้เป็นพิมพ์ใหญ่
        formatted_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        full_names.append(formatted_name)
        
    return full_names

# ทดสอบเรียกใช้งานตามตัวอย่างในโจทย์
persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))