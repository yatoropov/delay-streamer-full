# DELAY-STREAMER

Проєкт DELAY-STREAMER — це зручне рішення для організації трансляцій прямих ефірів через RTMP сервер з можливістю затримки трансляції (відкладеного рестріму).

## Основний функціонал

- Приймає трансляцію на `rtmp://<your-server-address>/live/delay`
- Записує її в файл
- Через вказану затримку запускає рестрім на іншу адресу

## Основне наповнення

- **RTMP сервер:** Прийом трансляцій та веб-інтерфейс з керуванням затримкою та RTMP-адресою через зручний веб-інтерфейс.
- **FFMPEG двіжок:** Запис та рестрім 

## Вимоги

- Сервер з Ubuntu 20.04+ / Debian 10+
- Docker 
```bash

# Uninstall all unofficials dockers
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done

# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

# Install official Docker 
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Test Docker 
sudo docker run hello-world
```

## A) Встановлення ручне

### 1. Клонування репозиторію

```bash
git clone https://github.com/yatoropov/delay-streamer-full.git
cd delay-streamer-full
```

### 2. Конфігурація

- *Опціонально* відредагуйте файл конфігурації, що знаходиться за шляхом:

```
delay-streamer-full/delay-streamer/config.json
```

Приклад налаштувань:

```json
{
  "stream_key": "delay",          // Ключ потоку, за допомогою якого буде прийматися RTMP-потік
  "delay_minutes": 30,            // Затримка трансляції в хвилинах
  "output_rtmp": "rtmp://a.rtmp.youtube.com/live2/key",  // Адреса, куди буде відправлятись затриманий потік
  "record_file": "buffer.flv"    // Назва файлу, який використовується для тимчасового зберігання трансляції
}
```

### 3. Запуск

```bash
sudo docker compose up --build -d
```

Web-Ui буде доступна за адресою: `http://<your-server-address>:5000`

## B) Автоматичне встановлення за запуск (включно з Docker) на чистий сервер з Ubuntu 20.04+ / Debian 10+ 

```bash
wget https://raw.githubusercontent.com/yatoropov/delay-streamer-full/d2bb1a34aaa1f540812a05667d3ac3e483d804af/install.sh
sudo chmod +x install.sh
./install.sh
```

## Використання

Після запуску відкрийте веб-інтерфейс за адресою `http://<your-server-address>:5000`, змініть необхідні налаштування (затримка трансляції, RTMP-адреса).

Запустіть трансляцію на свій DELAY-STREAMER сервер: `rtmp://<your-server-address>/live/delay`.

Enjoy!

## Внесок у розвиток

Будемо вдячні за ваші pull-запити та ідеї!

## Ліцензія

Цей проєкт поширюється під ліцензією MIT.

---
Автор: OnlineStage
