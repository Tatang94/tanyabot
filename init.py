#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Impor pustaka standar
import typing

# Impor pustaka pihak ketiga terkait
from telebot import types, util
import telebot
import requests

# Impor spesifik aplikasi/pustaka lokal
import utils

# Terhubung ke bot
# Token ditempatkan di file utils.py. Anda dapat menggantinya dengan token Anda
GPTbot: typing.ClassVar[typing.Any] = telebot.TeleBot(utils.TOKEN)
print(f"Bot sedang online (id: {GPTbot.get_me().id}) \33[0;31m[MODE Awal]\33[m...")

# Mengatur perintah bot
print("[!] Mengonfigurasi perintah bot...")
GPTbot.set_my_commands(
    commands=[
        types.BotCommand(
            command="start",
            description="Mulai bot"
        ),
        types.BotCommand(
            command="ping",
            description="Ping penyedia layanan"
        ),
        types.BotCommand(
            command="settings",
            description="Pengaturan penyedia layanan"
        ),
        types.BotCommand(
            command="chat",
            description="Chat di grup menggunakan perintah ini"
        ),
        types.BotCommand(
            command="tts",
            description="Respon Teks ke Suara Brian"
        ),
        types.BotCommand(
            command="history",
            description="Dapatkan riwayat chat Anda"
        ),
        types.BotCommand(
            command="reset",
            description="Reset riwayat chat Anda"
        ),
        types.BotCommand(
            command="danmode",
            description="Aktifkan/Nonaktifkan mode DAN versi 10.0"
        ),
        types.BotCommand(
            command="features",
            description="Lihat perubahan fitur"
        )
    ]
)
print("[!] Perintah berhasil dikonfigurasi.\n[!] Jalankan main.py")