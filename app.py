from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def student_results():

    students = [

        {"name": "Ali", "score": 95},
        {"name": "Vali", "score": 72},
        {"name": "Hasan", "score": 60},
        {"name": "Husan", "score": 48},
        {"name": "Sardor", "score": 85},
        {"name": "Aziz", "score": 91}

    ]

    results = []

    for s in students:

        if s["score"] >= 90:
            grade = "A"

        elif s["score"] >= 70:
            grade = "B"

        elif s["score"] >= 50:
            grade = "C"

        else:
            grade = "F"

        results.append({

            "name": s["name"],

            "score": s["score"],

            "grade": grade

        })

    highest = max(results, key=lambda x: x["score"])
    lowest = min(results, key=lambda x: x["score"])

    return render_template(
        "index.html",
        results=results,
        highest=highest,
        lowest=lowest
    )


if __name__ == "__main__":
    app.run(debug=True)
