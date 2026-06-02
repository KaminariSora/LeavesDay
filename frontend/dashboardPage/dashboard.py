import customtkinter as ctk

class DashboardPage(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=25, pady=25)

        # กำหนดสัดส่วนคอลัมน์ ฝั่งซ้ายน้ำหนัก 55% ฝั่งขวาน้ำหนัก 45%
        container.grid_columnconfigure(0, weight=55)
        container.grid_columnconfigure(1, weight=45)
        container.grid_rowconfigure(0, weight=1)

        # ==========================================
        # 📄 ฝั่งซ้าย: แบบฟอร์มขอลา (Leave Form)
        # ==========================================
        form_card = ctk.CTkFrame(container, fg_color="#222224", corner_radius=12)
        form_card.grid(row=0, column=0, sticky="nsew", padx=(0, 12))

        title_form = ctk.CTkLabel(form_card, text="📄 แบบฟอร์มขอลา", font=("Helvetica", 15, "bold"), text_color="#ffffff")
        title_form.pack(anchor="w", padx=25, pady=(20, 15))

        # แถวที่ 1: พนักงาน & ประเภทการลา (Row 1)
        row1 = ctk.CTkFrame(form_card, fg_color="transparent")
        row1.pack(fill="x", padx=25, pady=5)
        row1.grid_columnconfigure((0, 1), weight=1)

        lbl_emp = ctk.CTkLabel(row1, text="พนักงาน", text_color="#a0a0a5", font=("Helvetica", 12))
        lbl_emp.grid(row=0, column=0, sticky="w", pady=(0, 2))
        combo_emp = ctk.CTkOptionMenu(row1, values=["สมชาย รักดี (IT)"], fg_color="#2a2a2b", button_color="#2a2a2b", text_color="#ffffff", height=35)
        combo_emp.grid(row=1, column=0, sticky="ew", padx=(0, 10))

        lbl_type = ctk.CTkLabel(row1, text="ประเภทการลา", text_color="#a0a0a5", font=("Helvetica", 12))
        lbl_type.grid(row=0, column=1, sticky="w", pady=(0, 2))
        combo_type = ctk.CTkOptionMenu(row1, values=["ลาพักร้อน", "ลาป่วย", "ลากิจ"], fg_color="#2a2a2b", button_color="#2a2a2b", text_color="#93c5fd", height=35)
        combo_type.grid(row=1, column=1, sticky="ew")

        # แถวที่ 2: วันที่เริ่มลา & วันที่สิ้นสุด (Row 2)
        row2 = ctk.CTkFrame(form_card, fg_color="transparent")
        row2.pack(fill="x", padx=25, pady=10)
        row2.grid_columnconfigure((0, 1), weight=1)

        lbl_start = ctk.CTkLabel(row2, text="วันที่เริ่มลา", text_color="#a0a0a5", font=("Helvetica", 12))
        lbl_start.grid(row=0, column=0, sticky="w", pady=(0, 2))
        ent_start = ctk.CTkEntry(row2, fg_color="#2a2a2b", border_color="#4a4a4a", text_color="#ffffff", height=35)
        ent_start.insert(0, "📅   20 มี.ค. 2568")
        ent_start.grid(row=1, column=0, sticky="ew", padx=(0, 10))

        lbl_end = ctk.CTkLabel(row2, text="วันที่สิ้นสุด", text_color="#a0a0a5", font=("Helvetica", 12))
        lbl_end.grid(row=0, column=1, sticky="w", pady=(0, 2))
        ent_end = ctk.CTkEntry(row2, fg_color="#2a2a2b", border_color="#4a4a4a", text_color="#ffffff", height=35)
        ent_end.insert(0, "📅   21 มี.ค. 2568")
        ent_end.grid(row=1, column=1, sticky="ew")

        # แถวที่ 3: เหตุผลการลา
        lbl_reason = ctk.CTkLabel(form_card, text="เหตุผล", text_color="#a0a0a5", font=("Helvetica", 12))
        lbl_reason.pack(anchor="w", padx=25, pady=(5, 2))
        
        # 💡 ปรับให้กล่องข้อความยืดหยุ่นขยายแนวตั้งเพิ่มพื้นที่ว่าง (เปิด fill="both" และ expand=True)
        txt_reason = ctk.CTkTextbox(form_card, height=70, fg_color="#2a2a2b", border_color="#4a4a4a", border_width=1, text_color="#ffffff")
        txt_reason.insert("1.0", "ท่องเที่ยวต่างจังหวัดกับครอบครัว")
        txt_reason.pack(fill="both", expand=True, padx=25, pady=(0, 10))

        # แถวที่ 4: แนบไฟล์ (Drag & Drop Zone จำลอง)
        lbl_file = ctk.CTkLabel(form_card, text="แนบไฟล์ (ไม่บังคับ)", text_color="#a0a0a5", font=("Helvetica", 12))
        lbl_file.pack(anchor="w", padx=25, pady=(5, 2))
        
        # 💡 ให้โซนแนบไฟล์แปรผันขยายตามความสูงหน้าจออย่างเหมาะสม
        file_zone = ctk.CTkFrame(form_card, height=75, fg_color="#1e1e1f", border_color="#4a4a4a", border_width=1)
        file_zone.pack(fill="both", expand=True, padx=25, pady=(0, 15))
        file_zone.pack_propagate(False)
        
        lbl_zone_text = ctk.CTkLabel(file_zone, text="📤\nคลิกหรือลากไฟล์มาวาง", font=("Helvetica", 12), text_color="#a0a0a5")
        lbl_zone_text.place(relx=0.5, rely=0.5, anchor="center")

        # แถวที่ 5: ปุ่มกดยืนยัน / ล้างข้อมูล
        btn_frame = ctk.CTkFrame(form_card, fg_color="transparent")
        btn_frame.pack(fill="x", padx=25, pady=(10, 20))
        
        btn_submit = ctk.CTkButton(btn_frame, text="🚀 ส่งคำขอ", font=("Helvetica", 13, "bold"), fg_color="#2563eb", hover_color="#1d4ed8", width=110, height=36)
        btn_submit.pack(side="left", padx=(0, 10))
        
        btn_clear = ctk.CTkButton(btn_frame, text="ล้างข้อมูล", font=("Helvetica", 13), fg_color="#2a2a2b", border_color="#4a4a4a", border_width=1, text_color="#ffffff", hover_color="#3a3a3c", width=90, height=36)
        btn_clear.pack(side="left")

        # ==========================================
        # 📊 ฝั่งขวา: สถิติวันลาคงเหลือ & เกณฑ์การลา
        # ==========================================
        right_panel = ctk.CTkFrame(container, fg_color="transparent")
        right_panel.grid(row=0, column=1, sticky="nsew", padx=(12, 0))
        
        # 🔥 จุดแก้ไขที่ 2: จัดสัดส่วนระบบ Grid ให้กับพาเนลฝั่งขวา ให้ยอมกระจายพื้นที่ให้ลูกบน-ล่าง เท่าๆ กัน
        right_panel.grid_rowconfigure(0, weight=1)
        right_panel.grid_rowconfigure(1, weight=1)
        right_panel.grid_columnconfigure(0, weight=1)
        
        # การ์ดบน: วันลาคงเหลือของคุณ
        quota_card = ctk.CTkFrame(right_panel, fg_color="#222224", corner_radius=12)
        # เปลี่ยนไปใช้ระบบ grid เพื่อให้สัมพันธ์กับการคำนวณน้ำหนักแนวตั้ง
        quota_card.grid(row=0, column=0, sticky="nsew", pady=(0, 12))

        title_quota = ctk.CTkLabel(quota_card, text="📅 วันลาคงเหลือของคุณ", font=("Helvetica", 14, "bold"), text_color="#ffffff")
        title_quota.pack(anchor="w", padx=20, pady=(15, 10))

        def create_leave_progress(parent, title, remaining, details, progress_val, bar_color):
            frame = ctk.CTkFrame(parent, fg_color="transparent")
            frame.pack(fill="x", padx=20, pady=6)
            
            lbl_title = ctk.CTkLabel(frame, text=title, font=("Helvetica", 12, "bold"), text_color="#ffffff")
            lbl_title.pack(side="left")
            
            lbl_rem = ctk.CTkLabel(frame, text=remaining, font=("Helvetica", 12, "bold"), text_color=bar_color)
            lbl_rem.pack(side="right")
            
            pbar = ctk.CTkProgressBar(parent, height=8, progress_color=bar_color, fg_color="#141416")
            pbar.set(progress_val)
            pbar.pack(fill="x", padx=20, pady=(2, 2))
            
            lbl_det = ctk.CTkLabel(parent, text=details, font=("Helvetica", 11), text_color="#8e8e93")
            lbl_det.pack(anchor="w", padx=20, pady=(0, 8))

        create_leave_progress(quota_card, "ลาป่วย", "เหลือ 15 วัน", "ใช้ไป 15 / 30 วัน", 0.5, "#2563eb")
        create_leave_progress(quota_card, "ลากิจ", "เหลือ 7 วัน", "ใช้ไป 3 / 10 วัน", 0.3, "#16a34a")
        create_leave_progress(quota_card, "ลาพักร้อน", "เหลือ 6 วัน", "ใช้ไป 6 / 10 วัน · ใกล้หมด", 0.6, "#ca8a04")

        # การ์ดล่าง: เกณฑ์การลา
        rules_card = ctk.CTkFrame(right_panel, fg_color="#222224", corner_radius=12)
        # เปลี่ยนไปใช้ระบบ grid เช่นกัน
        rules_card.grid(row=1, column=0, sticky="nsew")

        title_rules = ctk.CTkLabel(rules_card, text="ℹ️ เกณฑ์การลา", font=("Helvetica", 14, "bold"), text_color="#ffffff")
        title_rules.pack(anchor="w", padx=20, pady=(15, 10))

        rules_text = (
            "• ลาป่วย: 30 วัน/ปี (มีเงินเดือน)\n"
            "• ลากิจ: 10 วัน/ปี\n"
            "• ลาพักร้อน: 10 วัน/ปี (แจ้งล่วงหน้า 3 วัน)\n"
            "• ลาคลอด: 98 วัน"
        )
        lbl_rules_content = ctk.CTkLabel(rules_card, text=rules_text, font=("Helvetica", 12), text_color="#d1d1d6", justify="left")
        lbl_rules_content.pack(anchor="w", padx=25, pady=5)