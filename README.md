# Tonfa
Приложение tonfa позволяет считать допуски и посадки все что связано с ними.

![Bitcoin](https://img.shields.io/badge/bitcoin-2F3134?style=for-the-badge&logo=bitcoin&logoColor=white)
![Solana](https://img.shields.io/badge/solana-%239945FF.svg?style=for-the-badge&logo=solana&logoColor=white)
![Ethereum](https://img.shields.io/badge/Ethereum-3C3C3D?style=for-the-badge&logo=Ethereum&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![BuyMeACoffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)
![Github-sponsors](https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA)
![uv](https://img.shields.io/badge/uv-%23DE5FE9.svg?style=for-the-badge&logo=uv&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Android](https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
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
```sh
# TODO: Вставить команду с git для скачивания проекта
docker build --tag=kivy/buildozer .
docker run --interactive --tty --rm \
    --volume "$HOME/.buildozer":/home/user/.buildozer \
    --volume "$PWD":/home/user/hostcwd \
    kivy/buildozer android release
```
После чего вы сможете перекинуть apk файл на android и оттуда установить его.

### Требования
Для установки и запуска проекта, необходим 
1. [Docker](https://www.docker.com/) 26.1.5+ 
2. [Git](https://git-scm.com/) 2.47.3+

### Установка зависимостей
Для Ubuntu/Debian выполните команду:
```sh
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin git
```

Для MacOS выполните команду:
```sh
brew install --cask docker
```

Для Windows выполните следующие действия:
1. Скачайте [Docker Dekstop](https://www.docker.com/products/docker-desktop/)
2. Запустите установщик.
3. Выполняйте инструкции по установке

## Contributing
<!-- Как помочь в разработке проекта? Как отправить предложение или баг-репорт. Как отправить доработку (оформить pull request, какие стайлгайды используются). Можно вынести в отдельный файл — [Contributing.md](./CONTRIBUTING.md). -->

## FAQ 
<!-- Если потребители вашего кода часто задают одни и те же вопросы, добавьте ответы на них в этом разделе. -->

## To do
- [ ] Добавить иконку для приложения и экран загрузки

## Команда проекта
- [Арман Меликбекян](amelikbekan@gmail.com) - Главный разработчик проекта

