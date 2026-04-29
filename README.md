# kino-bot 🎬

Telegram bot orqali kinolar haqida ma'lumot olish uchun oddiy va foydali ilovasi.

## Tavsifi

**kino-bot** - Bu aiogram kutubxonasi asosida yaratilgan Telegram boti bo'lib, foydalanuvchilar kino kodlarini kiritsalar, mos kino nomini olishlari mumkin. Bot Uzbek tilida ishlaydi va oddiy interfeysga ega.

## Xususiyatlari

✅ Tezkor javob  
✅ Oson foydalanish  
✅ Uzbek tilida ishlaydi  
✅ Async/await texnologiyasi  
✅ Logging tizimi

## O'rnatish

### Talab qilinadigan narsalar
- Python 3.8+
- pip paket boshqaruvchisi

### Qadamlar

1. Reposini klonlang:
```bash
git clone https://github.com/bahromyoldoahev376-crypto/kino-bot.git
cd kino-bot
```

2. Virtual muhit yaratib, faollashtiring:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac uchun
# yoki
venv\Scripts\activate  # Windows uchun
```

3. Zaruriy paketlarni o'rnatib qo'ying:
```bash
pip install -r requirements.txt
```

## Konfiguratsiya

1. **BotFather dan token oling:**
   - Telegram'da @BotFather botga xabar yuboring
   - `/newbot` buyrug'ini kiriting
   - Bot nomini va username'ni tanlang
   - Olingan tokenni saqlang

2. **main.py da tokenni o'rnatib qo'ying:**
```python
TOKEN = "SIZNING_BOT_TOKENINGIZ"
```

3. **Kino ma'lumotlarini qo'shib/o'zgartirib qo'ying:**
```python
KINOLAR = {
    "101": "Avatar",
    "102": "Fast & Furious",
    "103": "John Wick"
}
```

## Foydalanish

Botni ishga tushiring:
```bash
python main.py
```

Telegram'da botga xabar yuboring:
1. `/start` buyrug'ini yuboring
2. Kino kodini yuboring (masalan: "101", "102", "103")
3. Bot kino nomini qaytaradi

**Misol:**
```
Foydalanuvchi: 101
Bot: 🎥 Kino topildi:
     Avatar
```

## Struktura

```
kino-bot/
├── main.py           # Asosiy bot fayli
├── requirements.txt  # Zaruriy paketlar
└── README.md        # Bu fayl
```

## Zaruriy paketlar

- **aiogram** - Telegram Bot API kutubxonasi
- **asyncio** - Async programmaviy interfeys

Batafsil: `requirements.txt` faylini qarang.

## Loyihani Rivojlantirish

Agar siz bu loyihani kengaytirmoqchi bo'lsangiz, quyidagi qo'shilishlarni o'ylab ko'ring:

- 📊 Database integratsiyasi (SQLite, PostgreSQL)
- 🎨 Inline keyboard (InlineKeyboardMarkup)
- 💾 Stateful user sessions
- 🔍 Kino qidirish funksionali
- 📦 Raytinglar va kommentariyalar sistema
- 🌐 Bir nechta tilli qo'llab-quvvatlash

## Xavfsizlik Ogohlantirmasi

⚠️ **Bot tokenini hech qachon publicga ochiq qo'ymang!**
- `.gitignore` faylidan foydalaning
- Tokenni `.env` faylida saqlang
- Parol va sensitive ma'lumotlarni repositoryda saqlashdan saqlinin

## Muammolar va Takliflar

Agar sizda muammolar yoki takliflar bo'lsa, [Issues](https://github.com/bahromyoldoahev376-crypto/kino-bot/issues) bo'limiga yozing.

## Litsenziya

MIT Litsenziyasi - Batafsil uchun LICENSE faylini qarang.

## Mualliflar

👤 **bahromyoldoahev376-crypto**

---

**O'xshash loyihalarni ko'ring:** [GitHub](https://github.com/bahromyoldoahev376-crypto)  
**Yaratilgan:** 2026-yil