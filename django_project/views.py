from django.http import HttpResponse
import smtplib
import time

#timeout
def mailer(self):    
    tm = time.localtime()
    saat = time.strftime("%d-%m-20%y %H:%M", tm)
    gmailaddress = "refiksoyletmez@gmail.com"
    gmailpassword = ""
    #mailto = "refiksoyletmez@gmail.com","osmannes53@gmail.com"
    mailto = """
    batihan.ozdemir@turkiyeteknolojitakimi.org
    rumeysa.guc@turkiyeteknolojitakimi.org
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
    subject = "Yukselen Yildiz Bilisim Koordinatorlugu Bulteni"
    msg = f"Herkese selamlar cron-job ekibi tarafindan olusturulan haftalik bultene hos geldiniz\n Son yenilikler: Artik server herkese acik erorising.herokuapp.com uzerinden erisebilirsiniz. \nBunu goruyorsaniz bana haber verin plz {saat} tarihinde gonderildi."
    mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
    mailServer.starttls()
    mailServer.login(gmailaddress , gmailpassword)
    mailServer.sendmail(gmailaddress, mailto , f"Subject: {subject}\n{msg}")
    mailServer.quit()
    return HttpResponse("""
    <html><script>alert("Mail gönderildi!");</script>
    <head><meta http-equiv="refresh" content="4; url='https://giphy.com/stickers/cindysuenkeys-l3V0bpnfbQ3Ygpup2/fullscreen'" /></head></html>""")