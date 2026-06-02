import customtkinter as ctk

# ตั้งค่าธีมหลักเป็น Dark Mode
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class LoginScreenApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # ตั้งค่าหน้าต่างโปรแกรม (จำลองขนาดหน้าจอหลัก)
        self.title("Leave Management System - Login")
        self.geometry("950x550")
        self.configure(fg_color="#141416")  # สีพื้นหลังหลักภายนอกการ์ด

        self.create_login_card()

    def create_login_card(self):
        """สร้างการ์ด Dialog เข้าสู่ระบบตรงกลางหน้าจอ"""
        # กล่อง Login Card
        login_card = ctk.CTkFrame(self, width=380, height=480, fg_color="#222224", corner_radius=16)
        login_card.place(relx=0.5, rely=0.5, anchor="center")
        login_card.pack_propagate(False)

        # 1. โลโก้ไอคอนปฏิทิน (จำลองด้วยรูปสี่เหลี่ยมโค้งสีน้ำเงินเข้มและอิโมจิ)
        logo_frame = ctk.CTkFrame(login_card, width=70, height=70, fg_color="#1e3a8a", corner_radius=16)
        logo_frame.pack(pady=(45, 15))
        logo_frame.pack_propagate(False)
        
        lbl_logo_icon = ctk.CTkLabel(logo_frame, text="📅", font=("Helvetica", 28))
        lbl_logo_icon.place(relx=0.5, rely=0.5, anchor="center")

        # 2. ชื่อระบบ (Title)
        lbl_title_th = ctk.CTkLabel(login_card, text="ระบบบันทึกการลา", font=("Helvetica", 18, "bold"), text_color="#ffffff")
        lbl_title_th.pack(pady=(0, 2))
        
        lbl_title_en = ctk.CTkLabel(login_card, text="Leave Management System", font=("Helvetica", 13), text_color="#a0a0a5")
        lbl_title_en.pack(pady=(0, 25))

        # 3. ช่องกรอกข้อมูล บัญชีองค์กร (Email Input Container)
        input_container = ctk.CTkFrame(login_card, fg_color="#1c1c1e", height=75, border_color="#4a4a4a", border_width=1, corner_radius=10)
        input_container.pack(fill="x", padx=30, pady=10)
        input_container.pack_propagate(False)

        lbl_input_title = ctk.CTkLabel(input_container, text="บัญชีองค์กร", font=("Helvetica", 11), text_color="#8e8e93")
        lbl_input_title.pack(anchor="w", padx=15, pady=(8, 0))

        ent_email = ctk.CTkEntry(
            input_container, 
            fg_color="transparent", 
            border_width=0, 
            text_color="#ffffff", 
            font=("Helvetica", 13),
            placeholder_text="somchai@company.co.th"
        )
        ent_email.insert(0, "somchai@company.co.th")
        ent_email.pack(fill="x", padx=11, pady=(0, 5))

        # 4. ปุ่มเข้าสู่ระบบด้วย Microsoft (SSO Button)
        btn_sso = ctk.CTkButton(
            login_card, 
            text="🪟 เข้าสู่ระบบด้วย Microsoft", 
            font=("Helvetica", 13, "bold"), 
            fg_color="#23426f", 
            hover_color="#1d3557", 
            text_color="#93c5fd",
            height=42,
            corner_radius=8,
            command=self.handle_login
        )
        btn_sso.pack(fill="x", padx=30, pady=(15, 15))

        # 5. คำอธิบายเพิ่มเติมด้านล่าง (Footer)
        lbl_footer = ctk.CTkLabel(
            login_card, 
            text="Single Sign-On ผ่าน Azure Active Directory", 
            font=("Helvetica", 11), 
            text_color="#8e8e93"
        )
        lbl_footer.pack(pady=(10, 20))

    def handle_login(self):
        """ฟังก์ชันสำหรับจัดการเมื่อกดปุ่มล็อกอิน"""
        print("กำลังเชื่อมต่อกับ Azure Active Directory...")


if __name__ == "__main__":
    app = LoginScreenApp()
    app.mainloop()