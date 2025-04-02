import subprocess
import time
import json

CONFIG_PATH = "config.json"

def load_config():
    with open(CONFIG_PATH) as f:
        return json.load(f)

def start_recording(input_url, record_file):
    print("▶️ Starting recording...")
    return subprocess.Popen([
        "ffmpeg", "-y", "-i", input_url, "-c", "copy", "-f", "flv", record_file
    ])

def start_restream(record_file, output_url):
    print("🚀 Starting delayed restream...")
    return subprocess.Popen([
        "ffmpeg", "-re", "-i", record_file, "-c", "copy", "-f", "flv", output_url
    ])

def main():
    config = load_config()

    stream_key = config["stream_key"]
    delay_minutes = config["delay_minutes"]
    output_rtmp = config["output_rtmp"]
    record_file = config["record_file"]

    input_url = f"rtmp://rtmp-server/live/{stream_key}"

    recorder = start_recording(input_url, record_file)

    print(f"⏳ Waiting {delay_minutes} minutes before restream...")
    time.sleep(delay_minutes * 60)

    restreamer = start_restream(record_file, output_rtmp)

    restreamer.wait()
    recorder.terminate()

if __name__ == "__main__":
    main()
