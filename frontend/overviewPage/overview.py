import customtkinter as ctk

class OverviewPage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.create_main_content()

    def create_main_content(self):
        # ==========================================
        # 📊 ส่วนที่ 1: กล่องสถิติ 4 ช่องด้านบน (Top Summary Cards)
        # ==========================================
        summary_grid = ctk.CTkFrame(self, fg_color="transparent")
        summary_grid.pack(fill="x", padx=25, pady=(20, 10))
        summary_grid.grid_columnconfigure((0, 1, 2, 3), weight=1)

        top_cards = [
            ("พนักงานทั้งหมด", "42", "4 แผนก", "#ffffff"),
            ("วันลารวมปีนี้", "87", "ทุกประเภท", "#ffffff"),
            ("รออนุมัติ", "5", "คำขอ", "#ca8a04"),
            ("ลาป่วยสูงสุด", "8", "วัน (มาลี)", "#ffffff")
        ]

        for i, (title, num, sub, num_color) in enumerate(top_cards):
            card = ctk.CTkFrame(summary_grid, fg_color="#222224", corner_radius=12, height=110)
            p_left = 0 if i == 0 else 8
            p_right = 0 if i == 3 else 8
            card.grid(row=0, column=i, sticky="ew", padx=(p_left, p_right))
            card.pack_propagate(False)

            ctk.CTkLabel(card, text=title, font=("Helvetica", 12), text_color="#a0a0a5").pack(anchor="w", padx=20, pady=(15, 2))
            ctk.CTkLabel(card, text=num, font=("Helvetica", 30, "bold"), text_color=num_color).pack(anchor="w", padx=20)
            ctk.CTkLabel(card, text=sub, font=("Helvetica", 11), text_color="#8e8e93").pack(anchor="w", padx=20, pady=(0, 15))


        # ==========================================
        # 📈 ส่วนที่ 2: วันลาแต่ละแผนก & ประเภทการลา (Middle Charts)
        # ==========================================
        middle_layout = ctk.CTkFrame(self, fg_color="transparent")
        middle_layout.pack(fill="x", padx=25, pady=10)
        middle_layout.grid_columnconfigure((0, 1), weight=1) # แบ่งครึ่งซ้าย-ขวา 50/50 เท่ากัน

        # --- ฝั่งซ้าย: วันลาแต่ละแผนก ---
        dept_card = ctk.CTkFrame(middle_layout, fg_color="#222224", corner_radius=12, height=210)
        dept_card.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        
        ctk.CTkLabel(dept_card, text="🏢 วันลาแต่ละแผนก", font=("Helvetica", 14, "bold"), text_color="#ffffff").pack(anchor="w", padx=20, pady=(15, 10))

        def create_dept_row(dept_name, days_str, progress):
            row = ctk.CTkFrame(dept_card, fg_color="transparent")
            row.pack(fill="x", padx=20, pady=2)
            ctk.CTkLabel(row, text=dept_name, font=("Helvetica", 12), text_color="#ffffff").pack(side="left")
            ctk.CTkLabel(row, text=days_str, font=("Helvetica", 12, "bold"), text_color="#ffffff").pack(side="right")
            
            pbar = ctk.CTkProgressBar(dept_card, height=6, progress_color="#2563eb", fg_color="#141416")
            pbar.set(progress)
            pbar.pack(fill="x", padx=20, pady=(1, 6))

        create_dept_row("HR", "24 วัน", 0.8)
        create_dept_row("Finance", "22 วัน", 0.73)
        create_dept_row("IT", "18 วัน", 0.6)
        create_dept_row("Sales", "12 วัน", 0.4)

        # --- ฝั่งขวา: ประเภทการลาทั้งบริษัท (Bar Chart จำลอง) ---
        type_card = ctk.CTkFrame(middle_layout, fg_color="#222224", corner_radius=12, height=210)
        type_card.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        
        ctk.CTkLabel(type_card, text="📊 ประเภทการลาทั้งบริษัท", font=("Helvetica", 14, "bold"), text_color="#ffffff").pack(anchor="w", padx=20, pady=(15, 5))

        # พื้นที่แสดงแท่งกราฟ
        graph_body = ctk.CTkFrame(type_card, fg_color="transparent")
        graph_body.pack(fill="both", expand=True, padx=30, pady=(5, 10))
        graph_body.grid_columnconfigure((0, 1, 2), weight=1)

        bars_data = [
            ("38", 0.8, "#1e3a8a", "ลาป่วย"),
            ("21", 0.45, "#14532d", "ลากิจ"),
            ("28", 0.6, "#7c2d12", "ลาพักร้อน")
        ]

        for col, (num, val, color, label_text) in enumerate(bars_data):
            bar_container = ctk.CTkFrame(graph_body, fg_color="transparent")
            bar_container.grid(row=0, column=col, sticky="ns") # ยืดแนวตั้งเพื่อดันกราฟขึ้น
            
            # บังคับวิดเจ็ตในแท่งกราฟเรียงจากล่างขึ้นบน
            ctk.CTkLabel(bar_container, text=num, font=("Helvetica", 12, "bold"), text_color="#ffffff").pack(side="top", pady=(5, 2))
            
            # แท่งกราฟจำลองปรับความสูงตามตัวแปร val
            mock_bar = ctk.CTkFrame(bar_container, width=75, height=int(90 * val), fg_color=color, corner_radius=4)
            mock_bar.pack(side="top")
            mock_bar.pack_propagate(False)

        # แถบอธิบายสีด้านล่างกราฟแท่ง (Legend)
        legend_row = ctk.CTkFrame(type_card, fg_color="transparent")
        legend_row.pack(fill="x", pady=(0, 15))
        
        # จัดกึ่งกลางป้ายอธิบายสีแบบเว้นช่องไฟเท่าๆ กัน
        legend_center = ctk.CTkFrame(legend_row, fg_color="transparent")
        legend_center.pack(anchor="center")
        
        for text, color in [("ลาป่วย", "#2563eb"), ("ลากิจ", "#16a34a"), ("พักร้อน", "#ca8a04")]:
            item = ctk.CTkFrame(legend_center, fg_color="transparent")
            item.pack(side="left", padx=10)
            dot = ctk.CTkFrame(item, width=10, height=10, fg_color=color, corner_radius=5)
            dot.pack(side="left", padx=(0, 6))
            ctk.CTkLabel(item, text=text, font=("Helvetica", 11), text_color="#a0a0a5").pack(side="left")


        # ==========================================
        # 👥 ส่วนที่ 3: ตารางวันลาคงเหลือรายบุคคล (Table Area)
        # ==========================================
        table_card = ctk.CTkFrame(self, fg_color="#222224", corner_radius=12)
        table_card.pack(fill="both", expand=True, padx=25, pady=(10, 20))

        # แถบควบคุมด้านบนของตาราง (Header ตาราง + ปุ่ม Export)
        table_header = ctk.CTkFrame(table_card, fg_color="transparent")
        table_header.pack(fill="x", padx=20, pady=(15, 10))
        
        ctk.CTkLabel(table_header, text="👥 วันลาคงเหลือรายบุคคล", font=("Helvetica", 14, "bold"), text_color="#ffffff").pack(side="left")
        
        btn_export = ctk.CTkButton(table_header, text="📥 Export ยอดคงเหลือ", font=("Helvetica", 11, "bold"), fg_color="#14532d", hover_color="#166534", text_color="#4ade80", height=28, corner_radius=6)
        btn_export.pack(side="right")

        # สกรอลล์สำหรับรายชื่อพนักงาน
        table_scroll = ctk.CTkScrollableFrame(table_card, fg_color="transparent")
        table_scroll.pack(fill="both", expand=True, padx=20, pady=(0, 15))

        # ตั้งคอลัมน์ตาราง (7 คอลัมน์) กระจายสัดส่วนตามความกว้าง
        headers = [("พนักงาน", 22), ("แผนก", 10), ("ลาป่วย", 12), ("ลากิจ", 12), ("พักร้อน", 12), ("รวมใช้", 12), ("%ใช้", 20)]
        for i, (_, weight) in enumerate(headers):
            table_scroll.grid_columnconfigure(i, weight=weight, uniform="overview_cols")

        # สร้างหัวตาราง (Headers)
        for i, (text, _) in enumerate(headers):
            lbl = ctk.CTkLabel(table_scroll, text=text, font=("Helvetica", 12, "bold"), text_color="#8e8e93", anchor="w" if i < 2 else "center")
            lbl.grid(row=0, column=i, sticky="ew", padx=5, pady=(0, 8))

        # ข้อมูลพนักงานจำลองรายบุคคล
        employees_data = [
            {"avatar": "สช", "av_bg": "#1e3a8a", "av_txt": "#93c5fd", "name": "สมชาย รักดี", "dept": "IT", "sick": "15 วัน", "personal": "7 วัน", "vacation": "6 วัน", "used": "7 วัน", "prog": 0.35, "prog_color": "#2563eb", "percent": "35%"},
            {"avatar": "มล", "av_bg": "#991b1b", "av_txt": "#fca5a5", "name": "มาลี สวยงาม", "dept": "HR", "sick": "22 วัน", "personal": "9 วัน", "vacation": "2 วัน", "used": "17 วัน", "prog": 0.68, "prog_color": "#ca8a04", "percent": "68%"},
            {"avatar": "ปส", "av_bg": "#14532d", "av_txt": "#86efac", "name": "ประสิทธิ์ ทำงาน", "dept": "Sales", "sick": "28 วัน", "personal": "8 วัน", "vacation": "8 วัน", "used": "6 วัน", "prog": 0.22, "prog_color": "#16a34a", "percent": "22%"}
        ]

        for row_idx, emp in enumerate(employees_data, start=1):
            # เซลล์ชื่อพนักงาน + Avatar
            emp_cell = ctk.CTkFrame(table_scroll, fg_color="transparent")
            emp_cell.grid(row=row_idx, column=0, sticky="ew", padx=5, pady=6)
            av = ctk.CTkLabel(emp_cell, text=emp["avatar"], font=("Helvetica", 10, "bold"), width=26, height=26, fg_color=emp["av_bg"], text_color=emp["av_txt"], corner_radius=13)
            av.pack(side="left", padx=(0, 8))
            ctk.CTkLabel(emp_cell, text=emp["name"], font=("Helvetica", 13), text_color="#ffffff").pack(side="left")

            # เซลล์ข้อมูลข้อความธรรมดา (ดึงค่ามาวนลูปออก)
            ctk.CTkLabel(table_scroll, text=emp["dept"], font=("Helvetica", 13), text_color="#d1d1d6", anchor="w").grid(row=row_idx, column=1, sticky="ew", padx=5, pady=6)
            ctk.CTkLabel(table_scroll, text=emp["sick"], font=("Helvetica", 13), text_color="#ffffff", anchor="center").grid(row=row_idx, column=2, sticky="ew", padx=5, pady=6)
            ctk.CTkLabel(table_scroll, text=emp["personal"], font=("Helvetica", 13), text_color="#ffffff", anchor="center").grid(row=row_idx, column=3, sticky="ew", padx=5, pady=6)
            ctk.CTkLabel(table_scroll, text=emp["vacation"], font=("Helvetica", 13), text_color="#ffffff", anchor="center").grid(row=row_idx, column=4, sticky="ew", padx=5, pady=6)
            ctk.CTkLabel(table_scroll, text=emp["used"], font=("Helvetica", 13, "bold"), text_color="#ffffff", anchor="center").grid(row=row_idx, column=5, sticky="ew", padx=5, pady=6)

            # เซลล์แถบเปอร์เซ็นต์ความคืบหน้าด้านขวาสุด
            prog_cell = ctk.CTkFrame(table_scroll, fg_color="transparent")
            prog_cell.grid(row=row_idx, column=6, sticky="ew", padx=5, pady=6)
            prog_cell.grid_columnconfigure(0, weight=1)
            
            pbar = ctk.CTkProgressBar(prog_cell, height=6, progress_color=emp["prog_color"], fg_color="#141416")
            pbar.set(emp["prog"])
            pbar.grid(row=0, column=0, sticky="ew", padx=(0, 10))
            
            ctk.CTkLabel(prog_cell, text=emp["percent"], font=("Helvetica", 11), text_color="#ffffff").grid(row=0, column=1, sticky="e")