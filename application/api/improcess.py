from flask import Flask,Blueprint,Response,jsonify
import cv2
import time

apiImprocess = Blueprint('apiImprocess',__name__,url_prefix='/api/improcess')
terminate = True
def generate_frames():
    cap = cv2.VideoCapture(0) 
    while not terminate:
        ret, frame = cap.read() 
        if not ret:
            print("Error: Failed to capture image from camera")
            break

    
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        
        time.sleep(3)

    
    cap.release()


@apiImprocess.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@apiImprocess.route('/stop')
def stop():
    global terminate
    terminate = True
    return jsonify({"success":True,"message":"stopped"})

@apiImprocess.route('/start')
def start():
    global terminate
    if terminate == True:
     terminate= False
     
     return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

    else:
        return jsonify({"success":True,"message":"already working"})

