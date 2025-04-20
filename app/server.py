# server.py
from flask import Flask, request, send_file, render_template_string, render_template
import json
from io import BytesIO
from datetime import datetime

app = Flask(__name__)
@app.route('/', methods=['GET'])
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Получаем данные формы
        data = {
            "type": request.form.get('type'),
            "dns": request.form.get('dns'),
            "usercp": request.form.get('usercp'),
            "auht": request.form.get('auht'),
            "ids": request.form.get('ids'),
            "provider": request.form.get('provider'),
            "SSL": request.form.get('SSL'),
            "hwid": request.form.get('hwid'),
            "inn": request.form.get('inn'),
            "email": request.form.get('email'),
            "timestamp": datetime.now().isoformat()
        }
        inn = request.form.get('inn')
        
        # Создаем JSON в памяти
        json_data = json.dumps(data, ensure_ascii=False, indent=2)
        buffer = BytesIO()
        buffer.write(json_data.encode('utf-8'))
        buffer.seek(0)

        # Формируем имя файла
        filename = f"{inn}_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"

        # Отправляем файл как ответ
        return send_file(
            buffer,
            mimetype='application/json',
            as_attachment=True,
            download_name=filename
        )

    except Exception as e:
        return str(e), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)