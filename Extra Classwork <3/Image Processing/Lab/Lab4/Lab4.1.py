import cv2
import numpy as np
import matplotlib.pyplot as plt
from keras import Model, Input
from keras.layers import Dense, Conv2D, MaxPool2D, UpSampling2D
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
import glob
from tqdm import tqdm
import warnings
# warnings.filterwarnings('ignore')

# Set GPU
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# Suppress warnings
warnings.filterwarnings('ignore')

# 1. อ่านไฟล์ภาพทั้งหมดเก็บในรูป array (จำนวนภาพไม่น้อยกว่า 100 ภาพ)

image_files = glob.glob("./Lab4/face_mini/*/*.jpg")  # แทน path_to_images ด้วยที่ตั้งของไฟล์ภาพ
imgs = []

# 3. Append images to an array
for fname in tqdm(image_files):
    img = cv2.imread(fname)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # แปลงสีจาก BGR เป็น RGB
    img = cv2.resize(img, (100, 100))  # Resize ภาพเป็น (100, 100)
    img = np.array(img)
    imgs.append(img)

# 2. Normalized ภาพ (เพื่อให้ค่า pixel intensity = [0, 1])

imgs = np.array(imgs) / 255.0



# 4. แบ่งชุดข้อมูลเป็น Training_data, Testing_data (70 : 30)

random_state = 42  # กำหนด random state ตามที่คุณต้องการ
train_x, test_x = train_test_split(imgs, random_state=random_state, test_size=0.3)

# 5. แบ่งชุดข้อมูล Training_data เป็น Training_data, Validation_data (80:20)

train_x, val_x = train_test_split(train_x, random_state=random_state, test_size=0.2)

# 6. กำหนด noise parameters

noise_mean = 0
noise_std = 0.5  # ปรับค่าตามที่คุณต้องการ
noise_factor = 0.6  # ปรับค่าตามที่คุณต้องการ

# 7. สร้าง noise และเพิ่มเข้าในภาพ train_x, val_x, test_x

train_x_noise = train_x + (noise_factor * np.random.normal(loc=noise_mean, scale=noise_std, size=train_x.shape))
val_x_noise = val_x + (noise_factor * np.random.normal(loc=noise_mean, scale=noise_std, size=val_x.shape))
test_x_noise = test_x + (noise_factor * np.random.normal(loc=noise_mean, scale=noise_std, size=test_x.shape))

# 8. แสดงภาพเปรียบเทียบ ภาพที่เพิ่ม noise และภาพต้นฉบับ

plt.figure(figsize=(50, 50))

# # แสดงภาพต้นฉบับ
# plt.subplot(1, 2, 1)
# plt.title("Original Image")
# plt.imshow(train_x[0])  # เลือกภาพต้นฉบับจากชุด Training_data
# plt.axis('off')

# # แสดงภาพที่เพิ่ม noise
# plt.subplot(1, 2, 2)
# plt.title("Noisy Image")
# plt.imshow(train_x_noise[0])  # เลือกภาพที่มีเสียงจากชุด Training_data
# plt.axis('off')
# plt.show()

n = 10
for i in range(n):
    # Display original images
    ax = plt.subplot(3, n, i + 1)
    plt.imshow(train_x[i])
    plt.title("Original")
    plt.axis('off')

    # Display noisy images
    ax = plt.subplot(3, n, i + 1 + n)
    plt.imshow(train_x_noise[i])
    plt.title("Noisy")
    plt.axis('off')

plt.show()

