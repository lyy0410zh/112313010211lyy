import pandas as pd

# 查看提交文件
print("=== 提交文件 submission.csv ===")
df_sub = pd.read_csv('submission.csv')
print(f"总行数: {len(df_sub)}")
print("前10行:")
print(df_sub.head(10))
print()

# 查看训练结果
print("=== 训练结果 ===")
df_train = pd.read_csv('runs/detect/traffic_signs3/results.csv')
print("最后5个epoch的结果:")
print(df_train.tail(5))
print()

# 显示最佳结果
best_epoch = df_train['metrics/mAP50(B)'].idxmax()
print(f"最佳mAP50出现在第 {best_epoch} 个epoch")
print(f"最佳mAP50: {df_train.loc[best_epoch, 'metrics/mAP50(B)']:.4f}")
print(f"最佳mAP50-95: {df_train.loc[best_epoch, 'metrics/mAP50-95(B)']:.4f}")