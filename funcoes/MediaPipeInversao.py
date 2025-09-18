import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose


def MediaPipeInversao(frame):
    IMAGE_FILES = [frame]
    BG_COLOR = (192, 192, 192)  # gray
    with mp_pose.Pose(
            static_image_mode=True,
            model_complexity=2,
            enable_segmentation=True,
            min_detection_confidence=0.5) as pose:
        for idx, file in enumerate(IMAGE_FILES):
            image = cv2.imread(file)
            image_height, image_width, _ = image.shape
            # Convert the BGR image to RGB before processing.
            results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

            if not results.pose_landmarks:
                continue
            print(
                f'Nose coordinates: ('
                f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image_width}, '
                f'{results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * image_height})'
            )

            if(results.pose_landmarks):
                h , w, _  = image.shape
                feet = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_FOOT_INDEX]
                feetX = int(feet.x * w)
                feetY = int(feet.y * h)
                #cv2.circle(image, (feetX, feetY), radius=10, color=(0,0,255), thickness=-1)

                head = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE]
                headX = int(head.x * w)
                headY = int(head.y * h)
                #cv2.circle(image, (headX, headY), radius=10, color=(0,0,255), thickness=-1)

                feet2 = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX]
                feetX2 = int(feet2.x * w)
                feetY2 = int(feet2.y * h)

                if(feetY < headX):
                    cv2.rectangle(image, (feetX,feetY2),(headX,headY), color=(0,0,255), thickness=3)
                    cv2.putText(image,"INVERTIDO",((20),(60)),3,2, color=(0,0,255),thickness=2)

                    annotated_image = image.copy()
                    # Draw segmentation on the image.
                    # To improve segmentation around boundaries, consider applying a joint
                    # bilateral filter to "results.segmentation_mask" with "image".
                    condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
                    bg_image = np.zeros(image.shape, dtype=np.uint8)
                    bg_image[:] = BG_COLOR
                    annotated_image = np.where(condition, annotated_image, bg_image)
                    # Draw pose landmarks on the image.
                    mp_drawing.draw_landmarks(
                        annotated_image,
                        results.pose_landmarks,
                        mp_pose.POSE_CONNECTIONS,
                        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
                    cv2.imshow('MediaPipe Pose', image)
                    cv2.imwrite('Teste3.png', image)

                    cv2.waitKey(0)
