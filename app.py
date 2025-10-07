from flask import Flask, render_template, request
import pandas as pd
import joblib
import io
import base64
import matplotlib.pyplot as plt

app = Flask(__name__)

# Load model regresi linear
model = joblib.load("model_penjualan_kopi.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    hasil_prediksi = None
    gambar = None
    uploaded_data = None

    if request.method == "POST":
        if "file" in request.files:
            file = request.files["file"]
            if file.filename != "":
                df = pd.read_csv(file)
                uploaded_data = df.head().to_html(classes="table table-striped", index=False)

                # Prediksi berdasarkan kolom hour_of_day
                if "hour_of_day" in df.columns:
                    X = df[["hour_of_day"]]
                    df["Prediksi Penjualan (money)"] = model.predict(X)

                    hasil_prediksi = df[["hour_of_day", "Prediksi Penjualan (money)"]].head().to_html(classes="table table-bordered", index=False)

                    # Plot hasil prediksi
                    plt.figure(figsize=(6,4))
                    plt.scatter(df["hour_of_day"], df["money"], label="Data Aktual", color="blue", alpha=0.6)
                    plt.plot(df["hour_of_day"], df["Prediksi Penjualan (money)"], color="red", label="Prediksi", linewidth=2)
                    plt.xlabel("Jam Pembelian")
                    plt.ylabel("Jumlah Uang Penjualan")
                    plt.title("Prediksi Penjualan Kopi berdasarkan Jam")
                    plt.legend()
                    
                    img = io.BytesIO()
                    plt.savefig(img, format='png', bbox_inches='tight')
                    img.seek(0)
                    gambar = base64.b64encode(img.getvalue()).decode()
                    plt.close()

    return render_template("index.html", hasil_prediksi=hasil_prediksi, gambar=gambar, uploaded_data=uploaded_data)

if __name__ == "__main__":
    app.run(debug=True)
