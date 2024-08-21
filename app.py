from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from model.model import train_model, predict
import io
from io import BytesIO
import base64
import matplotlib.pyplot as plt

app = Flask(__name__)
data = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    global data
    if request.method == 'POST':
        file = request.files['file']
        
        # Đọc file Excel
        data = pd.read_excel(file)
        
        # Sau khi lưu dữ liệu, chuyển hướng tới dashboard
        return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    global data
    if data is None:
        return "No data available", 400
    
    plt.figure(figsize=(10, 6))
    
    # Thay thế bằng các cột thực tế trong dữ liệu
    if 'P1' in data.columns and 'SL(KWH)' in data.columns:
        plt.plot(data['P1'], data['SL(KWH)'], label='P1 vs SL(KWH)')

    # Nếu có thêm cột dữ liệu khác, thêm các biểu đồ tương tự
    if 'P2' in data.columns and 'SL(KWH)' in data.columns:
        plt.plot(data['P2'], data['SL(KWH)'], label='P2 vs SL(KWH)')

    plt.title('Data Analysis Dashboard')
    plt.xlabel('Features')
    plt.ylabel('Target')
    plt.legend()
    
    # Lưu biểu đồ vào bộ nhớ và chuyển đổi thành chuỗi base64
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    
    return render_template('dashboard.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True) 

app.py