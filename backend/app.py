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
# #     app.run(debug=True, port=5000, host='localhost')
# from flask import Flask, request, jsonify, session
# from flask_cors import CORS
# import psycopg2
# import psycopg2.extras

# app = Flask(__name__)
# app.secret_key = 'your-secret-key-here'
# CORS(app, supports_credentials=True)

# def get_db():
#     return psycopg2.connect(
#         host='localhost',
#         database='techstore',
#         user='postgres',
#         password='12345'  # Change to your PostgreSQL password
#     )

# @app.route('/api/test', methods=['GET'])
# def test():
#     return jsonify({'message': 'API is working!', 'status': 'ok'})

# @app.route('/api/products', methods=['GET'])
# def get_products():
#     conn = get_db()
#     cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#     cur.execute('SELECT * FROM products ORDER BY id')
#     products = [dict(row) for row in cur.fetchall()]
#     cur.close()
#     conn.close()
#     return jsonify(products)

# @app.route('/api/cart', methods=['GET'])
# def get_cart():
#     if 'user_email' not in session:
#         session['user_email'] = 'demo@example.com'
    
#     conn = get_db()
#     cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#     cur.execute('SELECT * FROM cart WHERE user_email = %s', (session['user_email'],))
#     cart_items = [dict(row) for row in cur.fetchall()]
#     cur.close()
#     conn.close()
#     print(f"Cart items: {len(cart_items)}")
#     return jsonify(cart_items)

# @app.route('/api/cart', methods=['POST'])
# def add_to_cart():
#     if 'user_email' not in session:
#         session['user_email'] = 'demo@example.com'
    
#     data = request.json
#     print(f"Adding to cart: {data}")
    
#     conn = get_db()
#     cur = conn.cursor()
#     cur.execute(
#         'INSERT INTO cart (user_email, product_id, product_name, product_price) VALUES (%s, %s, %s, %s)',
#         (session['user_email'], data['id'], data['name'], data['price'])
#     )
#     conn.commit()
#     cur.close()
#     conn.close()
    
#     print("Added successfully!")
#     return jsonify({'success': True})

# @app.route('/api/cart/<int:product_id>', methods=['DELETE'])
# def remove_from_cart(product_id):
#     if 'user_email' not in session:
#         return jsonify({'error': 'Not logged in'}), 401
    
#     conn = get_db()
#     cur = conn.cursor()
#     cur.execute('DELETE FROM cart WHERE user_email = %s AND product_id = %s', 
#                 (session['user_email'], product_id))
#     conn.commit()
#     cur.close()
#     conn.close()
#     return jsonify({'success': True})

# @app.route('/api/cart/clear', methods=['POST'])
# def clear_cart():
#     if 'user_email' not in session:
#         return jsonify({'error': 'Not logged in'}), 401
    
#     conn = get_db()
#     cur = conn.cursor()
#     cur.execute('DELETE FROM cart WHERE user_email = %s', (session['user_email'],))
#     conn.commit()
#     cur.close()
#     conn.close()
#     return jsonify({'success': True})

# @app.route('/api/login', methods=['POST'])
# def login():
#     data = request.json
#     email = data.get('email')
#     session['user_email'] = email
#     print(f"User logged in: {email}")
#     return jsonify({'success': True, 'email': email})

# if __name__ == '__main__':
#     print("=" * 50)
#     print("🚀 Server running on http://localhost:5000")
#     print("📋 Test: http://localhost:5000/api/test")
#     print("📋 Products: http://localhost:5000/api/products")
#     print("=" * 50)
#     app.run(debug=True, port=5000)

# from flask import Flask, request, jsonify, session, send_from_directory
# from flask_cors import CORS
# import psycopg2
# import psycopg2.extras
# import os

# app = Flask(__name__, static_folder='dist')
# app.secret_key = 'your-secret-key-here'
# CORS(app, supports_credentials=True)

# def get_db():
#     return psycopg2.connect(
#         host='localhost',
#         database='techstore',
#         user='postgres',
#         password='12345'  # Change to your PostgreSQL password
#     )

# @app.route('/api/test', methods=['GET'])
# def test():
#     return jsonify({'message': 'API is working!', 'status': 'ok'})

# @app.route('/api/products', methods=['GET'])
# def get_products():
#     conn = get_db()
#     cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#     cur.execute('SELECT * FROM products ORDER BY id')
#     products = [dict(row) for row in cur.fetchall()]
#     cur.close()
#     conn.close()
#     return jsonify(products)

# @app.route('/api/cart', methods=['GET'])
# def get_cart():
#     if 'user_email' not in session:
#         session['user_email'] = 'demo@example.com'
    
#     conn = get_db()
#     cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
#     cur.execute('SELECT * FROM cart WHERE user_email = %s', (session['user_email'],))
#     cart_items = [dict(row) for row in cur.fetchall()]
#     cur.close()
#     conn.close()
#     print(f"Cart items: {len(cart_items)}")
#     return jsonify(cart_items)

# @app.route('/api/cart', methods=['POST'])
# def add_to_cart():
#     if 'user_email' not in session:
#         session['user_email'] = 'demo@example.com'
    
#     data = request.json
#     print(f"Adding to cart: {data}")
    
#     conn = get_db()
#     cur = conn.cursor()
#     cur.execute(
#         'INSERT INTO cart (user_email, product_id, product_name, product_price) VALUES (%s, %s, %s, %s)',
#         (session['user_email'], data['id'], data['name'], data['price'])
#     )
#     conn.commit()
#     cur.close()
#     conn.close()
    
#     print("Added successfully!")
#     return jsonify({'success': True})

# @app.route('/api/cart/<int:product_id>', methods=['DELETE'])
# def remove_from_cart(product_id):
#     if 'user_email' not in session:
#         return jsonify({'error': 'Not logged in'}), 401
    
#     conn = get_db()
#     cur = conn.cursor()
#     cur.execute('DELETE FROM cart WHERE user_email = %s AND product_id = %s', 
#                 (session['user_email'], product_id))
#     conn.commit()
#     cur.close()
#     conn.close()
#     return jsonify({'success': True})

# @app.route('/api/cart/clear', methods=['POST'])
# def clear_cart():
#     if 'user_email' not in session:
#         return jsonify({'error': 'Not logged in'}), 401
    
#     conn = get_db()
#     cur = conn.cursor()
#     cur.execute('DELETE FROM cart WHERE user_email = %s', (session['user_email'],))
#     conn.commit()
#     cur.close()
#     conn.close()
#     return jsonify({'success': True})

# @app.route('/api/login', methods=['POST'])
# def login():
#     data = request.json
#     email = data.get('email')
#     session['user_email'] = email
#     print(f"User logged in: {email}")
#     return jsonify({'success': True, 'email': email})

# # ========== NEW: Serve React Frontend ==========
# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def serve_frontend(path):
#     # Don't interfere with API routes
#     if path.startswith('api/'):
#         return jsonify({'error': 'Not found'}), 404
    
#     # Serve React files from dist folder
#     dist_dir = os.path.join(os.path.dirname(__file__), 'dist')
    
#     # If file exists, serve it
#     if path and os.path.exists(os.path.join(dist_dir, path)):
#         return send_from_directory(dist_dir, path)
    
#     # Otherwise serve index.html (for React Router)
#     return send_from_directory(dist_dir, 'index.html')

# if __name__ == '__main__':
#     print("=" * 50)
#     print("🚀 Server running on http://localhost:5000")
#     print("📋 Test: http://localhost:5000/api/test")
#     print("📋 Products: http://localhost:5000/api/products")
#     print("🌐 Frontend: http://localhost:5000")
#     print("=" * 50)
#     app.run(debug=True, port=5000)
from flask import Flask, request, jsonify, session
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your-secret-key-here')
CORS(app, supports_credentials=True, origins=[
    'http://localhost:5173',
    'http://localhost:5185',
    'https://e-commerce-management-system.vercel.app',
    os.getenv('FRONTEND_URL', '')
])

# Initialize Supabase
supabase = None
try:
    from supabase import create_client
    supabase_url = os.getenv('SUPABASE_URL')
    supabase_key = os.getenv('SUPABASE_KEY')
    
    if supabase_url and supabase_key:
        supabase = create_client(supabase_url, supabase_key)
        print("✅ Supabase initialized successfully")
    else:
        print("⚠️ Supabase credentials missing")
except Exception as e:
    print(f"❌ Failed to initialize Supabase: {str(e)}")

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'supabase_connected': supabase is not None,
        'environment': {
            'supabase_url': bool(os.getenv('SUPABASE_URL')),
            'supabase_key': bool(os.getenv('SUPABASE_KEY')),
            'secret_key': bool(os.getenv('SECRET_KEY')),
            'jwt_secret_key': bool(os.getenv('JWT_SECRET_KEY'))
        }
    })

# Test endpoint
@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({'message': 'API is working!', 'status': 'ok'})

# Get all products
@app.route('/api/products', methods=['GET'])
def get_products():
    if not supabase:
        return jsonify({'error': 'Database not connected', 'details': 'Supabase not initialized'}), 500
    
    try:
        response = supabase.table('products').select('*').order('id').execute()
        return jsonify(response.data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get single product
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    if not supabase:
        return jsonify({'error': 'Database not connected'}), 500
    
    try:
        response = supabase.table('products').select('*').eq('id', product_id).execute()
        if response.data:
            return jsonify(response.data[0])
        return jsonify({'error': 'Product not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get categories
@app.route('/api/categories', methods=['GET'])
def get_categories():
    if not supabase:
        return jsonify({'error': 'Database not connected'}), 500
    
    try:
        response = supabase.table('categories').select('*').order('id').execute()
        return jsonify(response.data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get cart
@app.route('/api/cart', methods=['GET'])
def get_cart():
    if 'user_email' not in session:
        session['user_email'] = 'demo@example.com'
    
    if not supabase:
        return jsonify({'error': 'Database not connected'}), 500
    
    try:
        response = supabase.table('cart').select('*').eq('user_email', session['user_email']).execute()
        return jsonify(response.data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Add to cart
@app.route('/api/cart', methods=['POST'])
def add_to_cart():
    if 'user_email' not in session:
        session['user_email'] = 'demo@example.com'
    
    data = request.json
    
    if not supabase:
        return jsonify({'error': 'Database not connected'}), 500
    
    try:
        response = supabase.table('cart').insert({
            'user_email': session['user_email'],
            'product_id': data['id'],
            'product_name': data['name'],
            'product_price': data['price']
        }).execute()
        return jsonify({'success': True, 'message': 'Added to cart'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Remove from cart
@app.route('/api/cart/<int:product_id>', methods=['DELETE'])
def remove_from_cart(product_id):
    if 'user_email' not in session:
        return jsonify({'error': 'Not logged in'}), 401
    
    if not supabase:
        return jsonify({'error': 'Database not connected'}), 500
    
    try:
        response = supabase.table('cart').delete().eq('user_email', session['user_email']).eq('product_id', product_id).execute()
        return jsonify({'success': True, 'message': 'Removed from cart'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Clear cart
@app.route('/api/cart/clear', methods=['POST'])
def clear_cart():
    if 'user_email' not in session:
        return jsonify({'error': 'Not logged in'}), 401
    
    if not supabase:
        return jsonify({'error': 'Database not connected'}), 500
    
    try:
        response = supabase.table('cart').delete().eq('user_email', session['user_email']).execute()
        return jsonify({'success': True, 'message': 'Cart cleared'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Login
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    session['user_email'] = email
    return jsonify({'success': True, 'email': email, 'message': 'Logged in successfully'})

# Logout
@app.route('/api/logout', methods=['POST'])
def logout():
    session.pop('user_email', None)
    return jsonify({'success': True, 'message': 'Logged out'})

# Root endpoint
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'name': 'TechStore API',
        'version': '1.0.0',
        'status': 'running',
        'endpoints': [
            '/api/health',
            '/api/test', 
            '/api/products',
            '/api/products/<id>',
            '/api/categories',
            '/api/cart',
            '/api/login',
            '/api/logout'
        ]
    })

# For Vercel serverless
app = app

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("=" * 50)
    print("🚀 TechStore API Server")
    print("=" * 50)
    print(f"📍 Local: http://localhost:{port}")
    print(f"📋 Health: http://localhost:{port}/api/health")
    print(f"📋 Products: http://localhost:{port}/api/products")
    print(f"📋 Categories: http://localhost:{port}/api/categories")
    print("=" * 50)
    app.run(debug=True, port=port)