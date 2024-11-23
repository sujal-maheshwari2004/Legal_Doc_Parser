@echo off
echo Installing required dependencies...
pip install -r requirements.txt

echo Pulling the ollama models...
ollama pull llama3.2

echo Starting the Streamlit app...
streamlit run app.py

pause
