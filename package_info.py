PACKAGE_INFO = {
    "name": "nerotask",
    "version": "0.1.0",
    "author": "Salhi Abdennour",
    "author_email": "abdennoursalhi@yandex.com",
    "description": "A task management application",
    "url": "https://github.com/Salhi-Abdennour/NeroTask",
    "license": "Apache License 2.0",
    "itchio": "Itch.io: https://chrony.itch.io/",
    "carrd": "https://wh01m1.carrd.co/",
    "twitter": "https://x.com/CHR0N1_101"
}

def show_package_info():
    for key, value in PACKAGE_INFO.items():
        print(f"{key.capitalize()}: {value}")
