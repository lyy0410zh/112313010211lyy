# 交通标志检测 - AI Studio 运行指南

## 文件说明

- `traffic_signs_yolov8.ipynb` - 主 notebook 文件，包含完整的训练和预测流程
- `data/` - 数据目录（需要在AI Studio上传）
  - `train/images/` - 训练集图片
  - `train/labels/` - 训练集标注
  - `val/images/` - 验证集图片
  - `val/labels/` - 验证集标注
  - `test/images/` - 测试集图片

## AI Studio 上传步骤

### 1. 创建项目
1. 登录 [百度AI Studio](https://aistudio.baidu.com/)
2. 点击"创建项目"
3. 选择"Notebook"类型
4. 上传 `traffic_signs_yolov8.ipynb` 文件

### 2. 上传数据
1. 进入项目后，点击左侧"数据集"
2. 上传包含以下结构的压缩包：
```
data/
├── train/
│   ├── images/
│   └── labels/
├── val/
│   ├── images/
│   └── labels/
└── test/
    └── images/
```

### 3. 运行Notebook
1. 启动环境（建议选择GPU环境）
2. 按顺序运行所有代码单元格
3. 等待训练完成
4. 下载生成的 `submission.csv` 文件

## 训练参数

- 模型：YOLOv8n
- 训练轮数：50 epochs
- 图像尺寸：640x640
- Batch size：16
- 优化器：AdamW
- 学习率：0.01

## 类别说明

| 类别ID | 类别名称 |
|--------|----------|
| 0 | Green Light |
| 1 | Red Light |
| 2 | Speed Limit 10 |
| 3 | Speed Limit 100 |
| 4 | Speed Limit 110 |
| 5 | Speed Limit 120 |
| 6 | Speed Limit 20 |
| 7 | Speed Limit 30 |
| 8 | Speed Limit 40 |
| 9 | Speed Limit 50 |
| 10 | Speed Limit 60 |
| 11 | Speed Limit 70 |
| 12 | Speed Limit 80 |
| 13 | Speed Limit 90 |
| 14 | Stop |

## 注意事项

1. 确保数据路径正确设置为 `data/`
2. GPU环境训练速度更快
3. 训练过程大约需要 30-60 分钟（取决于硬件）
4. 生成的 `submission.csv` 可直接提交到比赛平台
