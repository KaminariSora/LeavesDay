import customtkinter as ctk

class MyProfilePage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.create_main_content()

    def create_main_content(self):
        # ==========================================
        # 👤 ส่วนที่ 1: ข้อมูลผู้ใช้งานโปรไฟล์ (User Header)
        # ==========================================
        user_frame = ctk.CTkFrame(self, fg_color="transparent")
        user_frame.pack(fill="x", padx=25, pady=(20, 10))

        av = ctk.CTkLabel(user_frame, text="สช", font=("Helvetica", 14, "bold"), width=46, height=46, fg_color="#1e3a8a", text_color="#93c5fd", corner_radius=23)
        av.pack(side="left", padx=(0, 15))

        u_info = ctk.CTkFrame(user_frame, fg_color="transparent")
        u_info.pack(side="left")
        ctk.CTkLabel(u_info, text="สมชาย รักดี", font=("Helvetica", 18, "bold"), text_color="#ffffff", height=22).pack(anchor="w")
        ctk.CTkLabel(u_info, text="นักพัฒนาซอฟต์แวร์ · แผนก IT · รหัส EMP-0042", font=("Helvetica", 12), text_color="#8e8e93", height=16).pack(anchor="w")


        # ==========================================
        # 📊 ส่วนที่ 2: กล่องสถิติตัวเลข 4 ช่อง (Summary Cards)
        # ==========================================
        summary_grid = ctk.CTkFrame(self, fg_color="transparent")
        summary_grid.pack(fill="x", padx=25, pady=10)
        summary_grid.grid_columnconfigure((0, 1, 2, 3), weight=1)

        cards_data = [
            ("ลาป่วยคงเหลือ", "15", "จาก 30 วัน"),
            ("ลากิจคงเหลือ", "7", "จาก 10 วัน"),
            ("พักร้อนคงเหลือ", "6", "จาก 10 วัน"),
            ("รออนุมัติ", "1", "คำขอ")
        ]

        for i, (title, count, sub) in enumerate(cards_data):
            card = ctk.CTkFrame(summary_grid, fg_color="#222224", corner_radius=12, height=105)
            p_left = 0 if i == 0 else 8
            p_right = 0 if i == 3 else 8
            card.grid(row=0, column=i, sticky="ew", padx=(p_left, p_right))
            card.pack_propagate(False)

            ctk.CTkLabel(card, text=title, font=("Helvetica", 12), text_color="#a0a0a5").pack(anchor="w", padx=20, pady=(12, 2))
            
            txt_color = "#ca8a04" if i == 3 else "#ffffff"
            ctk.CTkLabel(card, text=count, font=("Helvetica", 28, "bold"), text_color=txt_color).pack(anchor="w", padx=20)
            ctk.CTkLabel(card, text=sub, font=("Helvetica", 11), text_color="#8e8e93").pack(anchor="w", padx=20, pady=(0, 12))


        # ==========================================
        # 📈 ส่วนที่ 3: แผนภูมิสัดส่วน & แถบวันลาคงเหลือ (Middle Layout)
        # ==========================================
        middle_layout = ctk.CTkFrame(self, fg_color="transparent")
        middle_layout.pack(fill="x", padx=25, pady=10)
        middle_layout.grid_columnconfigure(0, weight=45) 
        middle_layout.grid_columnconfigure(1, weight=55) 

        # --- ฝั่งซ้าย: สัดส่วนการลาปีนี้ ---
        chart_card = ctk.CTkFrame(middle_layout, fg_color="#222224", corner_radius=12, height=180)
        chart_card.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        
        ctk.CTkLabel(chart_card, text="🎯 สัดส่วนการลาปีนี้", font=("Helvetica", 14, "bold"), text_color="#ffffff").pack(anchor="w", padx=20, pady=(15, 10))
        
        chart_body = ctk.CTkFrame(chart_card, fg_color="transparent")
        chart_body.pack(fill="both", expand=True, padx=20, pady=(0, 15))
        
        # วงกลมจำลองตรงกลาง 
        circle_mock = ctk.CTkFrame(chart_body, width=90, height=90, fg_color="transparent", border_color="#2563eb", border_width=10, corner_radius=45)
        circle_mock.pack(side="left", padx=(10, 20))
        circle_mock.pack_propagate(False)
        
        # 💡 แก้ไขจุดบักตรงนี้: ลบ anchor="center" ออก เพราะเลเอาต์ภายใน place สามารถคุมกึ่งกลางได้เองอยู่แล้วครับ
        lbl_circle_text = ctk.CTkLabel(circle_mock, text="13 วัน", font=("Helvetica", 13, "bold"), text_color="#ffffff")
        lbl_circle_text.place(relx=0.5, rely=0.5, anchor="center")
        
        # รายการคำอธิบายสีฝั่งขวา
        legend_frame = ctk.CTkFrame(chart_body, fg_color="transparent")
        legend_frame.pack(side="left", fill="y")
        
        legends = [("ลาป่วย 2 วัน", "#2563eb"), ("ลากิจ 1 วัน", "#16a34a"), ("พักร้อน 4 วัน", "#ca8a04")]
        for text, color in legends:
            item = ctk.CTkFrame(legend_frame, fg_color="transparent")
            item.pack(anchor="w", pady=3)
            dot = ctk.CTkFrame(item, width=10, height=10, fg_color=color, corner_radius=5)
            dot.pack(side="left", padx=(0, 8))
            ctk.CTkLabel(item, text=text, font=("Helvetica", 12), text_color="#ffffff").pack(side="left")

        # --- ฝั่งขวา: วันลาคงเหลือ (Progress Bars) ---
        quota_card = ctk.CTkFrame(middle_layout, fg_color="#222224", corner_radius=12, height=180)
        quota_card.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        
        ctk.CTkLabel(quota_card, text="🔄 วันลาคงเหลือ", font=("Helvetica", 14, "bold"), text_color="#ffffff").pack(anchor="w", padx=20, pady=(15, 5))

        def create_bar(title, val_str, progress, color, show_warning=False):
            row = ctk.CTkFrame(quota_card, fg_color="transparent")
            row.pack(fill="x", padx=20, pady=4)
            ctk.CTkLabel(row, text=title, font=("Helvetica", 12, "bold"), text_color="#ffffff").pack(side="left")
            
            w_text = " ⚠️" if show_warning else ""
            ctk.CTkLabel(row, text=val_str + w_text, font=("Helvetica", 12), text_color=color).pack(side="right")
            
            pbar = ctk.CTkProgressBar(quota_card, height=6, progress_color=color, fg_color="#141416")
            pbar.set(progress)
            pbar.pack(fill="x", padx=20, pady=(2, 6))

        create_bar("ลาป่วย", "15/30 (50%)", 0.5, "#2563eb")
        create_bar("ลากิจ", "3/10 (30%)", 0.3, "#16a34a")
        create_bar("ลาพักร้อน", "6/10 (60%)", 0.6, "#ca8a04", show_warning=True)


        # ==========================================
        # 🗓️ ส่วนที่ 4: ตารางประวัติการลา (Table History)
        # ==========================================
        history_card = ctk.CTkFrame(self, fg_color="#222224", corner_radius=12)
        history_card.pack(fill="both", expand=True, padx=25, pady=(10, 20))

        ctk.CTkLabel(history_card, text="🕒 ประวัติการลา (ปีนี้)", font=("Helvetica", 14, "bold"), text_color="#ffffff").pack(anchor="w", padx=20, pady=(15, 10))

        table_scroll = ctk.CTkScrollableFrame(history_card, fg_color="transparent")
        table_scroll.pack(fill="both", expand=True, padx=20, pady=(0, 15))

        headers = [("ประเภท", 20), ("วันที่", 25), ("วัน", 10), ("สถานะ", 15), ("เหตุผล", 30)]
        for i, (_, weight) in enumerate(headers):
            table_scroll.grid_columnconfigure(i, weight=weight, uniform="table_cols")

        for i, (text, _) in enumerate(headers):
            lbl = ctk.CTkLabel(table_scroll, text=text, font=("Helvetica", 12, "bold"), text_color="#8e8e93", anchor="w" if i in [0, 1, 4] else "center")
            lbl.grid(row=0, column=i, sticky="ew", padx=5, pady=(0, 8))

        ctk.CTkLabel(table_scroll, text="ลาป่วย", font=("Helvetica", 13, "bold"), text_color="#ffffff", anchor="w").grid(row=1, column=0, sticky="ew", padx=5, pady=8)
        ctk.CTkLabel(table_scroll, text="10-11 ม.ค. 68", font=("Helvetica", 13), text_color="#d1d1d6", anchor="w").grid(row=1, column=1, sticky="ew", padx=5, pady=8)
        ctk.CTkLabel(table_scroll, text="2", font=("Helvetica", 13, "bold"), text_color="#ffffff", anchor="center").grid(row=1, column=2, sticky="ew", padx=5, pady=8)
        
        status_badge = ctk.CTkLabel(table_scroll, text="อนุมัติ", font=("Helvetica", 11, "bold"), fg_color="#14532d", text_color="#4ade80", corner_radius=5, width=60, height=22)
        status_badge.grid(row=1, column=3, padx=5, pady=8) 

        ctk.CTkLabel(table_scroll, text="ไข้หวัด", font=("Helvetica", 13), text_color="#d1d1d6", anchor="w").grid(row=1, column=4, sticky="ew", padx=5, pady=8)