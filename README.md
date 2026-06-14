# AI Attendance System Using Face Recognition

## 📌 Overview

The AI Attendance System is a computer vision-based application that automatically records attendance using real-time face recognition. The system detects and recognizes registered faces through a webcam and logs attendance with timestamps into a CSV file.

This project demonstrates the practical application of Artificial Intelligence, Machine Learning, and Computer Vision for automating attendance management.

---

## 🚀 Features

* Real-time face detection and recognition
* Automatic attendance marking
* Attendance stored in CSV format
* Prevents duplicate attendance entries
* Fast and efficient processing
* Easy to use and customize

---

## 🛠️ Technologies Used

* Python
* OpenCV
* Face Recognition Library
* NumPy
* Pandas
* Datetime

---

## 📂 Project Structure

```text
AI-Attendance-System/
│
├── Attendance.csv
├── ImagesAttendance/
│   ├── Person1.jpg
│   ├── Person2.jpg
│   └── ...
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Attendance-System.git
cd AI-Attendance-System
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

1. Add images of authorized users to the `ImagesAttendance` folder.
2. Run the application:

```bash
python main.py
```

3. The webcam will start automatically.
4. When a known face is detected:

   * The person's name is displayed.
   * Attendance is recorded in `Attendance.csv`.
   * The date and time are stored automatically.

---

## 📸 How It Works

1. Load images of registered individuals.
2. Generate facial encodings.
3. Capture live video from the webcam.
4. Detect and recognize faces in each frame.
5. Match detected faces with stored encodings.
6. Mark attendance with a timestamp.

---

## 📈 Future Improvements

* Database integration (MySQL/PostgreSQL)
* Web-based dashboard
* Email notifications
* Attendance analytics and reports
* Multi-camera support
* Cloud deployment

---

## 🤝 Contributing

Contributions are welcome. Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Sujon**

If you found this project useful, please consider giving it a ⭐ on GitHub.
