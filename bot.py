import requests
import json
import os
import re 
import time
from datetime import datetime
from dotenv import load_dotenv

# 1. تفعيل قراءة ملف .env
load_dotenv()

token = os.getenv("TOKEN")
admin_id_env = os.getenv("ADMIN_ID")
admin = int(admin_id_env) if admin_id_env else 0

# 2. تعريف الدالة أولاً لكي يتعرف عليها البوت
def load_json(path, default_value=None):
    if default_value is None: default_value = {}
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except: return default_value
    return default_value

# 3. إنشاء المجلد
def handle_update(chat_id, from_id, text, data, message_id, res_msg, cleaner):
    global xmax, carlos, members, groups, XQ_3X, last_update_id
    # هنا تبدأ الـ 2000 سطر الخاصة بك

    # هنا تبدأ كل أوامرك الـ 2000 سطر
    # (يجب أن تضغط Tab لكل الأسطر التي تليها لتصبح داخل هذه الدالة)



if not os.path.exists("data"): 
    os.makedirs("data")

# 4. الآن نقوم بتحميل البيانات بأمان (بعد تعريف الدالة)
xmax = load_json("data/xmax.json", {"cleaner": {}})
carlos = load_json("data/carlos.json", {"admin": [], "ban": [], "ok": "no"})
data_members = load_json("data/members.json", {"members_list": []})
members = data_members.get("members_list", [])
data_groups = load_json("data/groups.json", {"groups_list": []})
groups = data_groups.get("groups_list", [])

API_KEY = token


# تحميل البيانات عند التشغيل
# 1. تعريف الدالة بشكل سليم
def load_json(path, default_value=None):
    if default_value is None: default_value = {}
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except: return default_value
    return default_value

# 2. إنشاء المجلد مرة واحدة
if not os.path.exists("data"): 
    os.makedirs("data")

# 3. تحميل البيانات (بدون تكرار وبقيم افتراضية آمنة)

# تحميل بيانات الإعدادات (مع ضمان وجود قائمة الأدمن والمحظورين)
carlos = load_json("data/carlos.json", {"admin": [], "ban": [], "ok": "no"})

# تحميل بيانات الأعضاء (مرة واحدة فقط)
data_members = load_json("data/members.json", {"members_list": []})
members = data_members.get("members_list", [])

# تحميل بيانات المجموعات
data_groups = load_json("data/groups.json", {"groups_list": []})
groups = data_groups.get("groups_list", [])
# تحميل بيانات المنظف بشكل آمن
# تأكد أن هذا في بداية الملف تماماً
data_xmax = load_json("data/xmax.json", {"cleaner": {}})
xmax = data_xmax




XQ_3X = {
    "sand": "اليك قسم الإذاعة 📢",
    "sand1": "ارسل نص الاذاعة للخاص 💬",
    "sand2": "جاري الارسال للخاص...",
    "sand3": "ارسل نص الاذاعة للمجموعات 👥",
    "sand4": "جاري الارسال للمجموعات...",
    "sand5": "ارسل نص الاذاعة للكل 🌐",
    "sand6": "جاري الارسال للجميع...",
    "sand7": "ارسل التوجيه للكل 🔄",
    "sand8": "جاري توجيه الرسالة للكل...",
    "sand9": "ارسل التوجيه للخاص 👤",
    "sand10": "جاري التوجيه للخاص...",
    "sand11": "ارسل التوجيه للمجموعات 👥",
    "sand12": "جاري التوجيه للمجموعات...",
    "start": "اهلا بك في بوت التواصل 🤖"
}


# إعداد الـ Webhook (يتم تنفيذه عادةً مرة واحدة)
# requests.get(f"https://api.telegram.org/bot{API_KEY}/setwebhook?url=YOUR_URL")

def bot(method, datas=None):
    if datas is None:
        datas = {}
    url = f"https://api.telegram.org/bot{API_KEY}/{method}"
    try:
        response = requests.post(url, data=datas)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Error: {e}")
    return None

def SendChatAction(chat_id, action):
    return bot('sendChatAction', {
        'chat_id': chat_id,
        'action': action
    })

def SendMessage(chat_id, text, parse_mode="MARKDOWN", disable_web_page_preview=True, reply_to_message_id=None, reply_markup=None):
    return bot('sendMessage', {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': parse_mode,
        'disable_web_page_preview': disable_web_page_preview,
        'disable_notification': False,
        'reply_to_message_id': reply_to_message_id,
        'reply_markup': reply_markup
    })

# --- (carlos) --- #
if not os.path.exists("data"):
    os.makedirs("data")

# ملاحظة: في بايثون، يتم استقبال التحديثات 'update' كقاموس (Dictionary) 
# سنقوم هنا بترجمة منطق استخراج المتغيرات حرفياً كما في الأصل

def process_update(update_dict):
    # تحويل القاموس إلى كائن لتسهيل الوصول (اختياري) أو التعامل معه مباشرة
    # سنقوم هنا بالتعامل مع المتغيرات بناءً على هيكلية التحديث
    
    message = update_dict.get('message')
    callback_query = update_dict.get('callback_query')
    edited_message = update_dict.get('edited_message')
    channel_post = update_dict.get('channel_post')
    edited_channel_post = update_dict.get('edited_channel_post')
    inline_query = update_dict.get('inline_query')
    chosen_inline_result = update_dict.get('chosen_inline_result')

    # تهيئة المتغيرات العامة
    message_id = None
    username = None
    chat_id = None
    title = None
    text = None
    user = None
    name = None
    from_id = None
    data = None
    query = None

    if message:
        message_id = message.get('message_id')
        username = message.get('from', {}).get('username')
        chat_id = message.get('chat', {}).get('id')
        title = message.get('chat', {}).get('title')
        text = message.get('text')
        user = username
        name = message.get('from', {}).get('first_name')
        from_id = message.get('from', {}).get('id')

    if callback_query:
        data = callback_query.get('data')
        chat_id = callback_query.get('message', {}).get('chat', {}).get('id')
        title = callback_query.get('message', {}).get('chat', {}).get('title')
        message_id = callback_query.get('message', {}).get('message_id')
        name = callback_query.get('message', {}).get('chat', {}).get('first_name')
        user = callback_query.get('message', {}).get('chat', {}).get('username')
        from_id = callback_query.get('from', {}).get('id')

    if edited_message:
        message = edited_message
        message_id = message.get('message_id')
        username = message.get('from', {}).get('username')
        chat_id = message.get('chat', {}).get('id')
        text = message.get('text')
        user = username
        name = message.get('from', {}).get('first_name')
        from_id = message.get('from', {}).get('id')

    if channel_post:
        message = channel_post
        message_id = message.get('message_id')
        chat_id = message.get('chat', {}).get('id')
        text = message.get('text')
        user = message.get('chat', {}).get('username')
        title = message.get('chat', {}).get('title')
        name = message.get('author_signature')
        from_id = message.get('chat', {}).get('id')

    if edited_channel_post:
        message = edited_channel_post
        message_id = message.get('message_id')
        chat_id = message.get('chat', {}).get('id')
        text = message.get('text')
        user = message.get('chat', {}).get('username')
        name = message.get('author_signature')
        from_id = message.get('chat', {}).get('id')

    if inline_query:
        inline = inline_query
        message = inline
        user = inline.get('from', {}).get('username')
        name = inline.get('from', {}).get('first_name')
        from_id = inline.get('from', {}).get('id')
        query = inline.get('query')
        text = query

    if chosen_inline_result:
        message = chosen_inline_result
        user = message.get('from', {}).get('username')
        name = message.get('from', {}).get('first_name')
        from_id = message.get('from', {}).get('id')
        inline_message_id = message.get('inline_message_id')
        message_id = inline_message_id
        text = message.get('query')
        query = text

    # --- (استخراج البيانات المتقدمة) --- #
    tc = message.get('chat', {}).get('type') if message and 'chat' in message else None
    re = message.get('reply_to_message') if message else None
    
    re_id = None
    re_user = None
    re_name = None
    re_messagid = None
    re_chatid = None

    if re:
        re_id = re.get('from', {}).get('id')
        re_user = re.get('from', {}).get('username')
        re_name = re.get('from', {}).get('first_name')
        re_messagid = re.get('message_id')
        re_chatid = re.get('chat', {}).get('id')

    photo = message.get('photo') if message else None
    video = message.get('video') if message else None
    sticker = message.get('sticker') if message else None
    file = message.get('document') if message else None
    audio = message.get('audio') if message else None
    voice = message.get('voice') if message else None
    caption = message.get('caption') if message else None

    # قراءة الملفات النصية
    def get_file_content(path):
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return f.read()
        return ""

    mmur = get_file_content("murt.txt")
    mmurt = get_file_content("channel.txt")

    # استخراج الـ IDs للمرفقات
    photo_id = photo[-1].get('file_id') if photo else None
    video_id = video.get('file_id') if video else None
    sticker_id = sticker.get('file_id') if sticker else None
    file_id = file.get('file_id') if file else None
    music_id = audio.get('file_id') if audio else None

    # التوجيه (Forward)
    forward = message.get('forward_from_chat') if message else None
    forward_id = message.get('forward_from_chat', {}).get('id') if message else None
    
    forward_type = None
    forward_name = None
    forward_user = None
    forward_title = None

    if re:
        fwd = re.get('forward_from', {})
        forward_type = fwd.get('type')
        forward_name = fwd.get('first_name')
        forward_user = fwd.get('username')
    elif message:
        fwd = message.get('forward_from', {})
        forward_type = fwd.get('type')
        forward_name = fwd.get('first_name')
        forward_user = fwd.get('username')
        forward_id = fwd.get('id')
        if forward_name is None:
            fwd_chat = message.get('forward_from_chat')
            if fwd_chat:
                forward_id = fwd_chat.get('id')
                forward_title = fwd_chat.get('title')

    # المنشن والحالة
    name_tag = f"[{name}](tg://user?id={from_id})"
    statjson = bot('getChatMember', {'chat_id': chat_id, 'user_id': from_id})
    status = statjson.get("result", {}).get("status") if statjson else None

    # --- (نهاية الجزء الأول) --- #





# --- (تحميل ملفات البيانات) --- #

def load_data(path):
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_data(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        # استخدام indent=4 و ensure_ascii=False لمحاكاة (32|128|265) في PHP
        json.dump(data, f, ensure_ascii=False, indent=4)

# المتغير $web يجب أن يكون معرفاً مسبقاً في الكود
web = "data/web.json" # افتراض المسار بناءً على السياق

carlos = load_data("data/carlos.json")
xmax = load_data("data/bot.json")
chat = load_data("data/chat.json")
sttings = load_data("data/media.json")
meca = load_data("data/members.json")
em = load_data("data/em.json")
iinfo = load_data(web)

# --- (ضبط القيم الافتراضية لـ carlos) --- #

keys_to_check = {
    "gch": "❎",
    "d6": "❎",
    "bot": "✅",
    "d7": "❎"
}

for key, default_val in keys_to_check.items():
    if carlos.get(key) is None:
        carlos[key] = default_val
        save_data("data/carlos.json", carlos)

# --- (إعدادات namezar و urlzar) --- #

if iinfo.get('namezar') is None:
    namezar = "𝗦𝘂𝗿𝘀 𝗫!𝗠𝗮𝗅"
else:
    namezar = iinfo['namezar']

if iinfo.get('urlzar') is None:
    urlzar = "https://t.me/OC_C3"
else:
    urlzar = iinfo['urlzar']

xch = carlos.get("ch")
xcch = carlos.get("cch")
# chat_id يجب أن يكون مستخرجاً من التحديث (Update) كما في الجزء الأول
# نضمن أولاً أن xmax قاموس قبل طلب get منه
# استبدل السطر 337 بهذا بالكامل:
# هذا السطر ذكي لأنه يفحص وجود المتغير قبل استخدامه
if 'xmax' in globals() or 'xmax' in locals():
    
else:
    # إذا لم يجد المتغير، يقوم بتعريفه فوراً كقاموس فارغ لمنع الانهيار
    xmax = {"cleaner": {}}
    cleaner = None



# --- (الإحصائيات والمتغيرات) --- #

members = meca.get("members", [])
groups = meca.get("group", [])
id_admin = carlos.get("admin", [])

md3 = len(meca.get("members", []))
md5 = len(meca.get("group", []))
countall = md5 + md3
# حساب المحظورين
md4 = len(meca.get("banbots", [])) - 1

# إضافة عضو جديد في الخاص
if tc == "private" and from_id not in members:
    if "members" not in meca:
        meca["members"] = []
    meca["members"].append(from_id)
    save_data("data/members.json", meca)

# --- (منطق المجموعات) --- #

# جلب عدد أعضاء المجموعة الحالية
chat_member_count_res = bot("getChatMemberCount", {"chat_id": chat_id})
addgroup = chat_member_count_res.get("result") if chat_member_count_res else 0

# اسم المجموعة من التحديث
namegroup = title # تم استخراجه في الجزء الأول كـ $title

if text and chat_id not in groups:
    if tc != "private":
        # إرسال إشعار للمطور عند تفعيل البوت في مجموعة جديدة
        bot("sendMessage", {
            "chat_id": Df,
            "text": f"*‹ : تم تفعيل مجموعه جديده *\n"
                    f"*‹ : من قام بتفعيلها :* {name} \n"
                    f"*‹ : معلومات المجموعه :*\n"
                    f"*‹ : الاسم :* {namegroup}\n"
                    f"*‹ : عدد الاعضاء :* {addgroup}\n"
                    f"*‹ : جميع الاحصائيات :* {countall}",
            "parse_mode": "Markdown"
        })
        if "group" not in meca:
            meca["group"] = []
        meca["group"].append(chat_id)
        save_data("data/members.json", meca)

# --- (منطق طرد البوت من المجموعة) --- #

left_member = message.get('left_chat_member') if message else None
idleft = left_member.get('id') if left_member else None

# جلب ايدي البوت
get_me_res = bot("getMe")
idbot = get_me_res.get("result", {}).get("id") if get_me_res else None

if idleft and idleft == idbot:
    bot("sendMessage", {
        "chat_id": Df,
        "text": f"*‹ :  تم طرد البوت من مجموعه جديده *\n"
                f"*‹ :  اسم المجموعه :* {namegroup}\n"
                f"*‹ :  ايدي المجموعه :* {chat_id}\n"
                f"*‹ :  تم مسح جميع البيانات المتعلقه بالمجموعه*",
        "parse_mode": "MarkDown"
    })
    if chat_id in meca.get("group", []):
        meca["group"].remove(chat_id)
        save_data("data/members.json", meca)

# --- (تتبع التفاعل اليومي) --- #

dd = datetime.now().strftime("%a") # جلب اليوم (مثلاً: Mon, Tue)
if dd not in em:
    em[dd] = []

em1 = len(em[dd])
em2 = em[dd]

if message and from_id not in em2:
    em[dd].append(from_id)
    save_data("data/em.json", em)

# --- (تحديد المطور/الأدمن الأساسي) --- #

if not carlos.get("sudo"):
    iidsod = Df
else:
    iidsod = carlos["sudo"]

admin = iidsod





# --- (إعداد النصوص والرسائل) --- #

tag_name = f"[{name}](tg://user?id={from_id})"

# التحقق من نص رسالة الترحيب
if carlos.get("start") is None:
    start_msg = "*اهلأ بك عزيزي في بوت تواصل المطور*"
else:
    start_msg = carlos["start"]

# قاموس النصوص XQ_3X (مطابق للأصل 100%)
# ملاحظة: المتغيرات مثل countall, md3 وغيرها يجب أن تكون معرفة من الأجزاء السابقة
XQ_3X = {
    "start": start_msg,
    "admin": "*• اهلا بك في لوحه الأدمن الخاصه بالبوت*\n-* يمكنك التحكم في البوت الخاص بك من هنا*\n⎯ ⎯ ⎯ ⎯",
    "off": "⚙- *عذرأ عزيزي حاليأ البوت معطل لتحديثات جديدة*",
    "ban": "⚠️- *عذرأ عزيزي لقد قام المطور بحظرك من هاذ البوت*",
    "sand": f"- عدد المستخدمين الكلي : {countall}\n- عدد الخاص : {md3}\n- عدد القنوات و الكروبات : {md5}\n- عدد التفاعل اليومي : {em1}\n- عدد المحظورين : {md4}\n⎯ ⎯ ⎯ ⎯",
    "sand1": f"{klisaamr}*أرسل رسالتك وسيتم إرسالها لـ {md3} من الاعضاء .* ",
    "sand2": f"{klisaamr}*تم ارسأل رسالتك لـ {md3} من الاعضاء .* ",
    "sand3": f"{klisaamr}*ارسأل رسالتك وسيتم ارسالها لـ {md5} من الكروبات .* ",
    "sand4": f"{klisaamr}*تم ارسأل رسالتك لـ {md5} من الكروبات .* ",
    "sand5": f"{klisaamr}*ارسأل رسالتك وسيتم ارسالها لـ {countall} من الاعضاء و الكروبات .* ",
    "sand6": f"{klisaamr}*تم ارسأل رسالتك لـ {countall} من الاعضاء و الكروبات .* ",
    "sand7": f"{klisaamr}*ارسأل رسالتك وسيتم توجيه لـ {countall} من الاعضاء و الكروبات .* ",
    "sand8": f"{klisaamr}*تم توجيه رسالتك لـ {countall} من الاعضاء و الكروبات .* ",
    "sand9": f"{klisaamr}*أرسل رسالتك وسيتم توجيه لـ {md3} من الاعضاء .* ",
    "sand10": f"{klisaamr}*تم توجيه رسالتك لـ {md3} من الاعضاء .* ",
    "sand11": f"{klisaamr}*ارسأل رسالتك وسيتم توجيه لـ {md5} من الكروبات .* ",
    "sand12": f"{klisaamr}*تم توجيه رسالتك لـ {md5} من الكروبات .* "
}

# --- (منطق تعطيل البوت) --- #

if message and carlos.get("bot") == "❎" and from_id != int(admin):
    bot("sendMessage", {
        "chat_id": chat_id,
        "text": XQ_3X["off"],
        "parse_mode": "Markdown",
        "reply_to_message_id": message_id
    })
    # في بايثون نستخدم return لإنهاء تنفيذ الدالة الحالية بدلاً من exit()
    # return 

# --- (التوجيه التلقائي للمطور) --- #

if message and text != "/start" and from_id != int(admin) and carlos.get("d7") == "✅" and not data and from_id not in carlos.get("ban", []):
    bot("forwardMessage", {
        "chat_id": admin,
        "from_chat_id": chat_id,
        "message_id": message_id
    })

# --- (إشعار دخول عضو جديد) --- #

if user is None or user == "":
    display_user = "None"
else:
    display_user = f"[@{user}]"

if text == "/start" and from_id != int(admin) and carlos.get("d6") == "✅" and from_id not in members and from_id not in carlos.get("ban", []):
    bot("sendMessage", {
        "chat_id": admin,
        "text": f"تم دخول عضو جديد الى البوت :\n"
                f"الاسم : [{name}]\n"
                f"المعرف : {display_user}\n"
                f"الايدي : [{from_id}](tg://user?id={from_id})\n"
                f"⎯ ⎯ ⎯ ⎯\n"
                f"عدد المستخدمين : {md3}",
        "parse_mode": "Markdown"
    })

# --- (منطق الاشتراك الإجباري - Force Join) --- #

tokenmas = info.get('tokenmas') # توكن بوت الحماية أو المساعد
idchb_list = [iinfo.get('dchb'), iinfo.get('chb')] # القنوات المحددة

for channel_id in idchb_list:
    if channel_id and message:
        # فحص العضوية عبر API تليجرام
        check_url = f"https://api.telegram.org/bot{tokenmas}/getChatMember?chat_id={channel_id}&user_id={from_id}"
        try:
            check_res = requests.get(check_url).text
            # محاكاة strpos في PHP للبحث عن الحالات التي تمنع المستخدم
            if '"status":"left"' in check_res or "USER_ID_INVALID" in check_res or '"status":"kicked"' in check_res:
                if tc == "private":
                    clean_ch = channel_id.replace("@", "")
                    # جلب معلومات القناة
                    get_ch = requests.get(f"https://api.telegram.org/bot{tokenmas}/getChat?chat_id={channel_id}").json()
                    namech = get_ch.get("result", {}).get("title", "القناة")
                    
                    bot('sendMessage', {
                        'chat_id': chat_id,
                        'text': f"*‹ : عزيزي عليك الاشتراك في قناة .*\n"
                                f"*‹ : ليمكنك استخدام البوت دون اي مشكلة .*\n"
                                f"‹ : [{namech}](t.me/{clean_ch})\n"
                                f"*‹ : بعد الاشتراك اضغط :* /start",
                        'reply_to_message_id': message_id,
                        'parse_mode': 'MarkDown',
                        'disable_web_page_preview': True,
                        'reply_markup': json.dumps({
                            'inline_keyboard': [[{'text': namech, 'url': f"https://t.me/{clean_ch}"}]]
                        })
                    })
                    # توقف عن تنفيذ بقية الأوامر (مثل return false في PHP)
                    # return 
        except:
            pass




# --- (نظام الاشتراك الإجباري - القنوات الأربعة) --- #

# 1. القناة الأولى (عامة)
ch11 = carlos.get('ch1')
if ch11 and message:
    check_ch1 = requests.get(f"https://api.telegram.org/bot{API_KEY}/getChatMember?chat_id={ch11}&user_id={from_id}").text
    if '"status":"left"' in check_ch1 or "USER_ID_INVALID" in check_ch1 or '"status":"kicked"' in check_ch1:
        if tc == "private":
            clean_ch = str(ch11).replace("@", "")
            get_ch = requests.get(f"http://api.telegram.org/bot{API_KEY}/getChat?chat_id={ch11}").json()
            namech = get_ch.get('result', {}).get('title', 'قناة البوت')
            bot('sendMessage', {
                'chat_id': chat_id,
                'text': f"⚠️- عذراً عزيزي \n⚙- يجب عليك الاشتراك في قنوات البوت أولا\n📮- اشترك ثم ارسل /start ⬇️\n[{namech}](t.me/{clean_ch})\n— — — — — — — — —",
                'reply_to_message_id': message_id,
                'parse_mode': "MarkDown",
                'disable_web_page_preview': True,
                'reply_markup': json.dumps({
                    'inline_keyboard': [[{'text': "اشتراك ⚠️", 'url': f"https://t.me/{clean_ch}"}]]
                })
            })
            # return False # إيقاف التنفيذ

# 2. القناة الثانية (عامة)
ch22 = carlos.get('ch2')
if ch22 and message:
    check_ch2 = requests.get(f"https://api.telegram.org/bot{API_KEY}/getChatMember?chat_id={ch22}&user_id={from_id}").text
    if '"status":"left"' in check_ch2 or "USER_ID_INVALID" in check_ch2 or '"status":"kicked"' in check_ch2:
        if tc == "private":
            clean_ch = str(ch22).replace("@", "")
            get_ch = requests.get(f"http://api.telegram.org/bot{API_KEY}/getChat?chat_id={ch22}").json()
            namech = get_ch.get('result', {}).get('title', 'قناة البوت')
            bot('sendMessage', {
                'chat_id': chat_id,
                'text': f"⚠️  عذراً عزيزي \n⚙  يجب عليك الاشتراك في قنوات البوت أولا\n📮  اشترك ثم ارسل /start ⬇️\n[{namech}](t.me/{clean_ch})\n — — — — — — — — —",
                'reply_to_message_id': message_id,
                'parse_mode': "MarkDown",
                'disable_web_page_preview': True,
                'reply_markup': json.dumps({
                    'inline_keyboard': [[{'text': "اشتراك ⚠️", 'url': f"https://t.me/{clean_ch}"}]]
                })
            })
            # return False

# 3. القناة الثالثة (خاصة برابط)
ch111 = carlos.get('ch1p')
if ch111 and message:
    check_chp = requests.get(f"https://api.telegram.org/bot{API_KEY}/getChatMember?chat_id={ch111}&user_id={from_id}").text
    if '"status":"left"' in check_chp or '"status":"kicked"' in check_chp or "USER_ID_INVALID" in check_chp:
        if tc == "private":
            get_ch = requests.get(f"http://api.telegram.org/bot{API_KEY}/getChat?chat_id={ch111}").json()
            namech = get_ch.get('result', {}).get('title', 'قناة البوت')
            chi = carlos.get('ch1pp') # الرابط الخاص
            bot('sendMessage', {
                'chat_id': chat_id,
                'text': f"⚠️  عذراً عزيزي \n⚙  يجب عليك الاشتراك في قنوات البوت أولا\n📮  اشترك ثم ارسل /start ⬇️\n[{namech}](t.me/{chi})\n — — — — — — — — —\n",
                'reply_to_message_id': message_id,
                'parse_mode': "MarkDown",
                'disable_web_page_preview': True,
                'reply_markup': json.dumps({
                    'inline_keyboard': [[{'text': "اشتراك ⚠️", 'url': chi}]]
                })
            })
            # return False

# 4. القناة الرابعة (خاصة برابط)
ch222 = carlos.get('ch2p')
if ch222 and message:
    check_ch2p = requests.get(f"https://api.telegram.org/bot{API_KEY}/getChatMember?chat_id={ch222}&user_id={from_id}").text
    if '"status":"left"' in check_ch2p or "USER_ID_INVALID" in check_ch2p or '"status":"kicked"' in check_ch2p:
        if tc == "private":
            get_ch = requests.get(f"http://api.telegram.org/bot{API_KEY}/getChat?chat_id={ch222}").json()
            namech = get_ch.get('result', {}).get('title', 'قناة البوت')
            chi = carlos.get('ch2pp') # الرابط الخاص
            bot('sendMessage', {
                'chat_id': chat_id,
                'text': f"⚠️  عذراً عزيزي \n⚙  يجب عليك الاشتراك في قنوات البوت أولا\n📮  اشترك ثم ارسل /start ⬇️\n[{namech}](t.me/{chi})\n — — — — — — — — —\n",
                'reply_to_message_id': message_id,
                'parse_mode': "MarkDown",
                'disable_web_page_preview': True,
                'reply_markup': json.dumps({
                    'inline_keyboard': [[{'text': "اشتراك ⚠️", 'url': chi}]]
                })
            })
            # return False

# --- (منطق المحظورين من البوت) --- #

if message and from_id in carlos.get("ban", []):
    bot("sendMessage", {
        "chat_id": chat_id,
        "text": XQ_3X["ban"],
        "parse_mode": "Markdown",
        "reply_to_message_id": message_id
    })
    # return # إيقاف التنفيذ

# --- (نظام الحظر وإلغاء الحظر من قبل المطور) --- #

# استخراج ايدي الشخص المراد حظره من التوجيه (Reply)
ban_id = None
if message and message.get('reply_to_message') and message['reply_to_message'].get('forward_from'):
    ban_id = message['reply_to_message']['forward_from'].get('id')

# 1. تنفيذ الحظر
if ban_id and text == "حظر":
    if from_id in id_admin or from_id == int(admin):
        res = bot("getChat", {"chat_id": ban_id})
        if res and res.get('ok'):
            banname = res['result'].get('first_name')
            bot("sendMessage", {
                "chat_id": chat_id,
                "text": f"⋄︙العضو - [{banname}](tg://user?id={ban_id})\n⋄︙تم حـظـرهه بـنـجاح",
                "parse_mode": "Markdown",
                "reply_to_message_id": message_id
            })
            if "ban" not in carlos:
                carlos["ban"] = []
            if str(ban_id) not in carlos["ban"]:
                carlos["ban"].append(str(ban_id))
                save_data("data/carlos.json", carlos)

# 2. تنفيذ إلغاء الحظر
if ban_id and text == "الغاء حظر":
    if from_id in id_admin or from_id == int(admin):
        res = bot("getChat", {"chat_id": ban_id})
        if res and res.get('ok'):
            banname = res['result'].get('first_name')
            bot("sendMessage", {
                "chat_id": chat_id,
                "text": f"\n⋄︙العضو - [{banname}](tg://user?id={ban_id})\n⋄︙تم الـغـاء حـظـرهه بـنـجاح\n",
                "parse_mode": "Markdown",
                "reply_to_message_id": message_id
            })
            if str(ban_id) in carlos.get("ban", []):
                carlos["ban"].remove(str(ban_id))
                save_data("data/carlos.json", carlos)



# --- (إعداد مسميات الأزرار) --- #
n = len(json_data.get("nas", [])) if 'json_data' in locals() else 0

ahs = "الاحصائيات"
cahadd = "الاشتراك"
staadd = "رساله الترحيب (start)"
admadd = "قسم الادمنية"
naadd = "الاذاعة"
nsadd = "قسم النسخة"
banamradd = "قسم المحظورين"

# --- (جلب حالة الإعدادات الحالية) --- #
d6 = carlos.get("d6")
d7 = carlos.get("d7")
bot2 = carlos.get("bot")

# --- (دالة إنشاء لوحة التحكم لتجنب التكرار) --- #
def get_admin_keyboard(bot_stat, dev_stat, notify_stat):
    return json.dumps({
        "inline_keyboard": [
            [
                {"text": f"البوت {bot_stat}", "callback_data": "bot3"},
                {"text": f"التوجية {dev_stat}", "callback_data": "d7"},
                {"text": f"الاشعارات {notify_stat}", "callback_data": "d6"}
            ],
            [{"text": staadd, "callback_data": "4"}],
            [{"text": nsadd, "callback_data": "Open"}, {"text": "نقل الملكية", "callback_data": "AddAdmin"}],
            [{"text": naadd, "callback_data": "10"}, {"text": ahs, "callback_data": "1"}, {"text": cahadd, "callback_data": "All Ch"}],
            [{"text": banamradd, "callback_data": "lastban"}, {"text": admadd, "callback_data": "5"}],
        ]
    })

# --- (أمر البداية للأدمن /start) --- #
if text == "/start":
    if from_id in id_admin or from_id == int(admin):
        # تحديث الحالات قبل العرض
        d6 = carlos.get("d6")
        d7 = carlos.get("d7")
        bot2 = carlos.get("bot")
        
        bot("sendMessage", {
            "chat_id": chat_id,
            "text": XQ_3X["admin"],
            "parse_mode": "Markdown",
            "reply_to_message_id": message_id,
            "reply_markup": get_admin_keyboard(bot2, d7, d6)
        })

# --- (زر العودة للخلف back) --- #
if data == "back":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": XQ_3X["admin"],
            "parse_mode": "Markdown",
            "reply_markup": get_admin_keyboard(bot2, d7, d6)
        })
        # إغلاق الحالات المؤقتة عند العودة
        carlos["addfiles"] = "off"
        carlos["Openstengs"] = "off"
        carlos["ok"] = "no"
        save_data("data/carlos.json", carlos)

# --- (تغيير حالة الإشعارات d6) --- #
if data == "d6":
    if from_id in id_admin or from_id == int(admin):
        # تبديل الحالة بين صح وخطأ
        carlos["d6"] = "✅" if carlos.get("d6") != "✅" else "❎"
        save_data("data/carlos.json", carlos)
        
        # تحديث الأزرار في نفس الرسالة
        bot("editMessageReplyMarkup", {
            "chat_id": chat_id,
            "message_id": message_id,
            "reply_markup": get_admin_keyboard(carlos["bot"], carlos["d7"], carlos["d6"])
        })

# --- (تغيير حالة التوجيه d7) --- #
if data == "d7":
    if from_id in id_admin or from_id == int(admin):
        # تبديل الحالة بين صح وخطأ
        carlos["d7"] = "✅" if carlos.get("d7") != "✅" else "❎"
        save_data("data/carlos.json", carlos)
        
        # تحديث الأزرار في نفس الرسالة
        bot("editMessageReplyMarkup", {
            "chat_id": chat_id,
            "message_id": message_id,
            "reply_markup": get_admin_keyboard(carlos["bot"], carlos["d7"], carlos["d6"])
        })

# --- (تغيير حالة البوت bot3) --- #
if data == "bot3":
    if from_id in id_admin or from_id == int(admin):
        # تبديل حالة تشغيل/تعطيل البوت
        carlos["bot"] = "✅" if carlos.get("bot") != "✅" else "❎"
        save_data("data/carlos.json", carlos)
        
        # تحديث الأزرار في نفس الرسالة
        bot("editMessageReplyMarkup", {
            "chat_id": chat_id,
            "message_id": message_id,
            "reply_markup": get_admin_keyboard(carlos["bot"], carlos["d7"], carlos["d6"])
        })






# --- (نظام نقل ملكية البوت / إضافة مطور جديد) --- #

# عند الضغط على زر "نقل الملكية"
if data == "AddAdmin":
    if from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "‼ ارسل الان ايدي المطور الجديد ✅",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "🔙", "callback_data": "back"}]]
            })
        })
        # حفظ الحالة لانتظار استقبال الأيدي من الرسالة القادمة
        carlos["data"] = "Addadmin"
        save_data("data/carlos.json", carlos)

# استقبال الأيدي (التحقق من أن النص عبارة عن أرقام فقط)
if text and re.match(r"^[0-9]+$", str(text)):
    if carlos.get("data") == "Addadmin" and from_id == int(admin):
        # تأكيد النقل للأدمن الحالي
        bot("sendMessage", {
            "chat_id": chat_id,
            "text": "تم رفع الادمن وتم التنزيل ✅",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "🔙", "callback_data": "back"}]]
            })
        })
        # إرسال رسالة للمطور الجديد لإعلامه
        bot("sendMessage", {
            "chat_id": text,
            "text": "✔ تم رفعك ادمن بالبوت"
        })
        # تحديث قيمة المطور الأساسي (sudo) وإلغاء حالة الانتظار
        carlos["sudo"] = str(text)
        if "data" in carlos:
            del carlos["data"]
        save_data("data/carlos.json", carlos)

# --- (قسم إدارة الاشتراك الإجباري - الواجهة الرئيسية) --- #

if data == "All Ch":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "،🖇:اهلا بك في قسم الاشتراك الاجباري ",
            "reply_markup": json.dumps({
                "inline_keyboard": [
                    [{"text": "اضف قناة اولى", "callback_data": "AddCh1"}, {"text": "حذف القناة الولى", "callback_data": "DelCh1"}],
                    [{"text": "اضف قناة ثانيه", "callback_data": "AddCh2"}, {"text": "حذف القناة الثانيه", "callback_data": "DelCh2"}],
                    [{"text": " عرض قنوات الاشتراك العامة", "callback_data": "ALLCH"}],
                    [{"text": "⬆️ اعدادات القنوات العامة ⚙", "callback_data": "."}],
                    [{"text": "⬇️ اعدادات القنوات الخاصة ⚙", "callback_data": "."}],
                    [{"text": "اضف قناة اولى ", "callback_data": "AddCh1p"}, {"text": "حذف القناة الاولى ", "callback_data": "DelCh1p"}],
                    [{"text": "اضف قناة ثانية", "callback_data": "AddCh2p"}, {"text": "حذف القناة الثانية", "callback_data": "DelCh2p"}],
                    [{"text": "عرض قنوات الاشتراك الخاصه", "callback_data": "ALLCHp"}],
                    [{"text": "🔙", "callback_data": "back"}]
                ]
            })
        })

# --- (إدارة القناة الخاصة الأولى - إضافة) --- #

# الخطوة 1: طلب الأيدي
if data == "AddCh1p":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "،(،🖇:ارسل ايدي القناة -100)",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "🔙", "callback_data": "back"}]]
            })
        })
        carlos["data"] = "okch1p"
        save_data("data/carlos.json", carlos)

# الخطوة 2: استقبال الأيدي وطلب الرابط
if text and carlos.get("data") == "okch1p" and from_id == int(admin):
    bot("sendMessage", {
        "chat_id": chat_id,
        "text": "،🖇:تم اضافه القناة\n،🖇:قم بأرسال رابط القناة الخاصة",
        "reply_markup": json.dumps({
            "inline_keyboard": [[{"text": "🔙", "callback_data": "back"}]]
        })
    })
    carlos["ch1p"] = str(text)
    carlos["data"] = "addp1"
    save_data("data/carlos.json", carlos)

# الخطوة 3: استقبال الرابط وحفظه نهائياً
if text and carlos.get("data") == "addp1" and from_id == int(admin):
    bot("sendMessage", {
        "chat_id": chat_id,
        "text": "،🖇:تم اضافه القناة \n،🖇:قم برفع البوت مشرف",
        "reply_markup": json.dumps({
            "inline_keyboard": [[{"text": "🔙", "callback_data": "back"}]]
        })
    })
    carlos["ch1pp"] = str(text)
    carlos["data"] = "stop"
    save_data("data/carlos.json", carlos)

# --- (إدارة القناة الخاصة الأولى - حذف) --- #

if data == "DelCh1p":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "،🖇:هل أنت متأكد من أنك تريد حذف القناة ",
            "reply_markup": json.dumps({
                "inline_keyboard": [
                    [{"text": "الغاء", "callback_data": "back"}, {"text": "تأكيد", "callback_data": "OKDelCh1p"}]
                ]
            })
        })

if data == "OKDelCh1p":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "،🖇:تم حذف القناة الاولى من الإشتراك الإجباري",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "🔙", "callback_data": "back"}]]
            })
        })
        # حذف مفتاح القناة من القاموس
        if "ch1p" in carlos:
            del carlos["ch1p"]
        save_data("data/carlos.json", carlos)


# --- (إدارة القناة الخاصة الثانية - إضافة) --- #

# الخطوة 1: طلب أيدي القناة الخاصة الثانية
if data == "AddCh2p":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "(،🖇:ارسل ايدي القناة -100)",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "🔙", "callback_data": "back"}]]
            })
        })
        carlos["data"] = "okch2p"
        save_data("data/carlos.json", carlos)

# الخطوة 2: استقبال الأيدي وطلب الرابط الخاص
if text and carlos.get("data") == "okch2p" and from_id == int(admin):
    bot("sendMessage", {
        "chat_id": chat_id,
        "text": "،🖇:تم اضافه القناة \n،🖇:قم بأرسال رابط القناة الخاصة",
        "reply_markup": json.dumps({
            "inline_keyboard": [[{"text": "🔙", "callback_data": "back"}]]
        })
    })
    carlos["ch2p"] = str(text)
    carlos["data"] = "setaddp"
    save_data("data/carlos.json", carlos)

# الخطوة 3: استقبال الرابط وحفظه نهائياً
if text and carlos.get("data") == "setaddp" and from_id == int(admin):
    bot("sendMessage", {
        "chat_id": chat_id,
        "text": "،🖇:تم اضافه القناة\n،🖇:قم برفع البوت مشرف",
        "reply_markup": json.dumps({
            "inline_keyboard": [[{"text": "🔙", "callback_data": "back"}]]
        })
    })
    carlos["ch2pp"] = str(text)
    carlos["data"] = "stop"
    save_data("data/carlos.json", carlos)

# --- (إدارة القناة الخاصة الثانية - حذف) --- #

if data == "DelCh2p":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "،🖇:هل أنت متأكد من أنك تريد حذف القناة ",
            "reply_markup": json.dumps({
                "inline_keyboard": [
                    [{"text": "الغاء", "callback_data": "back"}, {"text": "تأكيد", "callback_data": "OKDelCh2p"}]
                ]
            })
        })

if data == "OKDelCh2p":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "،🖇:تم حذف القناة الاولى من الإشتراك الإجباري",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "🔙", "callback_data": "back"}]]
            })
        })
        if "ch2p" in carlos:
            del carlos["ch2p"]
        save_data("data/carlos.json", carlos)

# --- (عرض قنوات الاشتراك الخاص المعينة حالياً) --- #

if data == "ALLCHp":
    if from_id in id_admin or from_id == int(admin):
        ch1p_val = carlos.get("ch1p", "غير معينة")
        ch2p_val = carlos.get("ch2p", "غير معينة")
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": f"،🖇:هذه قائمة القنوات الأشتراك الاجباري \n،🖇:القناة الاولى {ch1p_val}\n،🖇:القناة الثانية  {ch2p_val}",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "🔙", "callback_data": "back"}]]
            })
        })

# --- (إدارة القناة العامة الأولى - إضافة) --- #

if data == "AddCh1":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "،🖇 ارسل معرف قناتك مع @",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "🔙", "callback_data": "back"}]]
            })
        })
        carlos["data"] = "okch1"
        save_data("data/carlos.json", carlos)

if text and carlos.get("data") == "okch1" and from_id == int(admin):
    bot("sendMessage", {
        "chat_id": chat_id,
        "text": f"،🖇:تم اضافه القناة [{text}]\n،🖇:قم برفع البوت ادمن في القناة",
        "reply_markup": json.dumps({
            "inline_keyboard": [[{"text": "🔙", "callback_data": "back"}]]
        })
    })
    carlos["ch1"] = str(text)
    carlos["data"] = "stop"
    save_data("data/carlos.json", carlos)

# --- (إدارة القناة العامة الأولى - حذف) --- #

if data == "DelCh1":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "،🖇:هل أنت متأكد من أنك تريد حذف القناة ",
            "reply_markup": json.dumps({
                "inline_keyboard": [
                    [{"text": "الغاء", "callback_data": "back"}, {"text": "تاكيد", "callback_data": "OKDelCh1"}]
                ]
            })
        })

if data == "OKDelCh1":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "،🖇:تم حذف القناة الاولى من الإشتراك الإجباري",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "🔙", "callback_data": "back"}]]
            })
        })
        if "ch1" in carlos:
            del carlos["ch1"]
        save_data("data/carlos.json", carlos)

# --- (إدارة القناة العامة الثانية - إضافة) --- #

if data == "AddCh2":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "،🖇 ارسل معرف قناتك مع @",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "??", "callback_data": "back"}]]
            })
        })
        carlos["data"] = "okch2"
        save_data("data/carlos.json", carlos)

if text and carlos.get("data") == "okch2" and from_id == int(admin):
    bot("sendMessage", {
        "chat_id": chat_id,
        "text": f"🖇:تم اضافه القناة [{text}]\n🖇:قم برفع البوت ادمن في القناة",
        "reply_markup": json.dumps({
            "inline_keyboard": [[{"text": "🔙", "callback_data": "back"}]]
        })
    })

    carlos["ch2"] = str(text)
    carlos["data"] = "stop"
    save_data("data/carlos.json", carlos)

# --- (إدارة القناة العامة الثانية - حذف) --- #

if data == "DelCh2":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "،🖇:هل أنت متأكد من أنك تريد حذف القناة ",
            "reply_markup": json.dumps({
                "inline_keyboard": [
                    [{"text": "الغاء", "callback_data": "back"}, {"text": "تاكيد", "callback_data": "OKDelCh2"}]
                ]
            })
        })

if data == "OKDelCh2":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "،🖇:تم حذف القناة الاولى من الإشتراك الإجباري",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "🔙", "callback_data": "back"}]]
            })
        })
        if "ch2" in carlos:
            del carlos["ch2"]
        save_data("data/carlos.json", carlos)

# --- (عرض قنوات الاشتراك العام المعينة حالياً) --- #

if data == "ALLCH":
    if from_id in id_admin or from_id == int(admin):
        ch1_val = carlos.get("ch1", "غير معينة")
        ch2_val = carlos.get("ch2", "غير معينة")
        
        # نستخدم تعديل الرسالة فقط لتغيير المحتوى والأزرار
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": f"🖇:هذه قائمة القنوات الأشتراك الاجباري \n🖇:القناة الاولى {ch1_val}\n🖇:القناة الثانية  {ch2_val}",
            "reply_markup": json.dumps({
                "inline_keyboard": [
                    [{'text': 'حذف القناة 1', 'callback_data': 'delch1'}, {'text': 'حذف القناة 2', 'callback_data': 'delch2'}],
                    [{'text': '🔙', 'callback_data': 'back'}]
                ]
            })
        })



# --- (قسم إدارة المحظورين) --- #

# حساب عدد المحظورين الحاليين
addbanlst = len(carlos.get("ban", [])) if carlos.get("ban") else 0

# عند الضغط على زر "قسم المحظورين"
if data == "lastban":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "اليك قسم المحظورين.\n⎯ ⎯ ⎯ ⎯",
            "parse_mode": "markdown",
            "disable_web_page_preview": True,
            "reply_markup": json.dumps({
                "inline_keyboard": [
                    [{"text": f"المحظورين ( {addbanlst} )", "callback_data": "##"}],
                    [{"text": "حظر", "callback_data": "bannambar"}, {"text": "الغاء حظر", "callback_data": "unbannambar"}],
                    [{"text": "عرض المحظورين", "callback_data": "lstesban"}],
                    [{"text": "مسح المحظورين", "callback_data": "dellastban"}],
                    [{"text": "رجوع", "callback_data": "back"}]
                ]
            })
        })
        # تصفير حالات الإدخال عند الدخول للقسم
        carlos["okunban"] = "done"
        carlos["okban"] = "done"
        save_data("data/carlos.json", carlos)

# عرض قائمة المحظورين بالتفصيل (الأسماء والروابط)
if data == "lstesban":
    if from_id in id_admin or from_id == int(admin):
        if carlos.get("ban"):
            banlast = carlos["ban"]
            result = ""
            for user_id in banlast:
                # جلب معلومات كل عضو محظور من تليجرام
                res = requests.get(f"https://api.telegram.org/bot{API_KEY}/getChat?chat_id={user_id}").json()
                if res.get("ok"):
                    banuser = res['result'].get('username', 'None')
                    banname = res['result'].get('first_name', 'Deleted Account')
                    banid = res['result'].get('id')
                    result += f"- [{banname}](https://t.me/{banuser}) - {banid}\n"
            
            bot("editMessageText", {
                "chat_id": chat_id,
                "message_id": message_id,
                "text": f"اليك قائمة المحظورين : \nꔹ┉ ┉ ┉ ┉ ┉ ┉ ┉ꔹ\n{result}",
                "parse_mode": "markdown",
                "disable_web_page_preview": True,
                "reply_markup": json.dumps({
                    "inline_keyboard": [[{"text": "رجوع", "callback_data": "lastban"}]]
                })
            })
        else:
            # في حال كانت القائمة فارغة
            bot("editMessageText", {
                "chat_id": chat_id,
                "message_id": message_id,
                "text": "لايوجد محظور حاليأ",
                "parse_mode": "MarkDown",
                "reply_markup": json.dumps({
                    "inline_keyboard": [[{"text": "رجوع", "callback_data": "lastban"}]]
                })
            })

# مسح جميع المحظورين نهائياً
if data == "dellastban":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "تم مسح قائمة المحظورين",
            "parse_mode": "MARKDOWN",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "رجوع", "callback_data": "lastban"}]]
            })
        })
        carlos["ban"] = [] # تفريغ القائمة
        save_data("data/carlos.json", carlos)

# --- (منطق الحظر اليدوي عبر إرسال الأيدي) --- #

if data == "bannambar":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "حسنأ عزيزي ارسل ايدي العضو",
            "parse_mode": "markdown",
            "disable_web_page_preview": True,
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "رجوع", "callback_data": "lastban"}]]
            })
        })
        carlos["okban"] = "ok_id"
        save_data("data/carlos.json", carlos)

# استقبال أيدي الحظر
if text and re.match(r"^[0-9]+$", str(text)) and carlos.get("okban") == "ok_id":
    if from_id in id_admin or from_id == int(admin):
        res = requests.get(f"https://api.telegram.org/bot{API_KEY}/getChat?chat_id={text}").json()
        if res.get("ok"):
            banname = res['result'].get('first_name')
            banid = res['result'].get('id')
            bot("sendMessage", {
                "chat_id": chat_id,
                "text": f"العضو - [{banname}](tg://user?id={banid})\nتم حـظـرهه بـنـجاح",
                "parse_mode": "markdown",
                "disable_web_page_preview": True,
                "reply_to_message_id": message_id
            })
            if "ban" not in carlos or carlos["ban"] is None:
                carlos["ban"] = []
            carlos["ban"].append(str(text))
            carlos["okban"] = "done"
            save_data("data/carlos.json", carlos)

# --- (منطق إلغاء الحظر اليدوي) --- #

if data == "unbannambar":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "حسنأ عزيزي ارسل ايدي العضو",
            "parse_mode": "markdown",
            "disable_web_page_preview": True,
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "رجوع", "callback_data": "lastban"}]]
            })
        })
        carlos["okunban"] = "ok_id"
        save_data("data/carlos.json", carlos)

# استقبال أيدي إلغاء الحظر
if text and re.match(r"^[0-9]+$", str(text)) and carlos.get("okunban") == "ok_id":
    if from_id in id_admin or from_id == int(admin):
        res = requests.get(f"https://api.telegram.org/bot{API_KEY}/getChat?chat_id={text}").json()
        if res.get("ok"):
            banname = res['result'].get('first_name')
            banid = res['result'].get('id')
            bot("sendMessage", {
                "chat_id": chat_id,
                "text": f"\nالعضو - [{banname}](tg://user?id={banid})\nتم الـغـاء حـظـرهه بـنـجاح\n",
                "parse_mode": "markdown",
                "disable_web_page_preview": True,
                "reply_to_message_id": message_id
            })
            if str(text) in carlos.get("ban", []):
                carlos["ban"].remove(str(text))
            carlos["okunban"] = "done"
            save_data("data/carlos.json", carlos)




# --- (قسم إدارة النسخة الاحتياطية) --- #

# فتح واجهة قسم النسخة
if data == "Open":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "اليك قسم النسخة للبوت 🗂\n⎯ ⎯ ⎯ ⎯",
            "parse_mode": "Markdown",
            "reply_markup": json.dumps({
                "inline_keyboard": [
                    [{"text": "نسخة الاعضاء ➡️", "callback_data": "##"}, {"text": "جلب نسخة ✳", "callback_data": "OpenCopy"}],
                    [{"text": "نسخة الاعدادات ➡️", "callback_data": "##"}, {"text": "جلب نسخة ✳", "callback_data": "Openstengs"}],
                    [{"text": "رفع نسخة 📤", "callback_data": "addfiles"}],
                    [{"text": "رجوع", "callback_data": "back"}]
                ]
            })
        })

# إرسال ملف نسخة الأعضاء
if data == "OpenCopy":
    if from_id in id_admin or from_id == int(admin):
        with open("data/members.json", "rb") as doc:
            bot("sendDocument", {
                "chat_id": admin,
                "caption": f"اليك النسخة الحتياطية للعضاء 🗂\nعدد الاعضاء ( {md3} ).\n⎯ ⎯ ⎯ ⎯"
            }, files={"document": doc})

# إرسال ملف نسخة الإعدادات
if data == "Openstengs":
    if from_id in id_admin or from_id == int(admin):
        with open("data/carlos.json", "rb") as doc:
            bot("sendDocument", {
                "chat_id": admin,
                "caption": "اليك النسخة الحتياطية الاعدادات 🗂\n⎯ ⎯ ⎯ ⎯"
            }, files={"document": doc})

# تفعيل وضع رفع ملف نسخة
if data == "addfiles":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "حسنأ عزيزي ارسل لي الملف المطلوب 📤\n⎯ ⎯ ⎯ ⎯",
            "parse_mode": "Markdown",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "رجوع", "callback_data": "back"}]]
            })
        })
        carlos["addfiles"] = "no"
        save_data("data/carlos.json", carlos)

# معالجة الملف المرفوع من الأدمن
if message and 'document' in message and carlos.get("addfiles") == "no":
    if from_id == int(admin):
        file_name = message['document'].get('file_name')
        if file_name in ["members.json", "carlos.json"]:
            file_id = message['document']['file_id']
            # جلب رابط الملف من خوادم تليجرام
            get_file = requests.get(f"https://api.telegram.org/bot{API_KEY}/getFile?file_id={file_id}").json()
            file_path = get_file['result']['file_path']
            downloaded_file = requests.get(f"https://api.telegram.org/file/bot{API_KEY}/{file_path}").content
            
            # حفظ الملف في المجلد الخاص بالبيانات
            with open(f"data/{file_name}", "wb") as f:
                f.write(downloaded_file)
            
            bot("sendMessage", {
                "chat_id": chat_id,
                "text": f"تم رفعة نسخة الاعضاء بنجاح 📤\nالملف ( `{file_name}` ).",
                "parse_mode": "Markdown",
                "reply_markup": json.dumps({
                    "inline_keyboard": [[{"text": "رجوع", "callback_data": "back"}]]
                })
            })
            carlos["addfiles"] = "off"
            save_data("data/carlos.json", carlos)

# --- (قسم الإحصائيات) --- #

if data == "1":
    if from_id in id_admin or from_id == int(admin):
        # حساب عدد أعضاء المجموعات (اختياري حسب منطق البوت)
        tgnames = "0"
        if 'groups' in locals() and groups:
            for group_id in groups:
                res = bot("getChatMembersCount", {"chat_id": group_id})
                if res and res.get('ok'):
                    tgnames = str(res['result'])
        
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": XQ_3X["sand"], # يتم جلب نص الإحصائيات من قاموس النصوص
            "parse_mode": "Markdown",
            "reply_markup": json.dumps({
                "inline_keyboard": [
                    [{"text": "تصفير الاحصائيات 🗑.", "callback_data": "lstadel"}],
                    [{"text": "الغاء ↪️", "callback_data": "back"}]
                ]
            })
        })

# واجهة تصفير الإحصائيات
if data == "lstadel":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "حسنأ عزيزي انته متأكد من حذف الاحصائيات 🗑.\nعذرأ اولأ عليك ضغط علي نسخ الاحصائيات 🗂.",
            "reply_markup": json.dumps({
                "inline_keyboard": [
                    [{"text": "نسخ الاحصائيات 🗂.", "callback_data": "Copyahs"}],
                    [{"text": "استعادة الاحصائيات ♻️.", "callback_data": "asahs"}],
                    [{"text": "نعم انا متأكد ✅.", "callback_data": "dellahs"}, {"text": "لا لست متأكد ❎.", "callback_data": "1"}],
                    [{"text": "رجوع ↩", "callback_data": "back"}]
                ]
            })
        })

# تنفيذ مسح الإحصائيات
if data == "dellahs":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "تم تنظيف جميع الاحصائيات 🗑.",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "رجوع ↩", "callback_data": "lstadel"}]]
            })
        })
        # إعادة تعيين ملف الأعضاء (تصفير)
        meca = {"members": "okdell"}
        save_data("data/members.json", meca)

# أخذ نسخة احتياطية سريعة قبل الحذف
if data == "Copyahs":
    if from_id in id_admin or from_id == int(admin):
        with open("data/members.json", "r") as f:
            cc = f.read()
        with open("data/Copy.json", "w") as f:
            f.write(cc)
        
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "تم نسخ جميع الاحصائيات 🗂.\nيمكنك ب اي وقت استعادة الاحصائيات ♻️.",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "رجوع ↩", "callback_data": "lstadel"}]]
            })
        })

# استعادة الإحصائيات من النسخة السريعة
if data == "asahs":
    if from_id in id_admin or from_id == int(admin):
        try:
            with open("data/Copy.json", "r") as f:
                cc = f.read()
            with open("data/members.json", "w") as f:
                f.write(cc)
            
            bot("editMessageText", {
                "chat_id": chat_id,
                "message_id": message_id,
                "text": "تم استعادة جميع الاحصائيات ♻️.",
                "reply_markup": json.dumps({
                    "inline_keyboard": [[{"text": "رجوع ↩", "callback_data": "lstadel"}]]
                })
            })
        except FileNotFoundError:
            pass



# --- (قسم إدارة رسالة الترحيب - start) --- #

# الدخول إلى واجهة إعدادات رسالة الترحيب
if data == "4":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "اهلا بك في قسم رساله(start)",
            "reply_markup": json.dumps({
                "inline_keyboard": [
                    [{"text": "عرض رساله (start)", "callback_data": "startsho"}, {"text": "مسح رساله (start)", "callback_data": "unset start"}],
                    [{"text": "تغير رساله (start)", "callback_data": "setstart"}],
                    [{"text": "رجوع", "callback_data": "back"}]
                ]
            })
        })

# عرض رسالة الترحيب الحالية
if data == "startsho":
    if from_id == int(admin):
        current_start = carlos.get("start", "لا توجد رسالة حالياً")
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": f"⬇️رسالة الستارت هيه\n---------------\n {current_start}",
            "parse_mode": "Markdown",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "رجوع", "callback_data": "back"}]]
            })
        })

# حذف رسالة الترحيب
if data == "unset start":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "تم حذف الاستارت",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "رجوع", "callback_data": "back"}]]
            })
        })
        carlos["start"] = None
        save_data("data/carlos.json", carlos)

# تفعيل وضع استقبال رسالة ترحيب جديدة
if data == "setstart":
    if from_id in id_admin or from_id == int(admin):
        current_start = carlos.get("start", "غير محددة")
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": f"يمكنك الان ارسال رسالة الـstart ⏳\nلعرض الاسم : #name\nلعرض الايدي : #id\nلعرض المعرف : #user\n\nرسالة الـstart الحالية : {current_start}",
            "parse_mode": "Markdown",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "رجوع", "callback_data": "back"}]]
            })
        })
        carlos["ok"] = "ok_start"
        save_data("data/carlos.json", carlos)

# حفظ رسالة الترحيب الجديدة بعد إرسالها من المطور
if text and carlos.get("ok") == "ok_start":
    if from_id in id_admin or from_id == int(admin):
        bot("sendMessage", {
            "chat_id": chat_id,
            "text": f"تم تغير رسالة الـstart الى ℹ️:\n{text}",
            "reply_to_message_id": message_id,
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "رجوع", "callback_data": "back"}]]
            })
        })
        carlos["ok"] = "no"
        carlos["start"] = text
        save_data("data/carlos.json", carlos)

# --- (قسم المحظورين - نسخة مكررة في الكود لضمان التنفيذ) --- #

# حساب عدد المحظورين
addbanlst = len(carlos.get("ban", [])) if carlos.get("ban") else 0

if data == "lastban":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "اليك قسم المحظورين.\n⎯ ⎯ ⎯ ⎯",
            "parse_mode": "markdown",
            "disable_web_page_preview": True,
            "reply_markup": json.dumps({
                "inline_keyboard": [
                    [{"text": f"المحظورين ( {addbanlst} )", "callback_data": "##"}],
                    [{"text": "حظر", "callback_data": "bannambar"}, {"text": "الغاء حظر", "callback_data": "unbannambar"}],
                    [{"text": "عرض المحظورين", "callback_data": "lstesban"}],
                    [{"text": "مسح المحظورين", "callback_data": "dellastban"}],
                    [{"text": "رجوع", "callback_data": "back"}]
                ]
            })
        })
        carlos["okunban"] = "done"
        carlos["okban"] = "done"
        save_data("data/carlos.json", carlos)

# عرض قائمة المحظورين مع معلوماتهم
if data == "lstesban":
    if from_id in id_admin or from_id == int(admin):
        if carlos.get("ban"):
            result = ""
            for user_id in carlos["ban"]:
                res = requests.get(f"https://api.telegram.org/bot{API_KEY}/getChat?chat_id={user_id}").json()
                if res.get("ok"):
                    banuser = res['result'].get('username', 'None')
                    banname = res['result'].get('first_name', 'Account')
                    banid = res['result'].get('id')
                    result += f"- [{banname}](https://t.me/{banuser}) - {banid}\n"
            
            bot("editMessageText", {
                "chat_id": chat_id,
                "message_id": message_id,
                "text": f"اليك قائمة المحظورين : \nꔹ┉ ┉ ┉ ┉ ┉ ┉ ┉ꔹ\n{result}",
                "parse_mode": "markdown",
                "disable_web_page_preview": True,
                "reply_markup": json.dumps({
                    "inline_keyboard": [[{"text": "رجوع", "callback_data": "lastban"}]]
                })
            })
        else:
            bot("editMessageText", {
                "chat_id": chat_id,
                "message_id": message_id,
                "text": "لايوجد محظور حاليأ",
                "parse_mode": "MarkDown",
                "reply_markup": json.dumps({
                    "inline_keyboard": [[{"text": "رجوع", "callback_data": "lastban"}]]
                })
            })

# مسح قائمة المحظورين
if data == "dellastban":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "تم مسح قائمة المحظورين",
            "parse_mode": "MARKDOWN",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "رجوع", "callback_data": "lastban"}]]
            })
        })
        carlos["ban"] = []
        save_data("data/carlos.json", carlos)

# تفعيل وضع "أرسل الأيدي" للحظر اليدوي
if data == "bannambar":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "حسنأ عزيزي ارسل ايدي العضو",
            "parse_mode": "markdown",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "رجوع", "callback_data": "lastban"}]]
            })
        })
        carlos["okban"] = "ok_id"
        save_data("data/carlos.json", carlos)

# تنفيذ الحظر بعد إرسال الأيدي
if text and re.match(r"^[0-9]+$", str(text)) and carlos.get("okban") == "ok_id":
    if from_id in id_admin or from_id == int(admin):
        res = requests.get(f"https://api.telegram.org/bot{API_KEY}/getChat?chat_id={text}").json()
        if res.get("ok"):
            banname = res['result'].get('first_name')
            bot("sendMessage", {
                "chat_id": chat_id,
                "text": f"العضو - [{banname}](tg://user?id={text})\nتم حـظـرهه بـنـجاح",
                "parse_mode": "markdown",
                "reply_to_message_id": message_id
            })
            if "ban" not in carlos or carlos["ban"] is None:
                carlos["ban"] = []
            carlos["ban"].append(str(text))
            carlos["okban"] = "done"
            save_data("data/carlos.json", carlos)

# تنفيذ إلغاء الحظر اليدوي
if text and re.match(r"^[0-9]+$", str(text)) and carlos.get("okunban") == "ok_id":
    if from_id in id_admin or from_id == int(admin):
        if str(text) in carlos.get("ban", []):
            carlos["ban"].remove(str(text))
            bot("sendMessage", {
                "chat_id": chat_id,
                "text": f"تم الـغـاء حـظـرهه بـنـجاح",
                "reply_to_message_id": message_id
            })
            carlos["okunban"] = "done"
            save_data("data/carlos.json", carlos)




# --- (تابع: قسم الإحصائيات - تنفيذ الحذف والنسخ) --- #

# تنفيذ مسح الإحصائيات نهائياً
if data == "dellahs":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "تم تنظيف جميع الاحصائيات 🗑.",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "رجوع ↩", "callback_data": "lstadel"}]]
            })
        })
        # تصفير ملف الأعضاء
        meca = {"members": "okdell"}
        save_data("data/members.json", meca)

# عمل نسخة احتياطية سريعة للإحصائيات
if data == "Copyahs":
    if from_id in id_admin or from_id == int(admin):
        try:
            with open("data/members.json", "r") as f:
                cc = f.read()
            with open("data/Copy.json", "w") as f:
                f.write(cc)
            
            bot("editMessageText", {
                "chat_id": chat_id,
                "message_id": message_id,
                "text": "تم نسخ جميع الاحصائيات 🗂.\nيمكنك ب اي وقت استعادة الاحصائيات ♻️.",
                "reply_markup": json.dumps({
                    "inline_keyboard": [[{"text": "رجوع ↩", "callback_data": "lstadel"}]]
                })
            })
        except Exception as e:
            print(f"Error copying stats: {e}")

# استعادة الإحصائيات من النسخة السريعة
if data == "asahs":
    if from_id in id_admin or from_id == int(admin):
        try:
            with open("data/Copy.json", "r") as f:
                cc = f.read()
            with open("data/members.json", "w") as f:
                f.write(cc)
            
            bot("editMessageText", {
                "chat_id": chat_id,
                "message_id": message_id,
                "text": "تم استعادة جميع الاحصائيات ♻️.",
                "reply_markup": json.dumps({
                    "inline_keyboard": [[{"text": "رجوع ↩", "callback_data": "lstadel"}]]
                })
            })
        except FileNotFoundError:
            pass

# --- (قسم إدارة الأدمنية - الإدارة والرفع والحذف) --- #

# عرض قائمة الأدمنية الحاليين
if data == "5":
    if from_id == int(admin):
        keyboard = {"inline_keyboard": []}
        # توليد زر لكل أدمن موجود في القائمة
        if "admin" in carlos and carlos["admin"]:
            for ad in carlos["admin"]:
                keyboard["inline_keyboard"].append([{"text": str(ad), "callback_data": f"del#{ad}"}])
        
        # أزرار الإضافة والرجوع
        keyboard["inline_keyboard"].append([{"text": "اضف ادمن ➕", "callback_data": "add_admin"}])
        keyboard["inline_keyboard"].append([{"text": "رجوع", "callback_data": "back"}])
        
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "يمكنك رفع ادمن وحذف ادمن عن طريق الازرار 🔽\n⎯ ⎯ ⎯ ⎯\nيمكن للادمن التحقق من الاحصائيات فقط ⚠️",
            "reply_markup": json.dumps(keyboard)
        })

# معالجة حذف الأدمن عند الضغط على اسمه
if data and data.startswith("del#"):
    if from_id == int(admin):
        admin_to_del = data.split("#")[1]
        if "admin" in carlos and admin_to_del in carlos["admin"]:
            carlos["admin"].remove(admin_to_del)
            save_data("data/carlos.json", carlos)
            
            # إعادة بناء لوحة المفاتيح المحدثة
            keyboard = {"inline_keyboard": []}
            for ad in carlos["admin"]:
                keyboard["inline_keyboard"].append([{"text": str(ad), "callback_data": f"del#{ad}"}])
            keyboard["inline_keyboard"].append([{"text": "اضف ادمن ➕", "callback_data": "add_admin"}])
            keyboard["inline_keyboard"].append([{"text": "رجوع", "callback_data": "back"}])
            
            bot("editMessageReplyMarkup", {
                "chat_id": chat_id,
                "message_id": message_id,
                "reply_markup": json.dumps(keyboard)
            })

# طلب أيدي الأدمن الجديد
if data == "add_admin":
    if from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": "الان ارسل ايدي الشخص ℹ️",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "الغاء ↪️", "callback_data": "back"}]]
            })
        })
        carlos["ok"] = "ok_admin"
        save_data("data/carlos.json", carlos)

# التحقق من الأيدي المرسل (إذا لم يكن عضواً في البوت)
if text and carlos.get("ok") == "ok_admin":
    if from_id == int(admin):
        # التحقق إذا كان المستخدم موجوداً في قائمة الأعضاء
        if text not in members: # مفترض أن members هي قائمة معرفة مسبقاً من ملف members.json
            bot("sendMessage", {
                "chat_id": chat_id,
                "text": f"{text} ليس عضو بالبوت ⚠️",
                "reply_to_message_id": message_id,
                "reply_markup": json.dumps({
                    "inline_keyboard": [[{"text": "رجوع", "callback_data": "back"}]]
                })
            })

# التحقق إذا كان الأيدي المرسل مرفوعاً كأدمن بالفعل
if text and carlos.get("ok") == "ok_admin":
    if from_id == int(admin):
        if "admin" in carlos and text in carlos["admin"]:
            bot("sendMessage", {
                "chat_id": chat_id,
                "text": "العضو مرفوع ادمن ⚠️",
                "reply_to_message_id": message_id,
                "reply_markup": json.dumps({
                    "inline_keyboard": [[{"text": "رجوع", "callback_data": "back"}]]
                })
            })
            
            
            

# --- (تابع: إتمام إضافة أدمن جديد) --- #

# في حال كان العضو موجوداً في البوت (members) وغير مضاف مسبقاً
if text and carlos.get("ok") == "ok_admin" and text in members:
    if from_id == int(admin):
        bot("sendMessage", {
            "chat_id": chat_id,
            "text": f"تم اضافه {text} ادمن ✅",
            "reply_to_message_id": message_id,
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "رجوع", "callback_data": "back"}]]
            })
        })
        # إضافة الأيدي لقائمة الأدمنية وتصفير الحالة
        if "admin" not in carlos:
            carlos["admin"] = []
        carlos["admin"].append(str(text))
        carlos["ok"] = "no"
        save_data("data/carlos.json", carlos)

# --- (قسم الإذاعة والتبليغ - الواجهة الرئيسية) --- #

if data == "10":
    if from_id in id_admin or from_id == int(admin):
        # حساب إحصائيات المجموعات بشكل سريع للعرض
        tgnames = "0"
        if 'groups' in locals() and groups:
            for group_id in groups:
                res = bot("getChatMembersCount", {"chat_id": group_id})
                if res and res.get('ok'):
                    tgnames = str(res['result'])
        
        bot("editMessageText", {
            "chat_id": chat_id, 
            "message_id": message_id,
            "text": XQ_3X["sand"], # نص واجهة الإذاعة من قاموس النصوص
            "reply_markup": json.dumps({
                "inline_keyboard": [
                    [{"text": "اذاعة للكل", "callback_data": "send_text"}, {"text": "اذاعة توجيه للكل", "callback_data": "send_rep"}],
                    [{"text": "اذاعة للخاص", "callback_data": "send_text1"}, {"text": "اذاعة توجيه للخاص", "callback_data": "send_rep1"}],
                    [{"text": "اذاعة كروبات", "callback_data": "send_text2"}, {"text": "اذاعة توجيه كروبات", "callback_data": "send_rep2"}],
                    [{"text": "رجوع", "callback_data": "back"}]
                ]
            })
        })
        carlos["data"] = "no"
        save_data("data/carlos.json", carlos)

# --- (الإذاعة النصية للكل: خاص + مجموعات) --- #

# الخطوة 1: طلب نص الإذاعة
if data == "send_text":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": XQ_3X["sand5"], # نص "أرسل رسالتك الآن"
            "parse_mode": "Markdown",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "رجوع", "callback_data": "10"}]]
            })
        })
        carlos["data"] = "ok_text"
        save_data("data/carlos.json", carlos)

# الخطوة 2: استقبال النص وإرساله للجميع
if text and carlos.get("data") == "ok_text" and text != "/start" and from_id == int(admin):
    # إرسال تأكيد بدء الإذاعة للأدمن
    bot("sendMessage", {
        "chat_id": chat_id,
        "text": XQ_3X["sand6"], # نص "جاري الإرسال..."
        "parse_mode": "Markdown",
        "reply_to_message_id": message_id,
        "reply_markup": json.dumps({
            "inline_keyboard": [[{"text": "رجوع", "callback_data": "10"}]]
        })
    })

    # الإرسال للمجموعات
    if 'groups' in locals() and groups:
        for group_id in groups:
            bot("sendMessage", {
                "chat_id": group_id,
                "text": text,
                "parse_mode": "Markdown"
            })

    # الإرسال للخاص (للأعضاء)
    if 'members' in locals() and members:
        for member_id in members:
            bot("sendMessage", {
                "chat_id": member_id,
                "text": text,
                "parse_mode": "Markdown"
            })
    
    # إنهاء الحالة بعد الإكمال
    carlos["data"] = "done"
    save_data("data/carlos.json", carlos)



# --- (تابع: نظام الإذاعة - إذاعة التوجيه للكل) --- #

# الخطوة 1: طلب الرسالة المراد توجيهها للكل (خاص + مجموعات)
if data == "send_rep":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": XQ_3X["sand7"], # نص "أرسل ما تريد توجيهه للكل"
            "parse_mode": "Markdown",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "رجوع", "callback_data": "10"}]]
            })
        })
        carlos["data"] = "ok_rep"
        save_data("data/carlos.json", carlos)

# الخطوة 2: تنفيذ التوجيه (Forward) لجميع الوجهات
if text and carlos.get("data") == "ok_rep" and text != "/start" and from_id == int(admin):
    # إرسال رسالة تأكيد البدء
    bot("sendMessage", {
        "chat_id": chat_id,
        "text": XQ_3X["sand8"], # نص "جاري توجيه الرسالة..."
        "parse_mode": "Markdown",
        "reply_to_message_id": message_id,
        "reply_markup": json.dumps({
            "inline_keyboard": [[{"text": "رجوع", "callback_data": "10"}]]
        })
    })

    # التوجيه للمجموعات
    if 'groups' in locals() and groups:
        for group_id in groups:
            bot("forwardMessage", {
                "chat_id": group_id,
                "from_chat_id": from_id,
                "message_id": message_id
            })

    # التوجيه للخاص (الأعضاء)
    if 'members' in locals() and members:
        for member_id in members:
            bot("forwardMessage", {
                "chat_id": member_id,
                "from_chat_id": from_id,
                "message_id": message_id
            })
    
    carlos["data"] = "done"
    save_data("data/carlos.json", carlos)

# --- (الإذاعة النصية للخاص فقط) --- #

# الخطوة 1: طلب النص المراد إرساله للخاص
if data == "send_text1":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": XQ_3X["sand1"], # نص "أرسل نص الإذاعة للخاص"
            "parse_mode": "Markdown",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "رجوع", "callback_data": "10"}]]
            })
        })
        carlos["data"] = "ok_text1"
        save_data("data/carlos.json", carlos)

# الخطوة 2: تنفيذ الإرسال النصي للأعضاء فقط
if text and carlos.get("data") == "ok_text1" and text != "/start" and from_id == int(admin):
    bot("sendMessage", {
        "chat_id": chat_id,
        "text": XQ_3X["sand2"], # نص "جاري الإرسال للأعضاء..."
        "parse_mode": "Markdown",
        "reply_to_message_id": message_id,
        "reply_markup": json.dumps({
            "inline_keyboard": [[{"text": "رجوع", "callback_data": "10"}]]
        })
    })

    if 'members' in locals() and members:
        for member_id in members:
            bot("sendMessage", {
                "chat_id": member_id,
                "text": text,
                "parse_mode": "Markdown"
            })
    
    carlos["data"] = "done"
    save_data("data/carlos.json", carlos)

# --- (إذاعة التوجيه للخاص فقط) --- #

# الخطوة 1: طلب الرسالة لتوجيهها للأعضاء فقط
if data == "send_rep1":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": XQ_3X["sand9"], # نص "أرسل ما تريد توجيهه للأعضاء"
            "parse_mode": "Markdown",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "رجوع", "callback_data": "10"}]]
            })
        })
        # (بانتظار الجزء القادم لتكملة حالة ok_rep1)



# --- (تابع: نظام الإذاعة - إتمام توجيه الخاص) --- #

# الخطوة 2: تنفيذ توجيه الرسالة للأعضاء فقط
if text and carlos.get("data") == "ok_rep1" and text != "/start" and from_id == int(admin):
    bot("sendMessage", {
        "chat_id": chat_id,
        "text": XQ_3X["sand10"], # نص "جاري توجيه الرسالة للأعضاء..."
        "parse_mode": "Markdown",
        "reply_to_message_id": message_id,
        "reply_markup": json.dumps({
            "inline_keyboard": [[{"text": "رجوع", "callback_data": "10"}]]
        })
    })

    if 'members' in locals() and members:
        for member_id in members:
            bot("forwardMessage", {
                "chat_id": member_id,
                "from_chat_id": from_id,
                "message_id": message_id
            })
    
    carlos["data"] = "done"
    save_data("data/carlos.json", carlos)

# --- (الإذاعة النصية للمجموعات فقط) --- #

# الخطوة 1: طلب النص
if data == "send_text2":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": XQ_3X["sand3"],
            "parse_mode": "Markdown",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "رجوع", "callback_data": "10"}]]
            })
        })
        carlos["data"] = "ok_text2"
        save_data("data/carlos.json", carlos)

# الخطوة 2: الإرسال للمجموعات
if text and carlos.get("data") == "ok_text2" and text != "/start" and from_id == int(admin):
    bot("sendMessage", {
        "chat_id": chat_id,
        "text": XQ_3X["sand4"],
        "parse_mode": "Markdown",
        "reply_to_message_id": message_id,
        "reply_markup": json.dumps({
            "inline_keyboard": [[{"text": "رجوع", "callback_data": "10"}]]
        })
    })

    if 'groups' in locals() and groups:
        for group_id in groups:
            bot("sendMessage", {
                "chat_id": group_id,
                "text": text,
                "parse_mode": "Markdown"
            })
    
    carlos["data"] = "done"
    save_data("data/carlos.json", carlos)

# --- (إذاعة التوجيه للمجموعات فقط) --- #

# الخطوة 1: طلب الرسالة
if data == "send_rep2":
    if from_id in id_admin or from_id == int(admin):
        bot("editMessageText", {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": XQ_3X["sand11"],
            "parse_mode": "Markdown",
            "reply_markup": json.dumps({
                "inline_keyboard": [[{"text": "رجوع", "callback_data": "10"}]]
            })
        })
        carlos["data"] = "ok_rep2"
        save_data("data/carlos.json", carlos)

# الخطوة 2: تنفيذ التوجيه للمجموعات
if text and carlos.get("data") == "ok_rep2" and text != "/start" and from_id == int(admin):
    bot("sendMessage", {
        "chat_id": chat_id,
        "text": XQ_3X["sand12"],
        "parse_mode": "Markdown",
        "reply_to_message_id": message_id,
        "reply_markup": json.dumps({
            "inline_keyboard": [[{"text": "رجوع", "callback_data": "10"}]]
        })
    })

    if 'groups' in locals() and groups:
        for group_id in groups:
            bot("forwardMessage", {
                "chat_id": group_id,
                "from_chat_id": from_id,
                "message_id": message_id
            })
    
    carlos["data"] = "done"
    save_data("data/carlos.json", carlos)

# --- (قسم استقبال رسائل المستخدمين وتوجيهها للمطور) --- #

if text and text == '/start' and from_id != int(admin):
    bot('sendMessage', {
        'chat_id': chat_id,
        'text': XQ_3X["start"],
        'parse_mode': "markdown",
        'disable_web_page_preview': True,
        'reply_to_message_id': message_id,
        'reply_markup': json.dumps({
            'inline_keyboard': [[{'text': namezar, 'url': urlzar}]]
        })
    })

if text and text != '/start' and from_id != int(admin):
    # توجيه رسالة العضو إلى المطور
    bot('forwardMessage', {
        'chat_id': admin,
        'from_chat_id': chat_id,
        'message_id': message_id
    })
    # إبلاغ العضو بالنجاح
    bot('sendMessage', {
        'chat_id': chat_id,
        'text': "*تم ارسال رسالتك بنجاح ✅.*",
        'parse_mode': "markdown",
        'disable_web_page_preview': True,
        'reply_to_message_id': message_id
    })

# --- (قسم رد المطور على رسائل الأعضاء الموجهة) --- #

# التأكد أن المطور يقوم بالرد على رسالة موجهة
if message and 'reply_to_message' in message and 'forward_from' in message['reply_to_message']:
    target_user = message['reply_to_message']['forward_from']['id']
    
    if from_id == int(admin):
        # الرد بنص
        if text:
            bot('sendMessage', {'chat_id': target_user, 'text': text})
        
        # الرد ببصمة صوتية
        if 'voice' in message:
            bot('sendVoice', {'chat_id': target_user, 'voice': message['voice']['file_id']})
            
        # الرد بصورة
        if 'photo' in message:
            # نأخذ آخر حجم للصورة (الأعلى دقة)
            bot('sendPhoto', {'chat_id': target_user, 'photo': message['photo'][-1]['file_id']})
            
        # الرد بملف
        if 'document' in message:
            bot('sendDocument', {'chat_id': target_user, 'document': message['document']['file_id']})
            
        # الرد بملصق (Sticker)
        if 'sticker' in message:
            bot('sendSticker', {'chat_id': target_user, 'sticker': message['sticker']['file_id']})
            
        # الرد بفيديو
        if 'video' in message:
            bot('sendVideo', {'chat_id': target_user, 'video': message['video']['file_id']})
            
        # الرد بملف صوتي (Audio)
        if 'audio' in message:
            bot('sendAudio', {'chat_id': target_user, 'audio': message['audio']['file_id']})

# أضف هذا في نهاية الملف تماماً لكي يبدأ البوت بالعمل


print("البوت بدأ العمل الآن...")
last_update_id = 0

while True:
    try:
        # جلب التحديثات الجديدة
        updates = bot('getUpdates', {'offset': last_update_id + 1, 'timeout': 30})
        
        if updates and updates.get('ok'):
            for update in updates['result']:
                # --- انتبه! كل الأسطر التالية يجب أن تبدأ بمسافة (إزاحة) لتكون داخل الـ for ---
                last_update_id = update['update_id']
                message = update.get('message', {})
                callback_query = update.get('callback_query', {})

                # تعريف المتغيرات لكي يراها الكود
                if callback_query:
                    res_msg = callback_query.get('message', {})
                    data = callback_query.get('data')
                    text = None
                else:
                    res_msg = message
                    data = None
                    text = message.get('text')

                chat_id = res_msg.get('chat', {}).get('id')
                from_id = update.get('message', {}).get('from', {}).get('id') or update.get('callback_query', {}).get('from', {}).get('id')
                message_id = res_msg.get('message_id')

                # هنا يتم استخراج حالة المنظف بشكل آمن
                                # هنا يتم استخراج حالة المنظف بشكل آمن
                if 'xmax' in globals():
                    cleaner = xmax.get("cleaner", {}).get(str(chat_id))
                else:
                    cleaner = None

                # انظر للمسافات هنا (يجب أن يبدأ السطر من هنا)

                handle_update(chat_id, from_id, text, data, message_id, res_msg, cleaner)

                # ==========================================
                # هنا تضع كل أوامر الـ if (المنطق الخاص بالبوت)
                # ويجب أن تكون جميعها مزاحة بنفس مستوى chat_id
                # ==========================================

    except Exception as e:
        print(f"خطأ في الاتصال أو التنفيذ: {e}")
        time.sleep(1)
