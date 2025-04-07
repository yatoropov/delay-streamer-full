# DELAY-STREAMER

The DELAY-STREAMER project is a convenient solution for organizing live broadcasts through an RTMP server with the capability of delayed streaming (time-shifted restreaming).

## Main Features

- Receives a broadcast on `rtmp://<your-server-address>/live/delay`
- Records it into a file
- Initiates restreaming to another address after the specified delay

## Key Components

- **RTMP Server:** Broadcast reception and web interface for managing delay settings and RTMP addresses through a user-friendly UI.
- **FFMPEG Engine:** Recording and restreaming.

## Requirements

- Server with Ubuntu 20.04+ / Debian 10+
- Docker

```bash
# Uninstall all unofficial dockers
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done

# Add Docker's official GPG key
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add Docker's repository to Apt sources
sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
$(. /etc/os-release && echo \"${UBUNTU_CODENAME:-$VERSION_CODENAME}\") stable" > /etc/apt/sources.list.d/docker.list'
sudo apt-get update

# Install official Docker packages
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Test Docker installation
sudo docker run hello-world
```

## A) Manual Installation

### 1. Clone the repository

```bash
git clone https://github.com/yatoropov/delay-streamer-full.git
cd delay-streamer-full
```

### 2. Configuration

- *Optionally*, edit the configuration file located at:

```
delay-streamer-full/delay-streamer/config.json
```

Example configuration:

```json
{
  "stream_key": "delay",          // Stream key used for receiving the RTMP stream
  "delay_minutes": 30,            // Delay duration in minutes
  "output_rtmp": "rtmp://a.rtmp.youtube.com/live2/key",  // Destination address for delayed stream
  "record_file": "buffer.flv"    // Temporary file used for stream buffering
}
```

### 3. Launch

```bash
sudo docker compose up --build -d
```

The web interface will be available at: `http://<your-server-address>:5000`

## B) Automatic Installation and Launch (including Docker) on a fresh Ubuntu 20.04+ / Debian 10+ server

```bash
wget https://raw.githubusercontent.com/yatoropov/delay-streamer-full/d2bb1a34aaa1f540812a05667d3ac3e483d804af/install.sh
sudo chmod +x install.sh
./install.sh
```

## Usage

After launch, open the web interface at `http://<your-server-address>:5000`, adjust necessary settings (stream delay, RTMP URL).

Start streaming to your DELAY-STREAMER server at: `rtmp://<your-server-address>/live/delay`.

Enjoy!

## Contributing

We welcome your pull requests and ideas!

## License

This project is licensed under the MIT License.

---
Author: OnlineStage

