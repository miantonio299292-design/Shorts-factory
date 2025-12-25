from flask import Flask, request
import threading
from scripts.main_worker import generate_batch

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>🎥 Shorts Factory</h2>
    <form action="/generate">
      Quantidade de vídeos:
      <input name="qty" type="number" value="10"/>
      <button type="submit">GERAR</button>
    </form>
    """

@app.route("/generate")
def generate():
    qty = int(request.args.get("qty", 10))
    thread = threading.Thread(target=generate_batch, args=(qty,))
    thread.start()
    return f"🚀 Geração iniciada: {qty} vídeos"

app.run(host="0.0.0.0", port=10000)
