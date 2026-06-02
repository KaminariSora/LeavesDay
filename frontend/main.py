import customtkinter as ctk
from components.createNavBar import NavBar
from dashboardPage.dashboard import DashboardPage
from historyPage.history import LeaveHistoryPage
from settingPage.setting import SettingsSystemApp
from approvePage.approve import ApprovePage
from profilePage.profile import MyProfilePage
from overviewPage.overview import OverviewPage
# สมมติว่าในอนาคตคุณ import หน้าอื่นๆ เข้ามาตรงนี้ เช่น:
# from historyPage.history import LeaveHistoryPage

# ตั้งค่าธีมหลักเป็น Dark Mode
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class LeaveSystemApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # ตั้งค่าหน้าต่างโปรแกรม
        self.title("LeaveSystem Dashboard")
        self.geometry("1100x650")
        self.configure(fg_color="#141416")  # สีพื้นหลังหลักของแอป

        # 1. สร้าง Navbar แปะไว้บนสุดถาวร และส่งฟังก์ชันคอลแบ็กเข้าไป
        self.navbar = NavBar(master=self, change_page_callback=self.show_page)
        self.navbar.pack(fill="x", side="top")

        # 2. สร้าง Container หลักสำหรับพื้นที่เนื้อหาตรงกลาง (Content Area)
        self.content_container = ctk.CTkFrame(self, fg_color="transparent")
        self.content_container.pack(fill="both", expand=True)

        self.current_page = None

        # 3. เปิดแอปขึ้นมาให้แสดงหน้าแรก (หน้าขอลา/แดชบอร์ด) ทันที
        self.show_page("leave")

    def show_page(self, page_name):
        """ฟังก์ชันคุมระบบสลับหน้าจอตามสัญญาณที่ส่งมาจาก Navbar"""
        # เคลียร์หน้าจอเดิมทิ้งก่อน (ถ้ามี)
        if self.current_page is not None:
            self.current_page.pack_forget()
            self.current_page.destroy()

        # เลือกว่าจะเปิดหน้าไหนขึ้นมาแสดง
        if page_name == "leave":
            self.current_page = DashboardPage(master=self.content_container)
        elif page_name == "history":
            self.current_page = LeaveHistoryPage(master=self.content_container)
        elif page_name == "setting":
            self.current_page = SettingsSystemApp(master=self.content_container)
        elif page_name == "approve":
            self.current_page = ApprovePage(master=self.content_container)
        elif page_name == "profile":
            self.current_page = MyProfilePage(master=self.content_container)
        elif page_name == "overview":
            self.current_page = OverviewPage(master=self.content_container)

        # สั่งแสดงผลหน้าย่อยที่ถูกเลือกเต็มพื้นที่
        self.current_page.pack(fill="both", expand=True)

        # 🔥 เพิ่มบรรทัดนี้: สั่งให้ Navbar อัปเดตสีไฮไลต์ของปุ่มให้ตรงกับหน้าปัจจุบัน
        self.navbar.update_highlight(page_name)


# ==========================================
# 📦 ย้ายฟังก์ชันสร้าง Content เดิมมาไว้ใน Class นี้
# ==========================================
if __name__ == "__main__":
    app = LeaveSystemApp()
    app.mainloop()