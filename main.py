from pydantic import BaseModel, validator
from datetime import date

class User(BaseModel):
    id: int
    ism: str
    familya: str
    tugilgan_sana: date
    email: str

    @validator('email')
    def email_malumotlarini_kontroll_qil(cls, v):
        if '@' not in v:
            raise ValueError('Email manzili @ belgisini o'z ichiga olganligini tekshirib ko'ring')
        return v

    @validator('tugilgan_sana')
    def tugilgan_sana_kiritish(cls, v):
        if v > date.today():
            raise ValueError('Tug'ilgan sana hozirgi sana dan keyin bo'lishi mumkin emas')
        return v

class Arxitektor(BaseModel):
    ism: str
    familya: str
    tajriba_yillari: int
    kompaniya: str

    @validator('tajriba_yillari')
    def tajriba_yillari_kiritish(cls, v):
        if v < 0:
            raise ValueError('Tajriba yillari 0 dan kichik bo'lishi mumkin emas')
        return v

class ArxitektorDasturchi(User, Arxitektor):
    pass

arxitektor_dasturchi = ArxitektorDasturchi(
    id=1,
    ism='Ali',
    familya='Valiyev',
    tugilgan_sana=date(1990, 1, 1),
    email='ali.valiyev@example.com',
    tajriba_yillari=10,
    kompaniya='Google'
)

print(arxitektor_dasturchi.json())
```

Kodda quyidagi narsalar amalga oshirildi:

1. `User` va `Arxitektor` klasslari yaratildi, ular `BaseModel`dan meros olgan.
2. `User` klassida `email` va `tugilgan_sana` kiritish uchun validatsiya qiluvchi metodlar yaratildi.
3. `Arxitektor` klassida `tajriba_yillari` kiritish uchun validatsiya qiluvchi metodlar yaratildi.
4. `ArxitektorDasturchi` klassi yaratildi, u `User` va `Arxitektor` klasslaridan meros olgan.
5. `ArxitektorDasturchi` klassidan ob'ekt yaratildi va uning ma'lumotlari konsolga chiqarildi.
