# OLP AI Challenge - Computer Vision (CV) Track

Kho lưu trữ mã nguồn chính thức cho dự án Computer Vision trong khuôn khổ cuộc thi OLP AI. Dự án xây dựng hệ thống học máy sử dụng **PyTorch**, 
tuân thủ lập trình hướng module (Modular Programming) nhằm tối ưu hóa hiệu quả phối hợp nhóm không đồng bộ.

---


## 👥 Phân công nhiệm vụ & Sản phẩm bàn giao

LINK [Google Sheets - OLP_AI_CV](https://docs.google.com/spreadsheets/d/1e1VbjHUkjbwBUhNlQzfbxv-ReEsBs5M9sjEl6wFSvQM/edit?gid=1174271979#gid=1174271979)

---

## 📂 Cấu trúc thư mục dự án

```text
olp_ai_cv/
├── data/               # Thư mục chứa dữ liệu thô (Dataset từ BTC) (Clone GitHub về máy local -> Tự tạo folder data/ này riêng -> Đưa dữ liệu thô (ảnh, ...) riêng để  |                         tránh rò rỉ dữ liệu)
├── src/
│   ├── dataset.py      # Định nghĩa CustomDataset & DataLoader chuẩn hóa
│   ├── model.py        # Định nghĩa kiến trúc mạng CNN
│   └── train.py        # Vòng lặp huấn luyện, đánh giá & xuất file nộp bài
└── README.md           # Tài liệu kỹ thuật dự án
```

---


## 📐 Quy tắc phối hợp nhóm

  - Source of Truth: Toàn bộ mã nguồn lưu trữ tập trung trên GitHub. Tuyệt đối không gửi file .py riêng lẻ qua các ứng dụng chat.
  - Kiểm thử độc lập: Mỗi module cá nhân (dataset.py, model.py) bắt buộc phải chạy thử nghiệm độc lập, không lỗi cú pháp và khớp Shape trước khi bàn giao tích hợp.
  - Kỷ luật cập nhật: Tuân thủ quy chế báo cáo tiến độ trước 22h00 hàng ngày và áp dụng nghiêm ngặt Quy tắc 2 giờ khi gặp sự cố kỹ thuật.

---


## ⚡ Luồng xử lý kỹ thuật (Technical Data Flow)

Cả team tuân thủ đúng luồng truyền dữ liệu giữa các file như sau:

```text
  [ data/ ] (Ảnh thô từ BTC)
      │
      ▼
┌─────────────────────────────────────────────────────────┐
│  src/dataset.py (Khôi)                                  │
│  - Đọc ảnh, Augmentation, Resize                        │
│  - Trả về Batch Tensor: Image [B, C, H, W], Label [B]   │
└──────────────────────────┬──────────────────────────────┘
                           │  (Chuyển Batch Tensor)
                           ▼
┌─────────────────────────────────────────────────────────┐
│  src/model.py (Khánh)                                   │
│  - Nhận Input Tensor: [B, C, H, W]                       │
│  - Đưa qua mạng CNN -> Trả về Logits: [B, Num_Classes]   │
└──────────────────────────┬──────────────────────────────┘
                           │  (Chuyển Model & Output)
                           ▼
┌─────────────────────────────────────────────────────────┐
│  src/train.py (Dương)                                   │
│  - Nhận DataLoader từ dataset.py & Model từ model.py    │
│  - Tính Loss/Optimizer, chạy Epoch, Lưu Checkpoint      │
│  - Chạy Inference trên tập Test & Xuất `submission.csv` │
└─────────────────────────────────────────────────────────┘
```

---


## ⚙️ Road Map

```text
+--------------------------------------------------------+
|             PHASE 1: KHỞI TẠO (ĐÃ XONG)                |
|  • Dương  -> Khởi tạo GitHub Repo & Cấu trúc chuẩn     |
+---------------------------+----------------------------+
                            |
                            v
+--------------------------------------------------------+
|          PHASE 2: PHÁT TRIỂN ĐỘC LẬP (Ngày 1 - 4)      |
|  • Khôi   -> Hoàn thiện src/dataset.py                 |
|  • Khánh  -> Hoàn thiện src/model.py                   |
+---------------------------+----------------------------+
                            |
                            v
+--------------------------------------------------------+
|            PHASE 3: TÍCH HỢP & TRAIN (Ngày 5 - 6)      |
|  • Dương  -> Hoàn thiện src/train.py                   |
+---------------------------+----------------------------+
                            |
                            v
+--------------------------------------------------------+
|           PHASE 4: TỐI ƯU & NỘP BÀI (Ngày 7)           |
|  • Toàn đội -> Tinh chỉnh mô hình & submission.csv     |
+--------------------------------------------------------+
```

## 🌐 Môi trường & Quy trình làm việc (Google Colab + Git)

Môi trường khuyến khích: Google Colab (Dùng GPU T4 miễn phí): https://colab.research.google.com/

### 1. Clone Repo về Colab mỗi khi mở session mới (Command Prompt/Terminal) 
``` Command Prompt/Terminal
!git clone [https://github.com/120vey0u/OLP_AI_CV.git](https://github.com/120vey0u/OLP_AI_CV.git)
%cd OLP_AI_CV
```

### 2. Chỉnh sửa mã nguồn (.py)
- Mở menu bên trái Colab → Chọn biểu tượng Files (Thư mục).
- Double-click vào file cần sửa (src/dataset.py, src/model.py) để chỉnh sửa trực tiếp ở giao diện bên phải.

### 3. Chạy thử & Huấn luyện (Python)
```python
!python src/train.py
```

### 4. Commit & Push ngược lại GitHub (Command Prompt/Terminal)
``` Command Prompt/Terminal
!git config --global user.name "Tên_Của_Bạn"
!git config --global user.email "email_github@gmail.com"
!git add .
!git commit -m "Mô tả ngắn gọn thay đổi"
!git push origin master
# Nhập Personal Access Token (PAT) khi được hỏi Password
```

💡 Mẹo: Lưu bộ dữ liệu thô (Dataset) trên Google Drive và mount vào Colab để không mất thời gian upload lại khi hết phiên làm việc (Python): 
``` Python
from google.colab import drive
drive.mount('/content/drive')
```

