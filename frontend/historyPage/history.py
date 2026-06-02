import customtkinter as ctk

# เปลี่ยนจาก ctk.CTk เป็น ctk.CTkFrame เพื่อให้เป็นหน้าจอย่อยสลับได้ตามสถาปัตยกรรมหลัก
class LeaveHistoryPage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        # สืบทอดคุณสมบัติแบบ Frame
        super().__init__(master, fg_color="transparent", **kwargs)
        
        # 🔥 แก้ไขจุดที่ 1: เปลี่ยนชื่อเรียกฟังก์ชันให้ตรงกับด้านล่าง
        self.main_history_content()

    def main_history_content(self):
        """ส่วนเนื้อหาตารางประวัติและฟิลเตอร์ (เวอร์ชันปรับปรุงการยืดเต็มหน้าจอ)"""
        # 1. 💡 ปรับการ pack ของตัวการ์ดหลักให้เต็มที่ขึ้น
        main_card = ctk.CTkFrame(self, fg_color="#222224", corner_radius=12)
        main_card.pack(fill="both", expand=True, padx=25, pady=25)

        # --- ส่วนหัวตารางและปุ่มควบคุม (Header Toolbar) ---
        toolbar_frame = ctk.CTkFrame(main_card, fg_color="transparent")
        toolbar_frame.pack(fill="x", padx=25, pady=(20, 15))

        title_label = ctk.CTkLabel(toolbar_frame, text="📋 ประวัติการลาทั้งหมด", font=("Helvetica", 16, "bold"), text_color="#ffffff")
        title_label.pack(side="left")

        # กลุ่มปุ่มกดฝั่งขวา (Filters & Export)
        right_tools = ctk.CTkFrame(toolbar_frame, fg_color="transparent")
        right_tools.pack(side="right")

        filter_user = ctk.CTkOptionMenu(right_tools, values=["ทุกคน", "เฉพาะฉัน"], width=100, height=30, fg_color="#2a2a2b", button_color="#2a2a2b")
        filter_user.pack(side="left", padx=4)

        filter_type = ctk.CTkOptionMenu(right_tools, values=["ทุกประเภท", "ลาป่วย", "ลากิจ", "ลาพักร้อน"], width=110, height=30, fg_color="#2a2a2b", button_color="#2a2a2b")
        filter_type.pack(side="left", padx=4)

        filter_status = ctk.CTkOptionMenu(right_tools, values=["ทุกสถานะ", "อนุมัติ", "รออนุมัติ"], width=100, height=30, fg_color="#2a2a2b", button_color="#2a2a2b")
        filter_status.pack(side="left", padx=4)

        btn_excel = ctk.CTkButton(right_tools, text="📄 Export Excel", font=("Helvetica", 12, "bold"), fg_color="#14532d", hover_color="#166534", text_color="#4ade80", width=110, height=30)
        btn_excel.pack(side="left", padx=4)

        btn_report = ctk.CTkButton(right_tools, text="⏳ Export รายคน", font=("Helvetica", 12), fg_color="#2a2a2b", border_color="#4a4a4a", border_width=1, text_color="#d1d1d6", hover_color="#3a3a3c", width=110, height=30)
        btn_report.pack(side="left", padx=4)


        # --- ส่วนตารางข้อมูลที่แก้ไขระบบ Grid ใหม่ ---
        # 2. 💡 ปรับให้ตัวเลื่อน (ScrollableFrame) ยืดแนวนอนเต็มพื้นที่ด้วยคำสั่ง fill="both"
        table_container = ctk.CTkScrollableFrame(main_card, fg_color="transparent")
        table_container.pack(fill="both", expand=True, padx=25, pady=(0, 10))

        headers = [("พนักงาน", 25), ("แผนก", 12), ("ประเภท", 15), ("วันเริ่ม", 13), ("สิ้นสุด", 13), ("วัน", 7), ("สถานะ", 15), ("จัดการ", 15)]
        
        # 3. 🔥 จุดสำคัญที่สุด: บังคับให้คอลัมน์กระจายพื้นที่จนสุดขอบหน้าจอแนวนอน
        for i, (text, weight) in enumerate(headers):
            table_container.grid_columnconfigure(i, weight=weight, uniform="col_group")

        for i, (text, _) in enumerate(headers):
            lbl = ctk.CTkLabel(table_container, text=text, font=("Helvetica", 12, "bold"), text_color="#8e8e93", anchor="w" if i < 3 else "center")
            # 4. 💡 ใส่ sticky="ew" ให้หัวตารางขยายตัวเต็มคอลัมน์
            lbl.grid(row=0, column=i, sticky="ew", padx=5, pady=(0, 10))

        data_rows = [
            {"avatar": "สช", "color": "#1e3a8a", "txt_color": "#93c5fd", "name": "สมชาย รักดี", "dept": "IT", "type": "ลาป่วย", "start": "10/01/68", "end": "11/01/68", "days": "2", "status": "อนุมัติ"},
            {"avatar": "มล", "color": "#991b1b", "txt_color": "#fca5a5", "name": "มาลี สวยงาม", "dept": "HR", "type": "ลาพักร้อน", "start": "15/01/68", "end": "19/01/68", "days": "5", "status": "อนุมัติ"},
            {"avatar": "ปส", "color": "#14532d", "txt_color": "#86efac", "name": "ประสิทธิ์ ทำงาน", "dept": "Sales", "type": "ลากิจ", "start": "01/02/68", "end": "01/02/68", "days": "1", "status": "อนุมัติ"},
            {"avatar": "มล", "color": "#991b1b", "txt_color": "#fca5a5", "name": "มาลี สวยงาม", "dept": "HR", "type": "ลาป่วย", "start": "05/03/68", "end": "08/03/68", "days": "3", "status": "รออนุมัติ"},
            {"avatar": "สช", "color": "#1e3a8a", "txt_color": "#93c5fd", "name": "สมชาย รักดี", "dept": "IT", "type": "ลาพักร้อน", "start": "20/03/68", "end": "21/03/68", "days": "2", "status": "รออนุมัติ"}
        ]

        current_row = 1
        for item in data_rows:
            # 5. 💡 ปรับเซลล์ข้อมูลพนักงานให้ขยายและยึดชิดซ้าย (sticky="ew")
            emp_cell = ctk.CTkFrame(table_container, fg_color="transparent")
            emp_cell.grid(row=current_row, column=0, sticky="ew", padx=5, pady=6)
            
            av = ctk.CTkLabel(emp_cell, text=item["avatar"], font=("Helvetica", 10, "bold"), width=26, height=26, fg_color=item["color"], text_color=item["txt_color"], corner_radius=13)
            av.pack(side="left", padx=(0, 8))
            
            nm = ctk.CTkLabel(emp_cell, text=item["name"], font=("Helvetica", 13), text_color="#ffffff")
            nm.pack(side="left")

            ctk.CTkLabel(table_container, text=item["dept"], font=("Helvetica", 13), text_color="#d1d1d6", anchor="w").grid(row=current_row, column=1, sticky="ew", padx=5, pady=6)
            ctk.CTkLabel(table_container, text=item["type"], font=("Helvetica", 13), text_color="#ffffff", anchor="w").grid(row=current_row, column=2, sticky="ew", padx=5, pady=6)
            ctk.CTkLabel(table_container, text=item["start"], font=("Helvetica", 13), text_color="#ffffff", anchor="center").grid(row=current_row, column=3, sticky="ew", padx=5, pady=6)
            ctk.CTkLabel(table_container, text=item["end"], font=("Helvetica", 13), text_color="#ffffff", anchor="center").grid(row=current_row, column=4, sticky="ew", padx=5, pady=6)
            ctk.CTkLabel(table_container, text=item["days"], font=("Helvetica", 13, "bold"), text_color="#ffffff", anchor="center").grid(row=current_row, column=5, sticky="ew", padx=5, pady=6)

            if item["status"] == "อนุมัติ":
                bg_color, txt_color = "#14532d", "#4ade80"
            else:
                bg_color, txt_color = "#78350f", "#f59e0b"
                
            # 6. 💡 สั่งให้ตราสถานะและปุ่มกดแสดงอยู่ตรงกลางคอลัมน์อย่างเหมาะสม (sticky="nsew" หรือจัดการเซนเตอร์)
            badge = ctk.CTkLabel(table_container, text=item["status"], font=("Helvetica", 11, "bold"), fg_color=bg_color, text_color=txt_color, corner_radius=6, width=65, height=22)
            badge.grid(row=current_row, column=6, padx=5, pady=6)

            action_cell = ctk.CTkFrame(table_container, fg_color="transparent")
            action_cell.grid(row=current_row, column=7, padx=5, pady=6)
            
            if item["status"] == "รออนุมัติ":
                btn_approve = ctk.CTkButton(action_cell, text="อนุมัติ", font=("Helvetica", 11), fg_color="#16a34a", hover_color="#15803d", width=50, height=24, corner_radius=4)
                btn_approve.pack(side="left", padx=2)
                
            btn_delete = ctk.CTkButton(action_cell, text="🗑️", font=("Helvetica", 11), fg_color="#991b1b", hover_color="#7f1d1d", text_color="#fca5a5", width=30, height=24, corner_radius=4)
            btn_delete.pack(side="left", padx=2)

            current_row += 1

        # --- ส่วนท้ายตาราง (Footer Summary) ---
        footer_frame = ctk.CTkFrame(main_card, fg_color="transparent")
        footer_frame.pack(fill="x", padx=25, pady=(10, 20))
        
        lbl_summary = ctk.CTkLabel(footer_frame, text="แสดง 5 รายการ • รวม 13 วัน • กรองแล้ว: ทุกคน", font=("Helvetica", 12), text_color="#8e8e93")
        lbl_summary.pack(side="left")