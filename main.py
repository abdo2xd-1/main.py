from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import os

# كود واجهة Mnofy Master الاحترافية
class MnofyMasterApp(App):
    def build(self):
        # تنظيم الواجهة بشكل رأسي مع إضافة مسافات جمالية
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # عنوان التطبيق الرئيسي
        self.lbl = Label(
            text="Mnofy Master v1.0\nنظام التحكم الآلي المتكامل", 
            font_size='28sp', 
            halign='center',
            color=(0, 1, 0.5, 1) # لون أخضر مميز
        )
        
        # زر بدء المسح والسيطرة
        btn = Button(
            text="ابدأ السيطرة والمسح الآن", 
            size_hint=(1, 0.4), 
            background_color=(0.1, 0.5, 0.8, 1), # لون أزرق
            font_size='20sp'
        )
        
        # ربط الزر بوظيفة الأتمتة
        btn.bind(on_press=self.start_automation)
        
        layout.add_widget(self.lbl)
        layout.add_widget(btn)
        return layout

    def start_automation(self, instance):
        # هذه الرسالة ستظهر فور الضغط على الزر لتأكيد العمل الآلي
        self.lbl.text = "[+] جاري فحص الشبكات المحيطة...\n[+] محاولة تخطي حماية الميكروتك...\n[+] البحث عن ثغرات الـ DNS..."
        print("بدأ Mnofy Master في تنفيذ عمليات الأتمتة")

if __name__ == "__main__":
    MnofyMasterApp().run()