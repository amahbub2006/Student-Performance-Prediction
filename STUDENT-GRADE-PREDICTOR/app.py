from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load("artifacts/model_trainer/model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Raw user input (human scale)
        current_raw = int(request.form["current_grade"])
        desired_raw = int(request.form["desired_grade"])
        studytime_raw = int(request.form["studytime"])
        failures = int(request.form["failures"])
        absences = int(request.form["absences"])

        # Convert to model input scale
        current = round(current_raw * 20 / 100)
        desired = round(desired_raw * 20 / 100)
        studytime = min(4, max(1, round(studytime_raw / 10)))
        jump = desired - current

        # Format for model
        data = pd.DataFrame([{
            "current_grade": current,
            "desired_grade": desired,
            "studytime": studytime,
            "failures": failures,
            "absences": absences
        }])

        # Predict with threshold
        prob = model.predict_proba(data)[0][1]
        prediction = 1 if prob >= 0.35 else 0
        result = "LIKELY to succeed ✅" if prediction == 1 else "UNLIKELY to succeed ❌"

        # Realism message
        if jump <= 2:
            realism = "✅ Your goal is realistic and achievable."
        elif jump <= 8:
            realism = "⚠️ Ambitious goal. It might be difficult, but not impossible."
        elif jump <= 15:
            realism = "❌ That's a big stretch. Most students can't jump that far."
        else:
            realism = "🚫 That goal is extremely unrealistic based on past students."

        # Comparison stats
        df = pd.read_csv("artifacts/data_transformation/transformed.csv")
        filtered = df[df["desired_grade"] == desired]
        if not filtered.empty:
            total = len(filtered)
            success_count = filtered["success"].sum()
            rate = round((success_count / total) * 100, 1)
            comparison = f"🔎 Out of {total} past students who aimed for grade {desired}, {rate}% succeeded."
        else:
            comparison = "No past student aimed for this grade. You're blazing a new trail 🧭"

        return render_template("results.html", result=result, realism=realism, comparison=comparison)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)# trigger
