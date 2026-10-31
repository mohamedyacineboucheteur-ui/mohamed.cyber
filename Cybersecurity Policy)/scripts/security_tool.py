import re
import os
from cryptography.fernet import Fernet

def check_password_strength(password):
    """
    [القسم الأول]: فحص مدى التزام كلمة المرور بسياسات الأمان المؤسسية
    تشترط الشركات الكبرى: 8 خانات على الأقل، حروف كبيرة وصغيرة، أرقام، ورموز خاصة.
    """
    print("\n[*] جاري فحص سياسة قوة كلمة المرور...")
    
    if len(password) < 8:
        return "❌ ضعيفة جداً: كلمة المرور أقصر من 8 أحرف."
    if not re.search(r"[A-Z]", password):
        return "❌ ضعيفة: يجب أن تحتوي على حرف كبير واحد (A-Z) على الأقل."
    if not re.search(r"[a-z]", password):
        return "❌ ضعيفة: يجب أن تحتوي على حرف صغير واحد (a-z) على الأقل."
    if not re.search(r"[0-9]", password):
        return "❌ ضعيفة: يجب أن تحتوي على رقم واحد على الأقل (0-9)."
    if not re.search(r"[@$!%*?&]", password):
        return "❌ ضعيفة: يجب أن تحتوي على رمز خاص واحد على الأقل مثل (@$!%*?&)."
        
    return "✅ ممتازة: كلمة المرور تلبي معايير سياسة التعقيد المؤسسي."


def generate_and_save_key():
    """توليد مفتاح تشفير عشوائي وحفظه محلياً"""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("[+] تم إنشاء مفتاح التشفير وحفظه في ملف 'secret.key'.")


def load_key():
    """تحميل مفتاح التشفير من الملف"""
    return open("secret.key", "rb").read()


def encrypt_file(file_path):
    """
    [القسم الثاني]: تشفير الملفات الحساسة تطبيقاً لسياسة Data at Rest
    استخدام خوارزمية Fernet (المبنية على AES)
    """
    if not os.path.exists("secret.key"):
        generate_and_save_key()
        
    key = load_key()
    f = Fernet(key)
    
    try:
        with open(file_path, "rb") as file:
            file_data = file.read()
            
        encrypted_data = f.encrypt(file_data)
        
        with open(file_path + ".enc", "wb") as file:
            file.write(encrypted_data)
            
        print(f"[+] تم تشفير الملف بنجاح وحفظه بصيغة: {file_path}.enc")
    except FileNotFoundError:
        print(f"[-] خطأ: الملف {file_path} غير موجود.")


if __name__ == "__main__":
    print("="*50)
    print(" أدوات الأمن السيبراني التطبيقية - مشروع محمد ياسين")
    print("="*50)
    
    # تجربة فحص كلمة المرور
    test_password = input("أدخل كلمة مرور لفحصها معايير الأمان: ")
    result = check_password_strength(test_password)
    print(result)
    
    print("-" * 50)
    
    # تجربة تشفير ملف نصي تجريبي
    choice = input("هل تريد تجربة تشفير ملف نصي تجريبي؟ (y/n): ")
    if choice.lower() == 'y':
        # إنشاء ملف تجريبي مؤقت للاختبار
        sample_file = "confidential_data.txt"
        with open(sample_file, "w", encoding="utf-8") as f:
            f.write("هذه بيانات سرية خاصة بالشركة ويجب تشفيرها!")
            
        print([i] تم إنشاء ملف تجريبي باسم: {sample_file})
        encrypt_file(sample_file)سسس
