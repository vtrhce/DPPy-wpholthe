# กำหนดเมธอด average ที่รับพารามิเตอร์เป็น Dictionary ของคะแนนนักเรียน
def average(scores_dict):
    if not scores_dict:
        return 0.0
    # รวมคะแนนทั้งหมดจาก Values ใน Dictionary และหารด้วยจำนวนนักเรียน
    total_score = sum(scores_dict.values())
    num_students = len(scores_dict)
    return total_score / num_students

# ทดสอบเรียกใช้งานตามตัวอย่างในโจทย์
clazz_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

clazz_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

print(f"Average for class 3B: {average(clazz_3B)}.")
print(f"Average for class 3C: {average(clazz_3C)}.")