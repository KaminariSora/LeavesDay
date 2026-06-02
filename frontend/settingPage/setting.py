import customtkinter as ctk

# ตั้งค่าธีมหลักเป็น Dark Mode และโทนสีหลัก
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SettingsSystemApp(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        # สืบทอดคุณสมบัติแบบ Frame
        super().__init__(master, fg_color="transparent", **kwargs)
        
        # 🔥 แก้ไขจุดที่ 1: เปลี่ยนชื่อเรียกฟังก์ชันให้ตรงกับด้านล่าง
        self.create_main_content()

    def create_main_content(self):
        """ส่วนเนื้อหาหลัก แบ่งฝั่งซ้าย (ฟอร์มตั้งค่า+กลุ่ม) และ ฝั่งขวา (ตัวอย่างข้อความ)"""
        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=25, pady=25)

        # กำหนดสัดส่วนคอลัมน์ ฝั่งซ้าย 50% ฝั่งขวา 50%
        container.grid_columnconfigure((0, 1), weight=1, uniform="equal")
        container.grid_rowconfigure(0, weight=1)

        # ==========================================
        # 🛠️ ฝั่งซ้าย: ตั้งค่า LINE Notify & กลุ่มการแจ้งเตือน
        # ==========================================
        left_panel = ctk.CTkFrame(container, fg_color="transparent")
        left_panel.grid(row=0, column=0, sticky="nsew", padx=(0, 12))
        
        # 1. การ์ดตั้งค่า LINE Notify (บน)
        notify_card = ctk.CTkFrame(left_panel, fg_color="#222224", corner_radius=12)
        notify_card.pack(fill="both", expand=True, pady=(0, 12))

        lbl_title_config = ctk.CTkLabel(notify_card, text="💬 ตั้งค่า LINE Notify", font=("Helvetica", 15, "bold"), text_color="#ffffff")
        lbl_title_config.pack(anchor="w", padx=25, pady=(20, 10))

        # กล่องรายละเอียดฟอร์มภายใน
        form_inner = ctk.CTkFrame(notify_card, fg_color="#1c1c1e", corner_radius=8)
        form_inner.pack(fill="both", expand=True, padx=25, pady=(0, 20))

        desc_text = "เชื่อมต่อ LINE Notify เพื่อรับแจ้งเตือนสถานะการลาแบบ real-time\nผ่านกลุ่ม LINE ขององค์กร"
        lbl_desc = ctk.CTkLabel(form_inner, text=desc_text, font=("Helvetica", 12), text_color="#a0a0a5", justify="left")
        lbl_desc.pack(anchor="w", padx=20, pady=(15, 10))

        lbl_token = ctk.CTkLabel(form_inner, text="LINE Notify Token", font=("Helvetica", 12), text_color="#a0a0a5")
        lbl_token.pack(anchor="w", padx=20, pady=(5, 2))

        # ช่องกรอก Token (จำลองสัญลักษณ์ซ่อนรหัสและปุ่มรูปตา)
        token_frame = ctk.CTkFrame(form_inner, fg_color="transparent")
        token_frame.pack(fill="x", padx=20, pady=2)
        
        ent_token = ctk.CTkEntry(token_frame, fg_color="#2a2a2b", border_color="#4a4a4a", text_color="#ffffff", height=35)
        ent_token.insert(0, "")
        ent_token.pack(side="left", fill="x", expand=True)
        
        lbl_eye = ctk.CTkLabel(token_frame, text="👁️", font=("Helvetica", 14), text_color="#8e8e93", width=30)
        lbl_eye.pack(side="right", padx=(5, 0))

        # Checkboxes ส่วนแจ้งเตือนเมื่อ...
        lbl_notify_when = ctk.CTkLabel(form_inner, text="แจ้งเตือนเมื่อ", font=("Helvetica", 12), text_color="#a0a0a5")
        lbl_notify_when.pack(anchor="w", padx=20, pady=(10, 5))

        cb_1 = ctk.CTkCheckBox(form_inner, text="ส่งคำขอลาใหม่", font=("Helvetica", 12), text_color="#ffffff")
        cb_1.select()
        cb_1.pack(anchor="w", padx=20, pady=3)

        cb_2 = ctk.CTkCheckBox(form_inner, text="อนุมัติคำขอ", font=("Helvetica", 12), text_color="#ffffff")
        cb_2.select()
        cb_2.pack(anchor="w", padx=20, pady=3)

        cb_3 = ctk.CTkCheckBox(form_inner, text="ปฏิเสธคำขอ", font=("Helvetica", 12), text_color="#ffffff")
        cb_3.pack(anchor="w", padx=20, pady=3)

        cb_4 = ctk.CTkCheckBox(form_inner, text="วันลาเหลือน้อยกว่า 3 วัน", font=("Helvetica", 12), text_color="#ffffff")
        cb_4.select()
        cb_4.pack(anchor="w", padx=20, pady=3)

        # ปุ่มทดสอบส่งข้อความ
        btn_test = ctk.CTkButton(form_inner, text="🚀 ทดสอบส่งข้อความ", font=("Helvetica", 12, "bold"), fg_color="#1e3a8a", hover_color="#1e40af", height=34)
        btn_test.pack(anchor="w", padx=20, pady=(15, 15))

        # 2. การ์ดกลุ่มการแจ้งเตือน (ล่าง)
        group_card = ctk.CTkFrame(left_panel, fg_color="#222224", corner_radius=12)
        group_card.pack(fill="x", pady=(12, 0))

        lbl_title_group = ctk.CTkLabel(group_card, text="👥 กลุ่มการแจ้งเตือน", font=("Helvetica", 15, "bold"), text_color="#ffffff")
        lbl_title_group.pack(anchor="w", padx=25, pady=(15, 10))

        # ฟังก์ชันช่วยสร้างแถวกลุ่ม LINE
        def create_group_row(parent, name, status_text, is_connected=True):
            row = ctk.CTkFrame(parent, fg_color="#1c1c1e", height=40, border_color="#4a4a4a", border_width=1)
            row.pack(fill="x", padx=25, pady=4)
            row.pack_propagate(False)
            
            lbl_icon = ctk.CTkLabel(row, text="🟢", font=("Helvetica", 11), width=25)
            lbl_icon.pack(side="left", padx=(10, 0))
            
            lbl_name = ctk.CTkLabel(row, text=name, font=("Helvetica", 13), text_color="#ffffff")
            lbl_name.pack(side="left")
            
            lbl_status = ctk.CTkLabel(row, text=status_text, font=("Helvetica", 11, "bold"), text_color="#16a34a" if is_connected else "#8e8e93", fg_color="#14532d" if is_connected else "transparent", corner_radius=4, width=70, height=22)
            lbl_status.pack(side="right", padx=10)

        create_group_row(group_card, "กลุ่ม HR ทั้งหมด", "เชื่อมแล้ว")
        create_group_row(group_card, "กลุ่มผู้บริหาร", "เชื่อมแล้ว")

        # ปุ่มเพิ่มกลุ่มใหม่ (แบบตารางจุดประ)
        btn_add_group = ctk.CTkButton(group_card, text="+ เพิ่มกลุ่มใหม่", font=("Helvetica", 13), fg_color="transparent", border_color="#4a4a4a", border_width=1, border_spacing=5, text_color="#a0a0a5", hover_color="#2a2a2b", height=38)
        btn_add_group.pack(fill="x", padx=25, pady=(8, 15))


        # ==========================================
        # 📱 ฝั่งขวา: ตัวอย่างข้อความ LINE (Previews)
        # ==========================================
        right_panel = ctk.CTkFrame(container, fg_color="#222224", corner_radius=12)
        right_panel.grid(row=0, column=1, sticky="nsew", padx=(12, 0))

        lbl_title_preview = ctk.CTkLabel(right_panel, text="💬 ตัวอย่างข้อความ LINE", font=("Helvetica", 15, "bold"), text_color="#ffffff")
        lbl_title_preview.pack(anchor="w", padx=25, pady=(20, 15))

        # การ์ดตัวอย่างที่ 1: คำขอลาใหม่
        msg_1 = ctk.CTkFrame(right_panel, fg_color="#1c1c1e", corner_radius=8)
        msg_1.pack(fill="x", padx=25, pady=6)
        txt_1 = (
            "📄 คำขอลาใหม่\n"
            "พนักงาน:  สมชาย รักดี\n"
            "ประเภท:  ลาพักร้อน\n"
            "วันที่:  20-21 มี.ค. 2568\n"
            "จำนวน:  2 วัน\n"
            "สถานะ:  รออนุมัติ"
        )
        lbl_msg1 = ctk.CTkLabel(msg_1, text=txt_1, font=("Helvetica", 12), text_color="#d1d1d6", justify="left")
        lbl_msg1.pack(anchor="w", padx=20, pady=12)

        # การ์ดตัวอย่างที่ 2: อนุมัติแล้ว
        msg_2 = ctk.CTkFrame(right_panel, fg_color="#1c1c1e", corner_radius=8)
        msg_2.pack(fill="x", padx=25, pady=6)
        txt_2 = (
            "✅ อนุมัติแล้ว\n"
            "สมชาย รักดี  —  ลาพักร้อน 2 วัน\n"
            "อนุมัติโดย:  ผจก. สุขใจ ดีงาม\n"
            "วันลาคงเหลือ:  4 วัน"
        )
        lbl_msg2 = ctk.CTkLabel(msg_2, text=txt_2, font=("Helvetica", 12), text_color="#d1d1d6", justify="left")
        lbl_msg2.pack(anchor="w", padx=20, pady=12)

        # การ์ดตัวอย่างที่ 3: วันลาใกล้หมด
        msg_3 = ctk.CTkFrame(right_panel, fg_color="#1c1c1e", corner_radius=8)
        msg_3.pack(fill="x", padx=25, pady=6)
        txt_3 = (
            "⚠️ วันลาใกล้หมด\n"
            "มาลี สวยงาม\n"
            "ลาพักร้อนเหลือเพียง  2 วัน"
        )
        lbl_msg3 = ctk.CTkLabel(msg_3, text=txt_3, font=("Helvetica", 12), text_color="#d1d1d6", justify="left")
        lbl_msg3.pack(anchor="w", padx=20, pady=12)


if __name__ == "__main__":
    app = SettingsSystemApp()
    app.mainloop()