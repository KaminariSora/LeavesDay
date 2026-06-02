import customtkinter as ctk

# ตั้งค่าธีมเริ่มต้นเป็น Dark Mode และโทนสีน้ำเงิน
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ExportDialog(ctk.CTk):
    def __init__(self):
        super().__init__()

        # ตั้งค่าหน้าต่างหลัก (จำลองเป็นพื้นหลังสีดำเข้มแบบในภาพ)
        self.title("หน้า 8 — EXPORT ข้อมูล (DIALOG)")
        self.geometry("900integrity_check") 
        self.geometry("950x550")
        self.configure(fg_color="#0e0e10")  # สีพื้นหลังนอก Dialog

        # --- สร้างการ์ด Dialog ตรงกลาง ---
        self.dialog_frame = ctk.CTkFrame(self, width=420, height=480, fg_color="#222224", corner_radius=12)
        self.dialog_frame.place(relx=0.5, rely=0.5, anchor="center")
        self.dialog_frame.pack_propagate(False)

        # ส่วนหัว (Header)
        self.header_label = ctk.CTkLabel(
            self.dialog_frame, 
            text="📥 Export ข้อมูลการลา", 
            font=("Helvetica", 18, "bold"), 
            text_color="#ffffff"
        )
        self.header_label.pack(anchor="w", padx=25, pady=(25, 15))

        # --- ส่วนที่ 1: รูปแบบไฟล์ (File Format) ---
        self.format_label = ctk.CTkLabel(self.dialog_frame, text="รูปแบบไฟล์", font=("Helvetica", 13), text_color="#a0a0a5")
        self.format_label.pack(anchor="w", padx=25, pady=(5, 5))

        self.file_frame = ctk.CTkFrame(self.dialog_frame, fg_color="transparent")
        self.file_frame.pack(fill="x", padx=25, pady=5)

        # ปุ่ม Excel (เลือกอยู่ - สีน้ำเงิน)
        self.btn_excel = ctk.CTkButton(
            self.file_frame, text="📄\nExcel (.xlsx)", font=("Helvetica", 12),
            width=115, height=65, fg_color="#1a365d", border_color="#3182ce", border_width=2, text_color="#93c5fd"
        )
        self.btn_excel.pack(side="left", padx=(0, 8))

        # ปุ่ม CSV
        self.btn_csv = ctk.CTkButton(
            self.file_frame, text="📄\nCSV (.csv)", font=("Helvetica", 12),
            width=115, height=65, fg_color="#2a2a2b", border_color="#4a4a4a", border_width=1, text_color="#d1d1d6"
        )
        self.btn_csv.pack(side="left", padx=8)

        # ปุ่ม PDF
        self.btn_pdf = ctk.CTkButton(
            self.file_frame, text="📄\nPDF", font=("Helvetica", 12),
            width=115, height=65, fg_color="#2a2a2b", border_color="#4a4a4a", border_width=1, text_color="#d1d1d6"
        )
        self.btn_pdf.pack(side="left", padx=(8, 0))

        # --- ส่วนที่ 2: ช่วงเวลา (Date Range) ---
        self.time_label = ctk.CTkLabel(self.dialog_frame, text="ช่วงเวลา", font=("Helvetica", 13), text_color="#a0a0a5")
        self.time_label.pack(anchor="w", padx=25, pady=(15, 5))

        self.date_frame = ctk.CTkFrame(self.dialog_frame, fg_color="transparent")
        self.date_frame.pack(fill="x", padx=25, pady=5)

        self.date_start = ctk.CTkEntry(self.date_frame, width=175, height=35, fg_color="#2a2a2b", border_color="#4a4a4a", placeholder_text="📅 01/01/2568", text_color="#ffffff")
        self.date_start.insert(0, "📅  01/01/2568")
        self.date_start.pack(side="left", padx=(0, 10))

        self.date_end = ctk.CTkEntry(self.date_frame, width=175, height=35, fg_color="#2a2a2b", border_color="#4a4a4a", placeholder_text="📅 31/03/2568", text_color="#ffffff")
        self.date_end.insert(0, "📅  31/03/2568")
        self.date_end.pack(side="left")

        # --- ส่วนที่ 3: กรองข้อมูล (Filters) ---
        self.filter_label = ctk.CTkLabel(self.dialog_frame, text="กรองข้อมูล", font=("Helvetica", 13), text_color="#a0a0a5")
        self.filter_label.pack(anchor="w", padx=25, pady=(15, 5))

        self.dropdown_frame = ctk.CTkFrame(self.dialog_frame, fg_color="transparent")
        self.dropdown_frame.pack(fill="x", padx=25, pady=5)

        self.user_filter = ctk.CTkOptionMenu(self.dropdown_frame, width=175, height=35, values=["ทุกคน", "เฉพาะฉัน"], fg_color="#2a2a2b", button_color="#2a2a2b", text_color="#ffffff")
        self.user_filter.pack(side="left", padx=(0, 10))

        self.status_filter = ctk.CTkOptionMenu(self.dropdown_frame, width=175, height=35, values=["ทุกสถานะ", "อนุมัติแล้ว", "รออนุมัติ"], fg_color="#2a2a2b", button_color="#2a2a2b", text_color="#ffffff")
        self.status_filter.pack(side="left")

        # --- ส่วนที่ 4: กล่องสรุปข้อมูล (Summary Box) ---
        self.summary_frame = ctk.CTkFrame(self.dialog_frame, height=38, fg_color="#1c1c1e", corner_radius=6)
        self.summary_frame.pack(fill="x", padx=25, pady=20)
        self.summary_frame.pack_propagate(False)

        self.summary_label = ctk.CTkLabel(
            self.summary_frame, 
            text="พบ 24 รายการ • รวม 87 วัน • ขนาดไฟล์โดยประมาณ 45 KB", 
            font=("Helvetica", 11), 
            text_color="#8e8e93"
        )
        self.summary_label.place(relx=0.5, rely=0.5, anchor="center")

        # --- ส่วนที่ 5: ปุ่มกดยกเลิก / ดาวน์โหลด (Action Buttons) ---
        self.action_frame = ctk.CTkFrame(self.dialog_frame, fg_color="transparent")
        self.action_frame.pack(fill="x", padx=25, pady=(5, 0))

        # ปุ่มดาวน์โหลด (สีน้ำเงินเข้ม)
        self.btn_download = ctk.CTkButton(
            self.action_frame, text="📥 ดาวน์โหลด", font=("Helvetica", 13, "bold"),
            width=270, height=38, fg_color="#23426f", hover_color="#1d3557", text_color="#93c5fd"
        )
        self.btn_download.pack(side="left", padx=(0, 10))

        # ปุ่มยกเลิก
        self.btn_cancel = ctk.CTkButton(
            self.action_frame, text="ยกเลิก", font=("Helvetica", 13),
            width=80, height=38, fg_color="#2a2a2b", hover_color="#3a3a3c", text_color="#ffffff", border_color="#4a4a4a", border_width=1
        )
        self.btn_cancel.pack(side="left")

if __name__ == "__main__":
    app = ExportDialog()
    app.mainloop()