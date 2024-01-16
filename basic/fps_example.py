import cv2
import datetime
import imutils

def main():
    # Betölt egy videót
    cap = cv2.VideoCapture("test_video.mp4")  # link: https://www.pexels.com/video/people-in-a-park-3105196/

    # FPS számolás kezdeti időpontja
    fps_start_time = datetime.datetime.now()
    fps = 0
    total_frames = 0

    while True:
        # Képkocka beolvasása a videóból
        ret, frame = cap.read()
        
        # Képkocka méretének átméretezése (800x1600 pixel)
        frame = imutils.resize(frame, width=800, height=1600)

        # Összes képkocka számolása
        total_frames += 1

        # FPS számolás
        fps_end_time = datetime.datetime.now()
        time_diff = fps_end_time - fps_start_time
        if time_diff.seconds == 0:
            fps = 0.0
        else:
            fps = (total_frames / time_diff.seconds)

        # FPS szöveg formázása
        fps_text = "FPS: {:.2f}".format(fps)

        # Háttérzet rajzolása
        cv2.rectangle(frame, (5, 10), (130, 35), (0, 0, 0), -1)

        # Szöveg rajzolása a háttérzeten
        cv2.putText(frame, fps_text, (5, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)

        # Képkocka megjelenítése ablakban
        cv2.imshow("ablakCim", frame)

        # Ablak bezárására várakozás, és kilépés a 'q' billentyű lenyomásával
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    # Ablakok bezárása
    cv2.destroyAllWindows()

# Főprogram indítása
main()
