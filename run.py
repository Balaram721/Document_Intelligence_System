import subprocess
import sys
import webbrowser

def install_requirements():
    print("🔧 Checking and installing required dependencies...")
    subprocess.call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("✔ All dependencies are installed.")

def start_streamlit_app():
    print("🚀 Starting Document Intelligence System...")
    subprocess.Popen([sys.executable, "-m", "streamlit", "run", "ui/app.py"])
    print("✔ UI is running at: http://localhost:8501")
    webbrowser.open("http://localhost:8501")

if __name__ == "__main__":
    print("==========================================")
    print("  DOCUMENT INTELLIGENCE SYSTEM — LAUNCHER  ")
    print("==========================================")

    install_requirements()
    start_streamlit_app()