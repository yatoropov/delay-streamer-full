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

    stream_key = config.get("stream_key", "delay")
    delay_minutes = config.get("delay_minutes", 1)
    output_rtmp = config.get("output_rtmp", "")
    record_file = config.get("record_file", "buffer.flv")

    input_url = f"rtmp://rtmp-server/live/{stream_key}"

    if delay_minutes == 0:
        print("⚡ Прямий рестрім без затримки")
        subprocess.call([
            "ffmpeg", "-i", input_url, "-c", "copy", "-f", "flv", output_rtmp
        ])
        return

    recorder = start_recording(input_url, record_file)

    print(f"⏳ Затримка {delay_minutes} хвилин перед рестрімом...")
    time.sleep(delay_minutes * 60)

    print("🔄 Оновлюю конфіг після затримки...")
    config = load_config()

    restreamer = start_restream(record_file, output_rtmp)

    restreamer.wait()
    recorder.terminate()

if __name__ == "__main__":
    main()
