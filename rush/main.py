import sys

# ฟังก์ชันคำนวณมูลค่ารวมและราคาเฉลี่ยของสินค้าในคลัง (มี return ค่า)
def calculate_inventory_stats(inventory):
    if not inventory:
        return 0.0, 0.0
    total_value = sum(item['price'] * item['quantity'] for item in inventory.values())
    avg_price = sum(item['price'] for item in inventory.values()) / len(inventory)
    return total_value, avg_price

# ฟังก์ชันค้นหาสินค้าตามคำค้นหา (รับ parameter และ return ค่า)
def search_items(inventory, keyword):
    results = []
    for name, data in inventory.items():
        if keyword.lower() in name.lower():
            results.append((name, data))
    return results

# ฟังก์ชันแสดงเมนูหลัก
def show_menu():
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. เพิ่มสินค้า (Add Record)")
    print("2. ดูสินค้าทั้งหมด (View Records)")
    print("3. อัปเดตหรือลบสินค้า (Update/Remove Record)")
    print("4. ค้นหาและสรุปข้อมูล (Search and Summary)")
    print("5. ออกจากโปรแกรม (Exit)")

# ฟังก์ชันหลักในการรันโปรแกรม
def main():
    # ใช้ List และ Dictionary ตามข้อกำหนด[cite: 19]
    inventory = {}
    
    while True: # ใช้ while loop ควบคุมการทำงานหลัก[cite: 20]
        show_menu()
        choice = input("เลือกเมนู (1-5): ").strip()
        
        # เงื่อนไขการตัดสินใจ (if-elif-else) และ Validation Rules[cite: 20]
        if choice == '1':
            name = input("ระบุชื่อสินค้า: ").strip().lower()
            if not name:
                print("ข้อผิดพลาด: ชื่อสินค้าต้องไม่เป็นค่าว่าง!")
                continue
            if name in inventory:
                print("ข้อผิดพลาด: มีสินค้านี้อยู่ในระบบแล้ว (ห้ามข้อมูลซ้ำ)!")
                continue
            
            try:
                price = float(input("ระบุราคาสินค้าต่อหน่วย: "))
                quantity = int(input("ระบุจำนวนสินค้า: "))
                if price < 0 or quantity < 0:
                    print("ข้อผิดพลาด: ราคาและจำนวนต้องไม่ติดลบ!")
                    continue
            except ValueError:
                print("ข้อผิดพลาด: กรุณากรอกตัวเลขที่ถูกต้อง!")
                continue
            
            inventory[name] = {"price": price, "quantity": quantity}
            print(f"เพิ่มสินค้า '{name}' สำเร็จ!")
            
        elif choice == '2':
            if not inventory:
                print("ยังไม่มีข้อมูลสินค้าในระบบ (none)")
            else:
                print("\n--- รายการสินค้าทั้งหมด ---")
                for name, data in inventory.items(): # ใช้ for loop วนแสดงข้อมูล[cite: 20]
                    print(f"- {name.capitalize()}: ราคา {data['price']} บาท | จำนวน {data['quantity']} ชิ้น")
                    
        elif choice == '3':
            name = input("ระบุชื่อสินค้าที่ต้องการจัดการ: ").strip().lower()
            if name not in inventory:
                print("ข้อผิดพลาด: ไม่พบสินค้าดังกล่าวในระบบ!")
                continue
            action = input("ต้องการ (u) ปรับปรุงจำนวน หรือ (d) ลบสินค้า? พิมพ์ u/d: ").strip().lower()
            if action == 'u':
                try:
                    new_qty = int(input("ระบุจำนวนใหม่: "))
                    if new_qty < 0:
                        print("ข้อผิดพลาด: จำนวนต้องไม่ติดลบ!")
                        continue
                    inventory[name]['quantity'] = new_qty
                    print("อัปเดตจำนวนสินค้าสำเร็จ!")
                except ValueError:
                    print("ข้อผิดพลาด: กรุณากรอกตัวเลขที่ถูกต้อง!")
            elif action == 'd':
                del inventory[name]
                print("ลบสินค้าออกจากระบบสำเร็จ!")
            else:
                print("คำสั่งไม่ถูกต้อง กลับสู่เมนูหลัก")
                
        elif choice == '4':
            keyword = input("กรอกคำค้นหาชื่อสินค้า: ").strip()
            found = search_items(inventory, keyword)
            print(f"พบสินค้าที่ตรงกัน: {len(found)} รายการ")
            for name, data in found:
                print(f" > {name}: {data['quantity']} ชิ้น (ราคา {data['price']} บาท)")
            
            total_val, avg_pr = calculate_inventory_stats(inventory)
            print(f"\n[สรุปข้อมูล] มูลค่าสินค้าคงคลังรวม: {total_val:.2f} บาท | ราคาเฉลี่ยต่อหน่วย: {avg_pr:.2f} บาท")
            
        elif choice == '5':
            print("ออกจากโปรแกรม ขอบคุณที่ใช้งานครับ!")
            break
        else:
            print("ข้อผิดพลาด: ตัวเลือกไม่ถูกต้อง กรุณาเลือก 1-5 เท่านั้น")

if __name__ == "__main__":
    main()