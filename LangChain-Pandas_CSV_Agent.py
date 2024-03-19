from flask import Flask, jsonify, request
import os
import pandas as pd
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain.llms import OpenAI
import pandas as pd
import secrets
from flask_cors import CORS,cross_origin
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import io
import base64
app = Flask(__name__)
CORS(app)
app.secret_key = secrets.token_hex(16)

# Setup the API key
os.environ['OPENAI_API_KEY'] = "[YOUR-API-KEY]"

# Create OpenAI instance and agent (without loading data yet)
openai = OpenAI(temperature=0.0)

def plot_to_base64(plot):
    """Converts a Matplotlib plot to base64 for embedding in JSON."""
    image_stream = io.BytesIO()
    plot.savefig(image_stream, format='png')
    image_stream.seek(0)
    return base64.b64encode(image_stream.read()).decode('utf-8')

@app.route('/ingest', methods=['POST'])
@cross_origin()
def upload_csv():
    try:
        # Check if the 'file' field is present in the request
        if 'file' not in request.files:
            return jsonify({"error": "'file' field is required in the request"}), 400

        file = request.files['file']

        # Check if the file is not empty
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400
        
        if file.filename.endswith('.csv'):
            pd.DataFrame(pd.read_csv(file)).to_csv("df155.csv")
            data = pd.read_csv("df155.csv")
            c = data.columns.tolist()
            return jsonify({"message": file.filename + "file uploaded successfully  "})
        elif file.filename.endswith('.xlsx'):
            pd.DataFrame(pd.read_excel(file)).to_csv("df155.csv")
            data = pd.read_csv("df155.csv")
            c = data.columns.tolist()
            return jsonify({"message": file.filename + "file uploaded successfully  "})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    finally:
        return c


@app.route('/qa', methods=['POST'])
@cross_origin()
def ask_question():
    try:
        # Get the question and CSV file path from the request data
        question_data = request.get_json()
        question = question_data.get('question', '')

        # Check if CSV file path is provided
        #if data not in df.csv:
            #return jsonify({"error": "CSV file path must be provided"}), 400

        # Read CSV file into a DataFrame
        data = pd.read_csv("C:/Users/Raja/Downloads/house price.csv")
        data = data[:100]
        #print(data.columns.tolist())
        agent = create_pandas_dataframe_agent(openai, data, verbose=True)
        
        prompt = "If you plot anything then save the plot to C:/Users/Raja/Downloads/plot.png. "


        # Ask the agent and get the response
        response = agent(prompt + question)
        
        if os.path.exists('C:/Users/Raja/Downloads/plot.png'):
            img = mpimg.imread('C:/Users/Raja/Downloads/plot.png')
            encim = base64.b64encode(img).decode('utf-8')
            os.remove('C:/Users/Raja/Downloads/plot.png')
            return jsonify({"response": encim})
        else:
            return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run()


# In[ ]:




