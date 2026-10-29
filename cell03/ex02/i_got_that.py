# รับข้อความแรกเริ่มจากผู้ใช้ตามรูปแบบตัวอย่าง
user_input = input("What you gotta say? : ")

# วนลูปทำงานไปเรื่อย ๆ จนกว่าผู้ใช้จะพิมพ์ "STOP"
while user_input != "STOP":
    user_input = input("I got that! Anything else? : ")