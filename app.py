from flask import Flask, render_template, request, jsonify, session, send_from_directory
import sqlite3
import json
import os
from database import init_db, get_db_connection
from levels import LEVELS, validate_level_query
from mystery import check_solution, get_mystery_hint

app = Flask(__name__)
app.secret_key = 'sql_detective_noir_2024_secret'

# Initialize in-memory DB on startup
_db_connection = None

def get_db():
    global _db_connection
    if _db_connection is None:
        _db_connection = init_db()
    return _db_connection

@app.route('/')
def home():
    session.clear()
    return render_template('home.html')

@app.route("/google3e389395828ed8b7.html")
def google_verification():
    return send_from_directory("static", "google3e389395828ed8b7.html")

@app.route("/test")
def test():
    return "Working"
    
@app.route('/start')
def start_game():
    session['score'] = 0
    session['current_level'] = 0
    session['hints_used'] = {}
    session['levels_completed'] = []
    return render_template('levels.html', 
                           level=LEVELS[0], 
                           level_num=0, 
                           total_levels=len(LEVELS),
                           score=0)

@app.route('/level/<int:level_num>')
def load_level(level_num):
    if level_num >= len(LEVELS):
        return render_template('mystery.html', score=session.get('score', 0))
    
    if 'score' not in session:
        session['score'] = 0
        session['hints_used'] = {}
        session['levels_completed'] = []

    return render_template('levels.html',
                           level=LEVELS[level_num],
                           level_num=level_num,
                           total_levels=len(LEVELS),
                           score=session.get('score', 0),
                           completed=session.get('levels_completed', []))

@app.route('/mystery')
def mystery():
    if 'score' not in session:
        session['score'] = 0
    return render_template('mystery.html', score=session.get('score', 0))

@app.route('/api/run_query', methods=['POST'])
def run_query():
    data = request.get_json()
    query = data.get('query', '').strip()
    
    if not query:
        return jsonify({'error': 'No query provided'}), 400

    # Block dangerous operations
    forbidden = ['drop ', 'delete ', 'update ', 'alter ', 'create ', 'attach ', 'detach']
    q_lower = query.lower()
    for word in forbidden:
        if word in q_lower and 'insert into solution' not in q_lower:
            return jsonify({'error': f'Operation not allowed in detective mode: {word.strip().upper()}'}), 400

    try:
        conn = get_db()
        cursor = conn.cursor()
        
        # Handle INSERT INTO solution specially
        if 'insert into solution' in q_lower:
            cursor.execute(query)
            conn.commit()
            cursor.execute("SELECT value FROM solution WHERE user = 1")
            row = cursor.fetchone()
            if row:
                result = check_solution(row[0])
                return jsonify({'solution_check': True, 'correct': result['correct'], 'message': result['message']})
            return jsonify({'error': 'Solution insert failed'}), 400

        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description] if cursor.description else []
        
        return jsonify({
            'columns': columns,
            'rows': [list(row) for row in rows],
            'count': len(rows)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/validate_level', methods=['POST'])
def validate_level():
    data = request.get_json()
    query = data.get('query', '').strip()
    level_num = data.get('level_num', 0)

    if level_num >= len(LEVELS):
        return jsonify({'error': 'Invalid level'}), 400

    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description] if cursor.description else []
        result_data = {'columns': columns, 'rows': [list(r) for r in rows]}

        validation = validate_level_query(level_num, query, result_data)
        
        if validation['passed']:
            if 'levels_completed' not in session:
                session['levels_completed'] = []
            completed = session['levels_completed']
            if level_num not in completed:
                completed.append(level_num)
                session['levels_completed'] = completed
                session['score'] = session.get('score', 0) + 100
            
            return jsonify({
                'passed': True,
                'score': session['score'],
                'next_level': level_num + 1,
                'message': validation['message'],
                'columns': columns,
                'rows': [list(r) for r in rows],
                'count': len(rows)
            })
        else:
            return jsonify({
                'passed': False,
                'message': validation['message'],
                'columns': columns,
                'rows': [list(r) for r in rows],
                'count': len(rows)
            })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/hint/<int:level_num>', methods=['GET'])
def get_hint(level_num):
    if level_num >= len(LEVELS):
        return jsonify({'error': 'Invalid level'}), 400

    hints_used = session.get('hints_used', {})
    key = str(level_num)
    hint_index = hints_used.get(key, 0)
    
    level = LEVELS[level_num]
    hints = level.get('hints', [])
    
    if hint_index >= len(hints):
        return jsonify({'hint': 'No more hints available for this level.', 'penalty': 0})
    
    hint = hints[hint_index]
    hints_used[key] = hint_index + 1
    session['hints_used'] = hints_used
    
    # Apply penalty
    penalty = 25
    session['score'] = max(0, session.get('score', 0) - penalty)
    
    return jsonify({
        'hint': hint,
        'penalty': penalty,
        'score': session['score'],
        'hint_num': hint_index + 1,
        'total_hints': len(hints)
    })

@app.route('/api/mystery_hint', methods=['GET'])
def mystery_hint_api():
    hint_num = request.args.get('num', 1, type=int)
    hint = get_mystery_hint(hint_num)
    penalty = 50
    session['score'] = max(0, session.get('score', 0) - penalty)
    return jsonify({'hint': hint, 'penalty': penalty, 'score': session['score']})

@app.route('/api/get_tables', methods=['GET'])
def get_tables():
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
        tables = [row[0] for row in cursor.fetchall()]
        return jsonify({'tables': tables})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/get_schema/<table_name>', methods=['GET'])
def get_schema(table_name):
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute(f"PRAGMA table_info({table_name})")
        cols = cursor.fetchall()
        return jsonify({'columns': [{'name': c[1], 'type': c[2]} for c in cols]})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/result')
def result():
    score = session.get('score', 0)
    return render_template('result.html', score=score)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
