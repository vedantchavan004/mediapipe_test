import cv2
import mediapipe as mp
import os

# Input & Output paths
input_video_path = "vid.mp4"
output_video_path = "violin_elbow_arm_feedback_output.mp4"

# Initialize MediaPipe Pose
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(model_complexity=1, min_detection_confidence=0.5)

# Open input video
cap = cv2.VideoCapture(input_video_path)
if not cap.isOpened():
    raise Exception("Could not open video")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) or 640
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) or 480
fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0.0:
    fps = 25

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)

    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark
        h, w, _ = frame.shape

        # Right arm keypoints
        r_shoulder = landmarks[12]
        r_elbow = landmarks[14]
        r_wrist = landmarks[16]


        sx, sy = int(r_shoulder.x * w), int(r_shoulder.y * h)
        ex, ey = int(r_elbow.x * w), int(r_elbow.y * h)
        wx, wy = int(r_wrist.x * w), int(r_wrist.y * h)

        # Condition: elbow above shoulder
        elbow_above_shoulder = ey < sy
        color = (0, 0, 255) if elbow_above_shoulder else (0, 255, 0)

        # Draw pose
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Draw colored arm
        cv2.line(frame, (sx, sy), (ex, ey), color, 4)
        cv2.line(frame, (ex, ey), (wx, wy), color, 4)
        cv2.circle(frame, (ex, ey), 10, color, -1)

        # Optional feedback text
        if elbow_above_shoulder:
            cv2.putText(frame, "Elbow too high!", (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

    out.write(frame)

# Finalize
cap.release()
out.release()
pose.close()

if os.path.exists(output_video_path):
    print("Saved:", output_video_path)
else:
    print("Video not saved")
