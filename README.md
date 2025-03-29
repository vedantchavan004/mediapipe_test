# Posture Feedback System using MediaPipe Pose

This project provides **real-time visual posture feedback** from a video. It analyzes the **right arm posture** using MediaPipe Pose and highlights the **elbow** and **arm color** based on posture.

If the **right elbow is raised above the shoulder**, it is marked **red** and a warning is displayed. Otherwise, it’s marked **green**, indicating correct posture.

---

## 📽️ Demo Videos
Testing videos were taken from: https://www.pexels.com/

| Result |

![Violin Posture Demo](media/violin_feedback.gif)     ![Yoga Posture Demo](media/yoga_feedback.gif) 

---

## ✅ Features

- Tracks the **right shoulder, elbow, and wrist**.
- Draws real-time pose connections using MediaPipe.
- Highlights **arm red** if elbow is above shoulder (incorrect).
- Displays `"Elbow too high!"` warning on screen.
- Saves the **annotated video** for review and evaluation.

---

## 🔧 Requirements

Install dependencies using pip:

```bash
pip install mediapipe opencv-python
```

---

## 🚀 How to Use

1. Replace `vid.mp4` with your violin video file.
2. Run the script:
    ```bash
    python violin_posture_feedback.py
    ```
3. The output video will be saved as:
    ```
    violin_elbow_arm_feedback_output.mp4
    ```

---

## 🧠 How It Works

- Uses **MediaPipe Pose** to detect full-body landmarks (33 keypoints).
- Extracts keypoints:
  - Right shoulder: `landmarks[12]`
  - Right elbow: `landmarks[14]`
  - Right wrist: `landmarks[16]`
- Checks if:
    ```python
    elbow_y < shoulder_y
    ```
- If true → **elbow is too high** → highlight in red.
- Otherwise → draw green arm path.

---

## 📁 Output Example

- Green = Good posture  
- Red = Incorrect elbow height  
- Feedback = `Elbow too high!` displayed in red

---

## 🛠 File Structure

```bash
├── mediapipe_test.py        # Main Python script
├── vid.mp4                           # Input video file (replaceable)
├── violin_elbow_arm_feedback_output.mp4  # Output result video
```

---

