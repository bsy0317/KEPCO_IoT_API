from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import powerplan

app = Flask(__name__)
CORS(app)
        
@app.route('/', methods=['POST'])
def getUsagePowerData():
    if request.content_type != "application/json":
        return jsonify({'Message': "Invalid Content-Type"}), 400
    data = request.get_json()
    if data is None:
        return jsonify({'Message': "Empty JSON"}), 400
    USER_ID = data.get('USER_ID','NULL')
    USER_PWD = data.get('USER_PWD','NULL')
    IS_SIMPLE = data.get('SIMPLE',True)
    print(type(IS_SIMPLE))
    print(IS_SIMPLE)
    SELECT_DT = data.get('SELECT_DT', datetime.now().strftime('%Y-%m-%d'))
    if USER_ID == 'NULL' or USER_PWD == 'NULL':
        return jsonify({'Message': "Invalid JSON",'Example JSON':'{"USER_ID":"your_id","USER_PWD":"your_pw","SIMPLE":"True","SELECT_DT":"2023-01-01"}'}), 500
    return jsonify(powerplan.scraping(USER_ID, USER_PWD, SELECT_DT, IS_SIMPLE)), 200
    
@app.route('/')
def returnEmptyError():
    return jsonify({'Message': "Invalid request"}), 403
    
    
if __name__ == '__main__':
    #app.run(host="0.0.0.0", port=3388, debug=True, ssl_context=ssl_context)
    app.run(host="0.0.0.0", port=3389, debug=True)