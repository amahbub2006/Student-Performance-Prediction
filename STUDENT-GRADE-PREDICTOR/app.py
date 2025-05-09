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
        result = "Success Likely ✅" if prediction == 1 else "Success UNLIKELY ❌"

        # Realism message
        if jump <= 2:
            realism = "✅ Your goal is realistic and achievable."
        elif jump <= 8:
            realism = "⚠️ Ambitious goal. Difficult, but not impossible."
        elif jump <= 15:
            realism = "❌ That's a big stretch. Most don't achieve this."
        else:
            realism = "🚫 That goal is too unrealistic based on past students."

        # Comparison stats
        df = pd.read_csv("artifacts/data_transformation/transformed.csv")
        filtered = df[df["desired_grade"] == desired]
        if not filtered.empty:
            total = len(filtered)
            success_count = filtered["success"].sum()
            rate = round((success_count / total) * 100, 1)
            comparison = f"🔎 {total} students who aimed for {desired}, {rate}% succeeded."
        else:
            comparison = "Nobody else tried to get this grade. 🧭"

        return render_template("results.html", 
                               result=result, realism=realism, comparison=comparison)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)  # trigger
