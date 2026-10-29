import sys

# ---------------------------------------------------------
# ฟังก์ชันที่ 1: ระบบคำนวณค่าใช้จ่ายเฉลี่ยรายหมวดหมู่ (ใช้ Dict และคำนวณค่าเฉลี่ย)
# ---------------------------------------------------------
def calculate_budget_average(expenses_dict):
    if not expenses_dict:
        return 0.0
    total = sum(expenses_dict.values())
    count = len(expenses_dict)
    return total / count

# ---------------------------------------------------------
# ฟังก์ชันที่ 2: ระบบกรองรายชื่อสินค้าที่ราคาเกินงบ (ใช้ filter, lambda, และ list)
# ---------------------------------------------------------
def filter_affordable_items(prices_dict, max_budget):
    # กรองเฉพาะรายการที่ราคาไม่เกินงบที่ตั้งไว้
    affordable_keys = filter(lambda item: prices_dict[item] <= max_budget, prices_dict)
    return list(affordable_keys)

# ---------------------------------------------------------
# ฟังก์ชันที่ 3: ระบบจัดรูปแบบชื่องานบ้าน/สิ่งที่ต้องทำ (ใช้ capitalize และ String Concatenation)
# ---------------------------------------------------------
def format_task_list(tasks):
    formatted_tasks = []
    for task in tasks:
        # ตรวจสอบชนิดข้อมูลด้วย isinstance เพื่อความปลอดภัย
        if isinstance(task, str):
            # จัดรูปแบบตัวอักษรแรกให้เป็นพิมพ์ใหญ่ด้วย capitalize และเติมเครื่องหมาย
            clean_task = f"[ ] {task.capitalize()} - Done!"
            formatted_tasks.append(clean_task)
    return formatted_tasks

# ---------------------------------------------------------
# ส่วนหลักของโปรแกรม (Main Execution & Command Line Handler)
# ---------------------------------------------------------
def main():
    # ตัวอย่างข้อมูลจำลองในชีวิตประจำวัน
    my_daily_expenses = {
        "coffee": 65,
        "lunch": 120,
        "transport": 50,
        "snacks": 40
    }
    
    shopping_catalog = {
        "keyboard": 950,
        "mouse": 450,
        "monitor": 3500,
        "usb_cable": 150
    }
    
    chore_list = ["wash dishes", "buy groceries", "pay bills"]

    # ตรวจสอบพารามิเตอร์ที่รับเข้ามาทาง Command Line (ใช้ sys.argv)
    args = sys.argv[1:]

    if len(args) == 0:
        print("=== Python Daily Life Assistant ===")
        print("1. บันทึกค่าใช้จ่ายเฉลี่ยวันนี้:")
        avg = calculate_budget_average(my_daily_expenses)
        print(f"   -> ค่าใช้จ่ายเฉลี่ยต่อรายการ: {avg} บาท")
        
        print("\n2. สินค้าที่ราคาไม่เกิน 500 บาท (งบจำกัด):")
        cheap_items = filter_affordable_items(shopping_catalog, 500)
        print(f"   -> รายการแนะนำ: {cheap_items}")
        
        print("\n3. รายการสิ่งที่ต้องทำวันนี้:")
        formatted = format_task_list(chore_list)
        for t in formatted:
            print(f"   {t}")
            
        # ตัวอย่างการใช้ range() สร้างตารางเวลาคร่าวๆ
        print("\n4. ช่วงเวลาทำงานประจำวัน (ชั่วโมง):")
        work_hours = list(range(9, 18))
        print(f"   -> เวลาทำการ: {work_hours}")
    else:
        # หากผู้ใช้ส่งข้อความเข้ามาทาง Command Line ให้เอามาแปลงเป็นพิมพ์เล็กทั้งหมด
        print("คุณส่งข้อความเข้ามา:")
        for arg in args:
            print(f" - {arg.lower()}")

if __name__ == "__main__":
    main()