import socket

HOST = '127.0.0.1' #โทรตนเอง
PORT = 65432  #ยังไม่เช็คพอร์ตนี้

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #.AF_INET คือการใช้ IPv4, SOCK_STREAM คือการใช้ TCP
    s.bind((HOST, PORT)) #เชื่อมHOST และ PORT กับ socket
    s.listen(1) #รับคนได้ 1 คน
    print(f"Server เริ่มทำงานแล้ว กำลังรอรับการเชื่อมต่อที่ {HOST}:{PORT}...")

    while True:
        conn, addr = s.accept()# รอการaccept คุยกับ client ผ่านcon และaddr จะเก็บข้อมูลของ client ที่เชื่อมต่อเข้ามา(IP และ port)
        with conn:# จะจัดการเรื่อง close socket ให้อัตโนมัติเมื่อหลุดจากบล็อกนี้
            client_ip = addr[0] #เก็บค่า IP clint
            print(f"\n[+] มีการเชื่อมต่อมาจาก client IP address: {client_ip}:{addr[1]}")
            # วนลูปเพื่อคุยกับลูกค้าคนนี้ไปเรื่อยๆ จนกว่าเขาจะวางสาย
            while True:
                data = conn.recv(1024) #รับข้อมูลจาก client ขนาดไม่เกิน 1024 ตัวอักษร
                if not data:  #ถ้าไม่มีข้อมูลส่งมา แสดงว่า client วางสาย (disconnect)
                    print(f"[-] Client {client_ip} ทำการ disconnect (Close)")
                    print("Server พร้อมจะรับการเชื่อมต่อจาก client ต่อไป...")
                    break # ออกจากลูปการคุย
                
                
                message = data.decode('utf-8') #แปลงสัญญาณเป็นข้อความที่อ่านออก
                print(f"Client ส่งมาว่า: {message}")
                
                
                reply_message = f"Server ได้รับข้อความ '{message}' แล้ว!"# เตรียมคำพูดที่จะตอบกลับ
                
                
                conn.sendall(reply_message.encode('utf-8'))#write (ตอบกลับลูกค้า)
           