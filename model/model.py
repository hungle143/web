from sklearn.ensemble import RandomForestRegressor
import pandas as pd

# Tạo và huấn luyện mô hình
def train_model(data):
    
    X = data.iloc[:, 2:]
    y = data['SL(KWH)']  # Thay thế bằng cột mục tiêu thực tế
    
    # Khởi tạo mô hình RandomForestRegressor
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    
    # Huấn luyện mô hình
    model.fit(X, y)
    
    return model

# Dự đoán
def predict(model, input_data):
    return model.predict(input_data)
