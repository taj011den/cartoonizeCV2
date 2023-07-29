import cv2
import numpy as np
import os

def cartoonize_video(video_path, output_path):
    # تحميل الفيديو
    cap = cv2.VideoCapture(video_path)
    
    # التحقق مما إذا تم فتح ملف الفيديو بنجاح
    if not cap.isOpened():
        print(f"حدث خطأ في فتح ملف الفيديو {video_path}")
        return
    
    # الحصول على معلومات الفيديو
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # إنشاء كائن VideoWriter لحفظ الفيديو الناتج
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    # loop عبر إطارات الفيديو
    while cap.isOpened():
        # قراءة إطار من الفيديو
        ret, frame = cap.read()
        
        # إذا لم يتم قراءة الإطار بنجاح، انقطاع الدورة
        if not ret:
            break
        
        # تحويل الإطار إلى صورة تشبه الرسوم المتحركة
        cartoon = cv2.stylization(frame, sigma_s=150, sigma_r=0.25)
        
        # كتابة إطار الرسوم المتحركة إلى الفيديو الناتج
        out.write(cartoon)
        
        # عرض إطار الرسوم المتحركة
        cv2.imshow('Cartoon', cartoon)
        
        # الخروج إذا تم الضغط على زر 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # إطلاق كائنات VideoCapture و VideoWriter وإغلاق جميع النوافذ
    cap.release()
    out.release()
    cv2.destroyAllWindows()

# مسار ملف الفيديو الأصلي
video_path = "D:/cartoonize/1.mp4"

# مسار الفيديو المحول إلى كارتونز
output_dir = "D:/cartoonize/out/"

# انشاء مجلد الخرج في حال لم يكن موجود
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# إخراح الفيديو الى المسار المحدد و تميته ب  the cartoonized video
output_path = os.path.join(output_dir, "cartoonized_video.mp4")

# استدعاء الدالة لتحويل الفيديو إلى كارتونز
cartoonize_video(video_path, output_path)
