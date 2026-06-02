import customtkinter as ctk

class ApprovePage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        # 💡 ใช้ ctk.CTkFrame เป็นหลักเพื่อให้เนื้อหาหลักยืดเต็มจอสวยงาม
        super().__init__(master, fg_color="transparent", **kwargs)
        
        self.create_main_content()

    def create_main_content(self):
        # --- 1. ส่วนกล่องสรุปด้านบน (Top Summary Cards) ---
        summary_container = ctk.CTkFrame(self, fg_color="transparent")
        summary_container.pack(fill="x", padx=25, pady=(25, 10))
        summary_container.grid_columnconfigure((0, 1, 2), weight=1)

        # การ์ดที่ 1: รออนุมัติ
        card1 = ctk.CTkFrame(summary_container, fg_color="#222224", corner_radius=12, height=120)
        card1.grid(row=0, column=0, sticky="ew", padx=(0, 10))
        card1.pack_propagate(False)
        ctk.CTkLabel(card1, text="รออนุมัติ", font=("Helvetica", 13), text_color="#a0a0a5").pack(anchor="w", padx=20, pady=(15, 2))
        ctk.CTkLabel(card1, text="5", font=("Helvetica", 32, "bold"), text_color="#ca8a04").pack(anchor="w", padx=20)
        ctk.CTkLabel(card1, text="คำขอใหม่", font=("Helvetica", 12), text_color="#8e8e93").pack(anchor="w", padx=20, pady=(0, 10))

        # การ์ดที่ 2: อนุมัติวันนี้
        card2 = ctk.CTkFrame(summary_container, fg_color="#222224", corner_radius=12, height=120)
        card2.grid(row=0, column=1, sticky="ew", padx=10)
        card2.pack_propagate(False)
        ctk.CTkLabel(card2, text="อนุมัติวันนี้", font=("Helvetica", 13), text_color="#a0a0a5").pack(anchor="w", padx=20, pady=(15, 2))
        ctk.CTkLabel(card2, text="2", font=("Helvetica", 32, "bold"), text_color="#16a34a").pack(anchor="w", padx=20)
        ctk.CTkLabel(card2, text="คำขอ", font=("Helvetica", 12), text_color="#8e8e93").pack(anchor="w", padx=20, pady=(0, 10))

        # การ์ดที่ 3: ลาในทีม (เดือนนี้)
        card3 = ctk.CTkFrame(summary_container, fg_color="#222224", corner_radius=12, height=120)
        card3.grid(row=0, column=2, sticky="ew", padx=(10, 0))
        card3.pack_propagate(False)
        ctk.CTkLabel(card3, text="ลาในทีม (เดือนนี้)", font=("Helvetica", 13), text_color="#a0a0a5").pack(anchor="w", padx=20, pady=(15, 2))
        ctk.CTkLabel(card3, text="12", font=("Helvetica", 32, "bold"), text_color="#ffffff").pack(anchor="w", padx=20)
        ctk.CTkLabel(card3, text="วัน", font=("Helvetica", 12), text_color="#8e8e93").pack(anchor="w", padx=20, pady=(0, 10))


        # --- 2. ส่วนรายการคำขอลา (Main Content Card) ---
        main_card = ctk.CTkFrame(self, fg_color="#222224", corner_radius=12)
        main_card.pack(fill="both", expand=True, padx=25, pady=15)

        title_label = ctk.CTkLabel(main_card, text="🕒 รายการรออนุมัติ", font=("Helvetica", 15, "bold"), text_color="#ffffff")
        title_label.pack(anchor="w", padx=25, pady=(20, 15))

        # 💡 ตัวสไลด์เฉพาะรายการคำขอ เพื่อให้ยืดแนวตั้งเต็มจอและเลื่อนดูเมื่อรายการเยอะๆ ได้
        list_container = ctk.CTkScrollableFrame(main_card, fg_color="transparent")
        list_container.pack(fill="both", expand=True, padx=25, pady=(0, 15))

        # ข้อมูลสมมติจำลองตามรูปภาพของคุณ
        pending_requests = [
            {
                "avatar": "สช", "av_bg": "#1e3a8a", "av_txt": "#93c5fd",
                "name": "สมชาย รักดี", "sub": "IT · ยื่นเมื่อ 18 มี.ค. 2568",
                "type": "ลาพักร้อน", "start": "20 มี.ค.", "end": "21 มี.ค.", "days": "2 วัน",
                "reason": "เหตุผล: ท่องเที่ยวต่างจังหวัดกับครอบครัว — พักร้อนคงเหลือ 6 วัน"
            },
            {
                "avatar": "ปส", "av_bg": "#14532d", "av_txt": "#86efac",
                "name": "ประสิทธิ์ ทำงาน", "sub": "Sales · ยื่นเมื่อ 19 มี.ค. 2568",
                "type": "ลาป่วย", "start": "22 มี.ค.", "end": "22 มี.ค.", "days": "1 วัน",
                "reason": "เหตุผล: ไม่สบาย มีไข้ — แนบบันทึกใบรับรองแพทย์แล้ว"
            }
        ]

        for item in pending_requests:
            # กล่องกรอบนอกของแต่ละรายการคำขอลา
            item_box = ctk.CTkFrame(list_container, fg_color="#1e1e1f", border_color="#3a3a3c", border_width=1, corner_radius=10)
            item_box.pack(fill="x", pady=8)

            # --- ส่วนหัวรายการ: ข้อมูลพนักงาน ---
            header_frame = ctk.CTkFrame(item_box, fg_color="transparent")
            header_frame.pack(fill="x", padx=20, pady=(15, 10))

            av = ctk.CTkLabel(header_frame, text=item["avatar"], font=("Helvetica", 11, "bold"), width=32, height=32, fg_color=item["av_bg"], text_color=item["av_txt"], corner_radius=16)
            av.pack(side="left", padx=(0, 12))

            info_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
            info_frame.pack(side="left")
            ctk.CTkLabel(info_frame, text=item["name"], font=("Helvetica", 14, "bold"), text_color="#ffffff", height=18).pack(anchor="w")
            ctk.CTkLabel(info_frame, text=item["sub"], font=("Helvetica", 11), text_color="#8e8e93", height=14).pack(anchor="w")

            status_lbl = ctk.CTkLabel(header_frame, text="รออนุมัติ", font=("Helvetica", 12, "bold"), text_color="#ca8a04")
            status_lbl.pack(side="right")

            # --- ส่วนเนื้อหาตรงกลาง: สรุปวันลา (ระบบ Grid 4 คอลัมน์) ---
            details_grid = ctk.CTkFrame(item_box, fg_color="transparent")
            details_grid.pack(fill="x", padx=20, pady=5)
            details_grid.grid_columnconfigure((0, 1, 2, 3), weight=1)

            details_data = [
                ("ประเภท", item["type"]),
                ("วันเริ่ม", item["start"]),
                ("วันสิ้นสุด", item["end"]),
                ("จำนวน", item["days"])
            ]
            for col, (title, val) in enumerate(details_data):
                cell = ctk.CTkFrame(details_grid, fg_color="transparent")
                if col == 0:
                    cell.grid(row=0, column=col, sticky="w")
                else:
                    cell.grid(row=0, column=col)
                ctk.CTkLabel(cell, text=title, font=("Helvetica", 11), text_color="#8e8e93", height=14).pack(anchor="w" if col == 0 else "center")
                ctk.CTkLabel(cell, text=val, font=("Helvetica", 14, "bold"), text_color="#ffffff", height=20).pack(anchor="w" if col == 0 else "center")

            # --- แถบแถวเหตุผล (Reason Row) ---
            reason_box = ctk.CTkFrame(item_box, fg_color="#262628", corner_radius=6, height=32)
            reason_box.pack(fill="x", padx=20, pady=12)
            reason_box.pack_propagate(False)
            ctk.CTkLabel(reason_box, text=item["reason"], font=("Helvetica", 12), text_color="#ffffff").pack(side="left", padx=12)

            # --- ส่วนท้าย: ปุ่มกด Action ---
            action_frame = ctk.CTkFrame(item_box, fg_color="transparent")
            action_frame.pack(fill="x", padx=20, pady=(0, 15))

            btn_app = ctk.CTkButton(action_frame, text="✓  อนุมัติ", font=("Helvetica", 12, "bold"), fg_color="#14532d", hover_color="#166534", text_color="#4ade80", width=85, height=32, corner_radius=6)
            btn_app.pack(side="left", padx=(0, 8))

            btn_rej = ctk.CTkButton(action_frame, text="✕  ปฏิเสธ", font=("Helvetica", 12, "bold"), fg_color="#7f1d1d", hover_color="#991b1b", text_color="#fca5a5", width=85, height=32, corner_radius=6)
            btn_rej.pack(side="left", padx=(0, 8))

            btn_req = ctk.CTkButton(action_frame, text="💬  ขอข้อมูลเพิ่ม", font=("Helvetica", 12), fg_color="#2a2a2b", border_color="#4a4a4a", border_width=1, text_color="#d1d1d6", hover_color="#3a3a3c", width=110, height=32, corner_radius=6)
            btn_req.pack(side="left")