# 🔥 Fire Detection and Localization System  

A **real-time AI-powered system** for detecting and localizing fire using a single monocular camera feed, mapping it onto a **2D floor plan** for safety-critical monitoring. The system combines **deep learning**, **monocular depth estimation**, and **camera-to-world coordinate projection** to deliver accurate, real-world fire positions without stereo vision.  

---

## 🚀 Features  
- **High-Accuracy Fire Detection** – Uses **YOLOv11** achieving **96% mAP** to detect fire in real time.  
- **3D Spatial Understanding from Monocular Vision** – Integrates **Depth Anything v2** to estimate fire distance using reference-object calibration.  
- **2D Floor Map Localization** – Projects detected fire coordinates from the camera’s perspective into global floor plan coordinates using known camera parameters.  
- **Production-Ready** – Optimized for **real-time performance** in CCTV-based safety monitoring setups.  

---

## 🛠️ Tech Stack  
- **Frameworks:** PyTorch, OpenCV, Flask (optional for API deployment)  
- **Models:** YOLOv11 (object detection), Depth Anything v2 (monocular depth estimation)  
- **Other Tools:** NumPy, Matplotlib  
- **Hardware:** Standard CCTV or monocular camera (no stereo vision required)  

---

## 📂 Project Structure  
```plaintext
Fire-Localizer/
│
├── models/                # Pre-trained YOLOv11 and Depth Anything v2 weights
├── src/
│   ├── detection.py        # YOLOv11 inference
│   ├── depth_estimation.py # Monocular depth estimation
│   ├── localization.py     # Coordinate projection to global map
│   ├── utils.py            # Helper functions (calibration, geometry)
│
├── floor_map/              # Floor plan image + camera position data
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
└── main.py                 # Entry point for fire detection + localization
```

---

## 📏 How It Works  
1. **Fire Detection**  
   - Frame is captured from CCTV feed.  
   - YOLOv11 detects fire and extracts **bottom-center pixel coordinates** of bounding box.  

2. **Depth Estimation**  
   - Depth Anything v2 estimates depth map from monocular frame.  
   - Reference objects (with known real-world height) calibrate depth measurements.  

3. **Localization on Floor Plan**  
   - Camera’s **position, orientation, and field of view** are used to transform image-space coordinates into global coordinates.  
   - Fire location is plotted on a 2D floor plan in real time.  

---

## 🖥️ Installation & Usage  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/yourusername/Fire-Geolocator.git
cd Fire-Geolocator
```

### 2️⃣ Install dependencies  
```bash
pip install -r requirements.txt
```

### 3️⃣ Download model weights  
- **YOLOv11** → [Link to weights](https://github.com/ultralytics)  
- **Depth Anything v2** → [Link to weights](https://github.com/isl-org/Depth-Anything)  

### 4️⃣ Run the system  
```bash
python main.py --camera_id 0 --floor_map floor_map/map.png
```

---

## 📊 Performance  
| Metric              | YOLOv11 Fire Detection | Depth Estimation Accuracy | FPS |
|---------------------|------------------------|---------------------------|-----|
| **mAP@50**          | 96%                    | ±0.2m average error       | 30  |

---

## 🌍 Applications  
- **Airport Fire Monitoring**  
- **Industrial Safety Systems**  
- **Smart Building Surveillance**  
- **Railway/Metro Safety**  

---

## 🏆 Achievements  
- Real-time performance at **30 FPS** with high accuracy.  
- Designed for environments with **non-overlapping cameras** where stereo vision is not feasible.  
- Flexible to integrate with **existing CCTV infrastructure**.  

---

## 📜 License  
MIT License — free to use, modify, and distribute.  

---

## 👨‍💻 Author  
**Siddharth Khatod**  
- [LinkedIn](https://linkedin.com/in/sidkhatod)  
- [GitHub](https://github.com/sidkhatod)  
