import socket

# ต้องตั้งเบอร์โทร IP Port ให้ตรงกับ Server
HOST = '127.0.0.1' 
PORT = 65432

# ขั้นตอน: create (ลูกค้าเดินไปซื้อโทรศัพท์มา 1 เครื่อง ตั้งชื่อว่า s)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        # ขั้นตอน: connect 
        s.connect((HOST, PORT))
        print(f"เชื่อมต่อกับ Server ที่ {HOST}:{PORT} สำเร็จ\n")
        
        # วนลูปคุย จนกว่าclientจะอยากวางสาย
        while True:
            # 1. ให้clientพิมพ์ข้อความผ่านคีย์บอร์ด
            message = input("ใส่ข้อความ (กด Enter ว่างๆ เพื่อออก): ")
            
            # 2. เช็คว่าclient กด Enter ว่างๆ  หรือเปล่า
            if message.strip() == "":
                print("กำลังตัดการเชื่อมต่อ...")
                break # พังลูปทิ้ง เพื่อนำไปสู่ขั้นตอน close
            
            # write ส่งออกไปหา Server
            # ต้อง .encode() แปลงตัวหนังสือเป็นสัญญาณไฟฟ้า (Bytes) ก่อนส่ง
            s.sendall(message.encode('utf-8'))
            
            # ขั้นตอน: read รอ Server ตอบกลับ
            data = s.recv(1024)
            
            # เอาสัญญาณไฟฟ้าที่ได้มา .decode() กลับเป็นตัวหนังสือ แล้วพิมพ์โชว์
            print(f"ข้อความตอบกลับ: {data.decode('utf-8')}\n")
        
        
    except ConnectionRefusedError:
        # ดักจับ Error ถ้า Server ไม่มีใครรับสาย
        print("ไม่สามารถเชื่อมต่อได้ โปรดตรวจสอบว่า Server เปิดทำงานอยู่หรือไม่")