# Tonfa
Приложение tonfa позволяет считать допуски и посадки, а также то, что связано с ними.

![Bitcoin](https://img.shields.io/badge/bitcoin-2F3134?style=for-the-badge&logo=bitcoin&logoColor=white)
![Solana](https://img.shields.io/badge/solana-%239945FF.svg?style=for-the-badge&logo=solana&logoColor=white)
![Ethereum](https://img.shields.io/badge/Ethereum-3C3C3D?style=for-the-badge&logo=Ethereum&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Github-sponsors](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)
![uv](https://img.shields.io/badge/uv-%23DE5FE9.svg?style=for-the-badge&logo=uv&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Android](https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![F Droid](https://img.shields.io/badge/F_Droid-1976D2?style=for-the-badge&logo=f-droid&logoColor=white)
<!-- Добавьте краткое описание проекта, опишите какую задачу он решает. 1-3 предложения будет достаточно. Добавьте бейджи для важных статусов проекта: статус разработки (в разработке, на поддержке и т.д.), статус билда, процент покрытия тестами и тд. -->

## Содержание
- [Технологии](#технологии)
- [Использование](#использование)
- [Contributing](#contributing)
- [Faq](#faq)
- [To do](#to-do)
- [Команда проекта](#команда-проекта)

## Технологии
- [KivyMD](https://github.com/kivymd/KivyMD)
- [Kivy](https://kivy.org/)
- [Buildozer](https://github.com/kivy/buildozer)
- [Python](https://www.python.org/)

## Использование
Существуют 2 способа установки приложения на android:
1. Зайти на оф. сайт [f-droid](https://f-droid.org/) или [мобильное приложение](https://f-droid.org/F-Droid.apk) и скачать и установить оттуда приложение tonfa.
2. Выполнить следующие команды (необходим установленный git, docker):
- Включить режим разработчика на своем телефоне.
- Включить режим отладки.
- Подключиться к телефону.
- Выполнить в терминале следующие команды.
```sh
git clone https://github.com/Cpyte-Engine-Developer/tonfa.git
cd tonfa
keytool -genkey -v -keystore tonfa.keystore -alias tonfa -keyalg RSA -keysize 2048 -validity 10000
sh build_and_compile.sh
adb install -r bin/tonfa-0.0.1-arm64-v8a-release-signed.apk
```

### Требования
Для установки и запуска проекта, необходим 
1. [Docker](https://www.docker.com/) 26.1.5+ 
2. [Git](https://git-scm.com/) 2.47.3+
3. [Zipalign](https://github.com/blattmann/zipalign)
4. [ADB](https://developer.android.com/tools/adb?hl=ru)
5. [ApkSigner](https://developer.android.com/tools/apksigner?hl=ru)
6. [KeyTool](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/keytool.html)

### Установка зависимостей
Для Ubuntu/Debian выполните команду:
```sh
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin git zipalign adb apksigner default-jdk
```

Для MacOS выполните команду:
```sh
brew install --cask docker android-commandline-tools
brew install git openjdk@21
```

Для Windows выполните следующие действия:
1. Скачайте [Docker Dekstop](https://www.docker.com/products/docker-desktop/)
2. Запустите установщик.
3. Выполняйте инструкции по установке

## Contributing
<!-- Как помочь в разработке проекта? Как отправить предложение или баг-репорт. Как отправить доработку (оформить pull request, какие стайлгайды используются). Можно вынести в отдельный файл — [Contributing.md](./CONTRIBUTING.md). -->

## FAQ 
<!-- Если потребители вашего кода часто задают одни и те же вопросы, добавьте ответы на них в этом разделе. -->

## Команда проекта
- [Cpyte-Engine-Developer](amelikbekan@gmail.com) - Главный разработчик проекта

