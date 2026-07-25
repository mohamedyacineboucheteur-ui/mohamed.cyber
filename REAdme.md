import subprocess
import time
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma:2b"

def query_ollama(prompt_text):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt_text,
        "stream": False,
        "options": {"temperature": 0.1}
    }
    response = requests.post(OLLAMA_URL, json=payload, timeout=20)
    return response.json().get("response", "")

def monitor_system_journal():
    print("[*] Starting Local SOC Copilot...")
    cmd = ["journalctl", "-f", "-n", "0", "-o", "short"]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True)
    
    while True:
        line = process.stdout.readline()
        if "Failed password" in line or "Invalid user" in line:
            prompt = f"""
            [TASK] Act as a Senior SOC Analyst. Analyze this log entry.
            [LOG ENTRY] {line.strip()}
            [FORMAT] 1. Potential Threat 2. Risk Level 3. Recommended Action
            """
            print(query_ollama(prompt))

if __name__ == "__main__":
    monitor_system_journal()
