import smtplib
import time

tm = time.localtime()
saat = time.strftime("%d-%m-20%y %H:%M", tm)
gmailaddress = "refiksoyletmez@gmail.com"
gmailpassword = ""
#Mail listesi
mailto = """
abatihan.ozdemir@turkiyeteknolojitakimi.org
arumeysa.guc@turkiyeteknolojitakimi.org
fatmaerdemmm@gmail.com
sk.erdems@gmail.com
elifince6116@gmail.com
erengun4@gmail.com
ahmet@goksu.in
eminalikonukoglu@gmail.com
dokurokur@gmail.com
volkan.nisancii@gmail.com
yunus.bolgonul@gmail.com
serdar.ozdemir3456@hotmail.com
aaydag2001@gmail.com
zeyneptugrul2002@hotmail.com
gamze.kantar23@hotmail.com
hititoguzkagan@gmail.com""".split("\n")
subject = "konuBuraya"
msg = f"Mesaj buraya {saat} tarihinde gonderildi."
# Gmail ile bağlantı burada kuruluyor bkz. SMTP
mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
# Güvenli bağlantı için tls açtık.
mailServer.starttls()
# Mail adresi ve şifre ile hesaba giriş
mailServer.login(gmailaddress , gmailpassword)
# Maili burda gönderiyoruz
mailServer.sendmail(gmailaddress, mailto , f"Subject: {subject}\n{msg}")
# İş bittikten sonra çıkış yapmamız gerekiyor
mailServer.quit()