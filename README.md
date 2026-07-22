# OLP AI Challenge - Computer Vision (CV) Track

Kho lưu trữ mã nguồn chính thức cho dự án Computer Vision trong khuôn khổ cuộc thi OLP AI. Dự án xây dựng hệ thống học máy sử dụng **PyTorch**, 
tuân thủ lập trình hướng module (Modular Programming) nhằm tối ưu hóa hiệu quả phối hợp nhóm không đồng bộ.

---


## 👥 Phân công nhiệm vụ & Sản phẩm bàn giao

LINK GG SHEET OLP_AI_CV: https://docs.google.com/spreadsheets/d/1e1VbjHUkjbwBUhNlQzfbxv-ReEsBs5M9sjEl6wFSvQM/edit?gid=1174271979#gid=1174271979

---


## 📂 Cấu trúc thư mục dự án

```text
olp_ai_cv/
├── data/               # Thư mục chứa dữ liệu thô (Dataset từ BTC)
├── src/
│   ├── dataset.py      # Định nghĩa CustomDataset & DataLoader chuẩn hóa
│   ├── model.py        # Định nghĩa kiến trúc mạng CNN
│   └── train.py        # Vòng lặp huấn luyện, đánh giá & xuất file nộp bài
├── requirements.txt    # Danh sách thư viện phụ thuộc
└── README.md           # Tài liệu kỹ thuật dự án
```

---


## 📐 Quy tắc phối hợp nhóm

  - Source of Truth: Toàn bộ mã nguồn lưu trữ tập trung trên GitHub. Tuyệt đối không gửi file .py riêng lẻ qua các ứng dụng chat.
  - Kiểm thử độc lập: Mỗi module cá nhân (dataset.py, model.py) bắt buộc phải chạy thử nghiệm độc lập, không lỗi cú pháp và khớp Shape trước khi bàn giao tích hợp.
  - Kỷ luật cập nhật: Tuân thủ quy chế báo cáo tiến độ trước 22h00 hàng ngày và áp dụng nghiêm ngặt Quy tắc 2 giờ khi gặp sự cố kỹ thuật.

---

## ⚙️ Road Map

```mermaid
flowchart TD
    P1["<b>PHASE 1: KHỞI TẠO</b> (Đã xong)<br>• Dương: Repo & Cấu trúc chuẩn"] 
    P2["<b>PHASE 2: PHÁT TRIỂN</b> (Ngày 1 - 4)<br>• Khôi: src/dataset.py<br>• Khánh: src/model.py"]
    P3["<b>PHASE 3: TÍCH HỢP & TRAIN</b> (Ngày 5 - 6)<br>• Dương: src/train.py"]
    P4["<b>PHASE 4: TỐI ƯU & NỘP BÀI</b> (Ngày 7)<br>• Toàn đội: Tinh chỉnh & submission.csv"]

    P1 --> P2 --> P3 --> P4

---
