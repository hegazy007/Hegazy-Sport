from flask import Flask, render_template_string, request, redirect
from supabase import create_client, Client

# بيانات Supabase
url = "https://zowvqggksqwqqrahkcng.supabase.co"
key = "حط المفتاح العام هنا"
supabase: Client = create_client(url, key)

app = Flask(__name__)

# HTML بسيط داخل الكود
HTML = """
<!doctype html>
<title>Hegazy Sport - المهام</title>
<h1>📋 قائمة المهام</h1>

<form action="/add" method="post">
    <input name="task" placeholder="أضف مهمة جديدة" required>
    <button type="submit">➕ إضافة</button>
</form>

<ul>
    {% for todo in todos %}
        <li>
            {{ todo['task'] }}
            {% if not todo['is_complete'] %}
                <a href="/complete/{{ todo['id'] }}">✅ تم</a>
            {% else %}
                <span style="color: green;">✔️ مكتملة</span>
            {% endif %}
        </li>
    {% endfor %}
</ul>
"""

@app.route("/")
def index():
    result = supabase.table("todos").select("*").order("created_at", desc=True).execute()
    return render_template_string(HTML, todos=result.data)

@app.route("/add", methods=["POST"])
def add():
    task_text = request.form["task"]
    supabase.table("todos").insert({"task": task_text, "is_complete": False}).execute()
    return redirect("/")

@app.route("/complete/<int:task_id>")
def complete(task_id):
    supabase.table("todos").update({"is_complete": True}).eq("id", task_id).execute()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
