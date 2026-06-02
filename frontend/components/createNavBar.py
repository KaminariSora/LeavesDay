import customtkinter as ctk

class NavBar(ctk.CTkFrame):
    def __init__(self, master, change_page_callback, **kwargs):
        super().__init__(master, height=60, fg_color="#222224", corner_radius=0, **kwargs)
        self.pack_propagate(False)
        
        self.change_page = change_page_callback

        # โลโก้แอป
        logo_label = ctk.CTkLabel(self, text="📅 LeaveSystem", font=("Helvetica", 18, "bold"), text_color="#ffffff")
        logo_label.pack(side="left", padx=(25, 20))

        # --- สร้างปุ่มเมนู และเก็บไว้ใน Dictionary เพื่อให้เรียกจัดการง่ายๆ ---
        self.menu_buttons = {}

        # ปุ่มขอลา (leave)
        self.menu_buttons["leave"] = ctk.CTkButton(
            self, text="ขอลา", font=("Helvetica", 13), width=75, height=32,
            command=lambda: self.change_page("leave")
        )
        self.menu_buttons["leave"].pack(side="left", padx=5)

        # ปุ่มประวัติ (history)
        self.menu_buttons["history"] = ctk.CTkButton(
            self, text="ประวัติ", font=("Helvetica", 13), width=75, height=32,
            command=lambda: self.change_page("history")
        )
        self.menu_buttons["history"].pack(side="left", padx=5)

        # ปุ่ม setting
        self.menu_buttons["setting"] = ctk.CTkButton(
            self, text="ตั้งค่า", font=("Helvetica", 13), width=75, height=32,
            command=lambda: self.change_page("setting")
        )
        self.menu_buttons["setting"].pack(side="left", padx=5)

        # ปุ่ม อนุมัติ
        self.menu_buttons["approve"] = ctk.CTkButton(
            self, text="การอนุมัติ", font=("Helvetica", 13), width=75, height=32,
            command=lambda: self.change_page("approve")
        )
        self.menu_buttons["approve"].pack(side="left", padx=5)

        # ปุ่ม profile
        self.menu_buttons["profile"] = ctk.CTkButton(
            self, text="profile", font=("Helvetica", 13), width=75, height=32,
            command=lambda: self.change_page("profile")
        )
        self.menu_buttons["profile"].pack(side="left", padx=5)

        # ปุ่ม ภาพรวม
        self.menu_buttons["overview"] = ctk.CTkButton(
            self, text="overview", font=("Helvetica", 13), width=75, height=32,
            command=lambda: self.change_page("overview")
        )
        self.menu_buttons["overview"].pack(side="left", padx=5)

        # เมนูโปรไฟล์ฝั่งขวา
        profile_frame = ctk.CTkFrame(self, fg_color="transparent")
        profile_frame.pack(side="right", padx=25)
        avatar = ctk.CTkLabel(profile_frame, text="สช", font=("Helvetica", 12, "bold"), width=32, height=32, fg_color="#1e3a8a", text_color="#93c5fd", corner_radius=16)
        avatar.pack(side="left", padx=(0, 10))
        user_name = ctk.CTkLabel(profile_frame, text="สมชาย รักดี", font=("Helvetica", 13), text_color="#ffffff")
        user_name.pack(side="left")

    def update_highlight(self, active_page):
        """ฟังก์ชันสำหรับเปลี่ยนสีไฮไลต์ของปุ่มตามชื่อหน้าที่เปิดอยู่"""
        for page_name, btn in self.menu_buttons.items():
            if page_name == active_page:
                # ปุ่มของหน้าปัจจุบัน: ปรับเป็นสีน้ำเงินเด่น อักษรตัวหนาสีขาว
                btn.configure(
                    fg_color="#1e3a8a", 
                    hover_color="#1e40af", 
                    text_color="#ffffff",
                    font=("Helvetica", 13, "bold")
                )
            else:
                # ปุ่มของหน้าอื่น: ปรับเป็นสีโปร่งใส ตัวอักษรสีเทาขุ่น
                btn.configure(
                    fg_color="transparent", 
                    hover_color="#2a2a2b", 
                    text_color="#a0a0a5",
                    font=("Helvetica", 13)
                )