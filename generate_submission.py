import os
import csv
from pathlib import Path

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
os.environ['YOLO_CONFIG_DIR'] = './ultralytics_settings'

from ultralytics import YOLO

model = YOLO('runs/detect/traffic_signs_complete/weights/best.pt')
image_paths = sorted([p for p in Path('test/images').iterdir() if p.is_file()])

print(f"测试集图片数量: {len(image_paths)}")

with open('submission.csv', 'w', encoding='utf-8', newline='') as handle:
    writer = csv.DictWriter(
        handle,
        fieldnames=['image_id', 'class_id', 'x_center', 'y_center', 'width', 'height', 'confidence'],
    )
    writer.writeheader()
    
    results = model.predict(
        source=[str(p) for p in image_paths],
        conf=0.001,
        save=False,
        verbose=True
    )
    
    for result in results:
        image_id = Path(result.path).name
        if result.boxes is None:
            continue
        for box in result.boxes:
            x_center, y_center, width, height = box.xywhn[0].tolist()
            writer.writerow(
                {
                    'image_id': image_id,
                    'class_id': int(box.cls[0].item()),
                    'x_center': x_center,
                    'y_center': y_center,
                    'width': width,
                    'height': height,
                    'confidence': float(box.conf[0].item()),
                }
            )

print(f"\n提交文件已生成: submission.csv")