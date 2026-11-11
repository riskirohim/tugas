
from flask import Flask, render_template_string
import psutil

app = Flask(__name__)

@app.route('/')
def home():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    
    html = f"""
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Server Monitoring Dashboard</title>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; margin-top: 50px; background: #0f172a; color: white; }}
            .card {{ background: #1e293b; display: inline-block; padding: 25px; border-radius: 12px; margin: 15px; width: 220px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }}
            h1 {{ color: #38bdf8; font-size: 28px; }}
            .val {{ font-size: 36px; font-weight: bold; color: #4ade80; margin-top: 10px; }}
            .footer {{ margin-top: 40px; color: #94a3b8; font-size: 14px; }}
        </style>
    </head>
    <body>
        <h1>🖥️ Live Server Monitoring Dashboard</h1>
        <p>Deployment berbasis Docker di Cloud Platform (Render)</p>
        
        <div class="card">
            <h2>CPU Usage</h2>
            <div class="val">{cpu}%</div>
        </div>
        <div class="card">
            <h2>RAM Usage</h2>
            <div class="val">{ram}%</div>
        </div>

        <div class="footer">
            <p>Dikembangkan oleh Rizqy Rohimulhudda | Cloud Computing Portfolio</p>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
