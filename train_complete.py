import os
import sys

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

from pathlib import Path
home_dir = Path('./ultralytics_settings')
home_dir.mkdir(exist_ok=True)
os.environ['YOLO_CONFIG_DIR'] = str(home_dir.absolute())

from ultralytics import YOLO

def train_model():
    model = YOLO('yolov8n.pt')
    
    results = model.train(
        data='data.yaml',
        epochs=30,
        imgsz=640,
        batch=16,
        name='traffic_signs_complete',
        project='runs/detect',
        patience=10,
        save=True,
        device='cpu',
        workers=0,
        verbose=True,
        plots=True
    )
    
    print("Training completed!")
    print(f"Best model saved at: runs/detect/traffic_signs_complete/weights/best.pt")
    
    return results

if __name__ == '__main__':
    train_model()