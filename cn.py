from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

@app.route('/save', methods=['POST'])
def save_data():
    bookid = request.form.get('bookid')
    name = request.form.get('name')
    gmail = request.form.get('gmail')
    phone = request.form.get('phone')
    
    if not all([bookid, name, gmail, phone]):
        return jsonify({'message': 'All fields must be filled in.'}), 400

    try:
        bookid = int(bookid)
        connection = pymysql.connect(host='localhost', user='root', password='root', database='hotel')
        with connection.cursor() as cursor:
            sql = "INSERT INTO hotel (BookID, Name, Gmail, Phone) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (bookid, name, gmail, phone))
            connection.commit()
        return jsonify({'message': 'Data saved successfully'})
    except ValueError:
        return jsonify({'message': 'BookID must be an integer.'}), 400
    except pymysql.MySQLError as e:
        return jsonify({'message': f'An error occurred: {e}'}), 500
    finally:
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
