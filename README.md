# RESTEAM / RTMP PROJECT

RESTEAM is a convenient solution for organizing live broadcasts through an RTMP server with the capability of delayed streaming.

## Main Features

- **RTMP Server:** Receive and restream broadcasts.
- **Stream Delay:** Ability to set stream delay (e.g., 30 minutes).
- **Web Interface:** Easy management of delay settings and RTMP URLs through a user-friendly web interface.

## Requirements

- Ubuntu 20.04+ / Debian 10+ server
- Docker and Docker Compose v2.0

sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version


## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yatoropov/delay-streamer-full.git
cd delay-streamer-full
```

### 2. Configuration

Edit the configuration file located at:

```
delay-streamer-full/delay-streamer/config.json
```

Example configuration:

```json
{
  "stream_key": "delay",          // Stream key used to receive the RTMP stream
  "delay_minutes": 30,            // Delay duration in minutes
  "output_rtmp": "rtmp://a.rtmp.youtube.com/live2/key",  // URL to forward the delayed stream
  "record_file": "buffer.flv"    // Temporary file name used for storing the stream
}
```

### 3. Launch the application

```bash
docker-compose up -d
```

The application will be available at: `http://your-server-address:5000`

## Usage

After launch, open the web interface at `http://your-server-address:5000`, adjust settings as needed (stream delay, RTMP URL), and start streaming.

## Contributing

We welcome your pull requests and ideas!

## License

This project is licensed under the MIT License.

---
Author: OnlineStage




