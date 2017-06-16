# -*- coding: utf-8 -*-

import smtplib
import sys


address= sys.argv.pop(1)
text1= sys.argv.pop(1)
text2 = sys.argv.pop(1)


t1=" Ho! Ho! Ho! <br><br><br> Świeta już za pasem, a tu by się przydało jakieś" \
    " prezenciory wybrać, nieprawdaż? <br> Jako iż w tym roku zrobiliśmy" \
    " małe losowanie, czas ogłosić wyniki!!!<br><br>"\
    "W tym roku tajnie i niejawnie wytypowano, że będziesz Światecznym"\
    " Dobrodziejem / Dziadkiem Mrozem / Gwiazdorem / Mikołajem (itd..itp.. niepotrzebne skreslić)"\
    " dla następujących osób:<br><br>"

#t1="Ho! Ho! Ho! <br><br><br> Gwiazdor stary już jest, i omylny. Pojedwabiły mu się listy od grzecznej "\
#    "i niegrzecznej dziatwy, a co za tym idzie - LOSOWANIE ZOSTAŁO ANULOWANE!<br><br><br>"\
#    "Niemniej nie zasypując gruszek w popiele od razu zabrał się do porządków i rozpisał nowe listy. "\
#    "Tym razem Twoją fuchą będzie bycie Światecznym Dobrodziejem / Dziadkiem Mrozem / Gwiazdorem /  "\
#    "Mikołajem (itd..itp.. niepotrzebne skreslić) dla następujących osób:<br><br>"
t2="<br><br>Jak już wspomniane było - zacznij się nad podarunkami zastanawiać! <br>"\
    "Azaliż ażeby by sportowe fair-play wprowadzić - pamiętaj, że masz TYLKO dwa miejsca pod choinką!!!"\
    "<br><br>Mokrego karpia i smacznego śniegu!"\
    "<br><br><br>P.S. Pamiętaj!! Nie jedz żółtego śniegu!!!"

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'gwiazdor.rakow.2012@gmail.com'
recipient = address
subject = 'Prezenciory!!!'
body = t1+text1+'<br>'+text2+'<br>'+t2


body = "" + body + ""

headers = ["From: " + sender,
           "Subject: " + subject,
           "To: " + recipient,
           "MIME-Version: 1.0",
           "Content-Type: text/html"]
headers = "\r\n".join(headers)

session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

session.ehlo()
session.starttls()
session.ehlo
session.login('gwiazdor.rakow.2012', 'gwiazdor.skasujkropka')

session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
session.quit()
