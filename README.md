# برنامج المصروفات الشهرية

نسخة جاهزة للنشر على Render باستخدام Flask + Gunicorn.

## الحسابات التجريبية
- خالد / 12 / 150000
- اسعد / 13 / 250000
- صديق / 14 / 350000
- الرشيد / 15 / 0

## التشغيل محلياً
```bash
pip install -r requirements.txt
python app.py
```
ثم افتح: http://127.0.0.1:5000

## النشر على Render
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`
- Health Check Path: `/`

> هذه نسخة تجريبية. قبل استخدامها لبيانات حقيقية يفضل نقل المستخدمين إلى قاعدة بيانات، تخزين كلمات المرور بشكل مجزأ (hashed)، وإضافة نظام صلاحيات ومحددات لمحاولات تسجيل الدخول.
