import torch
import torch.nn as nn

# Giả sử mô hình phân loại 3 lớp: [Chó, Mèo, Ngựa]
# Batch = 2 ảnh. Output trả về điểm thô (Logits), CHƯA qua Softmax
outputs = torch.tensor([[2.5, 0.1, 0.3],   # Ảnh 1: Điểm lớp Chó (index 0) cao nhất
                        [0.1, 0.2, 3.8]])  # Ảnh 2: Điểm lớp Ngựa (index 2) cao nhất

# Đáp án thực tế (Label dạng index số nguyên, không cần one-hot)
targets = torch.tensor([0, 2]) # Ảnh 1 là Chó (0), Ảnh 2 là Ngựa (2)

# --- KHỞI TẠO (Nhiệm vụ Ngày 2) ---
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# --- LUỒNG TÍNH TOÁN ---
# 1. Tính Loss
loss = criterion(outputs, targets)
print(f"Loss value: {loss.item():.4f}")

# 2. Cập nhật trọng số (Backpropagation)
optimizer.zero_grad() # Clear gradient cũ
loss.backward()        # Tính gradient mới
optimizer.step()        # Adam cập nhật weights
