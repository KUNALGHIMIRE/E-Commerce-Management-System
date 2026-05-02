# from flask import Flask, request, jsonify, session
# from flask_cors import CORS
# import psycopg2
# import psycopg2.extras

# app = Flask(__name__)
# app.secret_key = 'your-secret-key-here'
# CORS(app, supports_credentials=True)

# def get_db():
#     try:
#         return psycopg2.connect(
#             host='localhost',
#             database='techstore',
#             user='postgres',
#             password='12345'
#         )
#     except Exception as e:
#         print(f"Database connection error: {e}")
#         return None

# # Test route
# @app.route('/')
# def home():
#     return jsonify({'message': 'Flask server is running!'})

# @app.route('/api/test', methods=['GET'])
# def test():
#     return jsonify({'message': 'API is working!', 'status': 'ok'})

# # Products route
# @app.route('/api/products', methods=['GET'])
# def get_products():
#     try:
#         conn = get_db()
#         if not conn:
#             return jsonify([])
        
#         category = request.args.get('category', 'All')
#         cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
#         if category == 'All':
#             cur.execute('SELECT * FROM products ORDER BY id')
#         else:
#             cur.execute('SELECT * FROM products WHERE category = %s ORDER BY id', (category,))
        
#         products = [dict(row) for row in cur.fetchall()]
#         cur.close()
#         conn.close()
#         return jsonify(products)
#     except Exception as e:
#         print(f"Error: {e}")
#         return jsonify([])

# # Cart routes
# @app.route('/api/cart', methods=['GET'])
# def get_cart():
#     if 'user_email' not in session:
#         session['user_email'] = 'demo@example.com'
#     return jsonify([])

# @app.route('/api/cart', methods=['POST'])
# def add_to_cart():
#     if 'user_email' not in session:
#         session['user_email'] = 'demo@example.com'
#     return jsonify({'success': True})

# @app.route('/api/cart/<int:product_id>', methods=['DELETE'])
# def remove_from_cart(product_id):
#     return jsonify({'success': True})

# @app.route('/api/cart/clear', methods=['POST'])
# def clear_cart():
#     return jsonify({'success': True})

# @app.route('/api/login', methods=['POST'])
# def login():
#     data = request.json
#     email = data.get('email')
#     session['user_email'] = email
#     return jsonify({'success': True, 'email': email})

# if __name__ == '__main__':
#     print("=" * 50)
#     print("🚀 Server starting...")
#     print("📍 URL: http://localhost:5000")
#     print("📋 Test URL: http://localhost:5000/api/test")
#     print("=" * 50)
#     app.run(debug=True, port=5000, host='localhost')
from flask import Flask, request, jsonify, session
from flask_cors import CORS
import psycopg2
import psycopg2.extras

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'
CORS(app, supports_credentials=True)

def get_db():
    return psycopg2.connect(
        host='localhost',
        database='techstore',
        user='postgres',
        password='12345'  # Change to your PostgreSQL password
    )

@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({'message': 'API is working!', 'status': 'ok'})

@app.route('/api/products', methods=['GET'])
def get_products():
    conn = get_db()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('SELECT * FROM products ORDER BY id')
    products = [dict(row) for row in cur.fetchall()]
    cur.close()
    conn.close()
    return jsonify(products)

@app.route('/api/cart', methods=['GET'])
def get_cart():
    if 'user_email' not in session:
        session['user_email'] = 'demo@example.com'
    
    conn = get_db()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('SELECT * FROM cart WHERE user_email = %s', (session['user_email'],))
    cart_items = [dict(row) for row in cur.fetchall()]
    cur.close()
    conn.close()
    print(f"Cart items: {len(cart_items)}")
    return jsonify(cart_items)

@app.route('/api/cart', methods=['POST'])
def add_to_cart():
    if 'user_email' not in session:
        session['user_email'] = 'demo@example.com'
    
    data = request.json
    print(f"Adding to cart: {data}")
    
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO cart (user_email, product_id, product_name, product_price) VALUES (%s, %s, %s, %s)',
        (session['user_email'], data['id'], data['name'], data['price'])
    )
    conn.commit()
    cur.close()
    conn.close()
    
    print("Added successfully!")
    return jsonify({'success': True})

@app.route('/api/cart/<int:product_id>', methods=['DELETE'])
def remove_from_cart(product_id):
    if 'user_email' not in session:
        return jsonify({'error': 'Not logged in'}), 401
    
    conn = get_db()
    cur = conn.cursor()
    cur.execute('DELETE FROM cart WHERE user_email = %s AND product_id = %s', 
                (session['user_email'], product_id))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'success': True})

@app.route('/api/cart/clear', methods=['POST'])
def clear_cart():
    if 'user_email' not in session:
        return jsonify({'error': 'Not logged in'}), 401
    
    conn = get_db()
    cur = conn.cursor()
    cur.execute('DELETE FROM cart WHERE user_email = %s', (session['user_email'],))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'success': True})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    session['user_email'] = email
    print(f"User logged in: {email}")
    return jsonify({'success': True, 'email': email})

if __name__ == '__main__':
    print("=" * 50)
    print("🚀 Server running on http://localhost:5000")
    print("📋 Test: http://localhost:5000/api/test")
    print("📋 Products: http://localhost:5000/api/products")
    print("=" * 50)
    app.run(debug=True, port=5000)