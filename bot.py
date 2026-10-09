import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# إعداد السجلات لمتابعة حالة التشغيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# توكن البوت
TOKEN = "8704311162:AAGv9FLgVhP1LyvFWrsXmqjNZ-jDSqKbGmM"

# ==================== الروابط الدقيقة والمباشرة لكل المواد ====================
DRIVE_GENERAL_URL = "https://drive.google.com/drive/folders/10gHDDg5mzJmO9081eaajxjDlphKqt6eB"

BASICS_URL = "https://drive.google.com/drive/folders/15YS4dsFrYKDY7mX7tRlkv4mdIBt5yk5j?usp=drive_link" 
CALCULUS_1_URL = "https://drive.google.com/drive/folders/1daJqTERNOOoirMl27nJKX4BUd0W_ZSGg?usp=drive_link" 
CALCULUS_2_URL = "https://drive.google.com/drive/folders/1fOrpWBVWZ6WuFZkouQrXBRSQ2Ts0N2Dr?usp=drive_link" 
LINEAR_1_URL = "https://drive.google.com/drive/folders/1CQBEPnz7P0aM8bvzfgsh6ezvVEnNeRwP?usp=drive_link" 
LINEAR_2_URL = "https://drive.google.com/drive/folders/1JbbEp07_Hx5MHyS3Nj9B5cQjeUQI3Uvm?usp=drive_link" 
PRINCIPLES_STATS_URL = "https://drive.google.com/drive/folders/1Pf-MqO3VnXX-ZXDo-DlbQGKYFtVSS7ix?usp=drive_link" 
PROB_URL = "https://drive.google.com/drive/folders/1yL8JlUyaCRIPpzM0He7Px1XTfcdnXDfM?usp=drive_link" 
INTERMEDIATE_ANALYSIS_URL = "https://drive.google.com/drive/folders/1x0WMCMk4-BSsS2WtHBQ8Rqv43wT2OGGT?usp=drive_link" 
DIFF_URL = "https://drive.google.com/drive/folders/189JdwFD0RHy_zhBMpbJI8XbBpS1pzqcK?usp=drive_link" 
LOGIC_URL = "https://drive.google.com/drive/folders/1G5VbQcqJmcghSESRCwBf0lFxw-XQp2fE?usp=drive_link" 
METHODS_URL = "https://drive.google.com/drive/folders/1Hl4TblXIO9VBX_8nCxYAbjZHNZiLCOpC?usp=drive_link" 
EUCLIDEAN_GEOMETRY_URL = "https://drive.google.com/drive/folders/1OVpwU5MjfyN0mA9WeCRBnf8SFnwI8ctZ?usp=drive_link" 
MATHEMATICAL_STATS_URL = "https://drive.google.com/drive/folders/1Aw6EaJqpZbrkm6BinS4Fi7N9XLVi0zyb?usp=drive_link" 
ADVANCED_URL = "https://drive.google.com/drive/folders/1JllqoJaNV4tIyLu5vN6s1ihkqpVEHI-h?usp=drive_link" 
LINEAR_PROGRAMMING_URL = "https://drive.google.com/drive/folders/1ivd_lqw9SEaf4d-SDa8wHb7cP7hBh9PY?usp=drive_link" 
NUMERICAL_ANALYSIS_URL = "https://drive.google.com/drive/folders/1WbAlRDI8rawJQBkJHAozcXiSscP6Rl-S?usp=drive_link" 
COMPLEX_ANALYSIS_URL = "https://drive.google.com/drive/folders/1EXpLju6736JofZ8SIA7QL49wQbwSmeql?usp=drive_link" 
COMP_MATH_APPS_URL = "https://drive.google.com/drive/folders/1Gl0FGad4l8w66zx9WSrgYFQxlL4OalZC?usp=drive_link" 
TOPOLOGY_URL = "https://drive.google.com/drive/folders/1JWwiAQxKPhjQUYnJ4lJzPolRvo4KoXmG?usp=drive_link" 
REAL_1_URL = "https://drive.google.com/drive/folders/1zclSSFjh0YxAKnPw2GjHwLQdcWRiY3MO?usp=drive_link" 
REAL_2_URL = "https://drive.google.com/drive/folders/1hNRs7kvUAd7a6C2EhprdVqHIAq7opxBn?usp=drive_link" 
STATISTICAL_METHODS_URL = "https://drive.google.com/drive/folders/1eiU8EvsZgd4IjXFX86WEK4nzJHUOsqWW?usp=drive_link" 
NUMBER_THEORY_URL = "https://drive.google.com/drive/folders/1__GHQ5lt11zhkEXjMUTIU42Htuvw87ed?usp=drive_link" 
MATH_TEACHING_METHODS_URL = "https://drive.google.com/drive/folders/1XkpbvdwtZM06VmRSZzeL9iV0Gn_jUlx_?usp=drive_link" 
OR_PROB_MODELS_URL = "https://drive.google.com/drive/folders/1XzLJI-_-jrlJTrs5ZVHbBl80-KsvAN8u?usp=drive_link" 
ABSTRACT_ALGEBRA_2_URL = "https://drive.google.com/drive/folders/1Hmv6dLybCF1i3QsXffPaomG28GhjRGcF?usp=drive_link" 
PHYSICS_1_URL = "https://drive.google.com/drive/folders/1TsE0Ss_K3TYUJEeVLyqZEW032QXnclAL?usp=drive_link" 
PHYSICS_2_URL = "https://drive.google.com/drive/folders/1buLX_1GqFCmz72F_n98mAG3pMDuH8JD_?usp=drive_link" 
PHYSICS_LAB_URL = "https://drive.google.com/drive/folders/1z5ELY3krIq_TwCeHhxCOtG-LZgzY6_IA?usp=drive_link" 
CPP_URL = "https://drive.google.com/drive/folders/1qdOlelE_80EG4-9lvPT9vAVfEmeZUgOS?usp=drive_link" 
TIME_SERIES_URL = "https://drive.google.com/drive/folders/1ZDBT3AC8IDCFJHocBNc4TxvcpCpSh_Sw?usp=drive_link" 
REPRESENTATION_THEORY_URL = "https://drive.google.com/drive/folders/1yXygF9KZMELF2C9CJ14jK75Gwbs4cXz4?usp=drive_link" 
GRAPH_THEORY_URL = "https://drive.google.com/drive/folders/1_rrY17KYsot3NB_53RDnDtMLkHhdtB9A?usp=drive_link" 
MATH_MODELS_URL = "https://drive.google.com/drive/folders/1IubVON1tWCF_HWj6yf-fNwPucsLLNfKK?usp=drive_link" 

# أمر البدء /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    
    keyboard = [
        [InlineKeyboardButton("🟡 مواد السنة الأولى", callback_data="year_1")],
        [InlineKeyboardButton("🟣 مواد السنة الثانية", callback_data="year_2")],
        [InlineKeyboardButton("🔘 مواد السنة الثالثة", callback_data="year_3")],
        [InlineKeyboardButton("🟤 مواد السنة الرابعة", callback_data="year_4")],
        [InlineKeyboardButton("📚 حرات القسم", callback_data="elective_dept")],
        [InlineKeyboardButton("🩷 إجباري كلية", callback_data="college_req")],
        [
            InlineKeyboardButton("📌 الأسماء الشائعة", callback_data="send_names_image"),
            InlineKeyboardButton("📊 العلامات والرموز", callback_data="send_marks_image")
        ],
        [InlineKeyboardButton("🌳 شجرة التخصص", callback_data="send_tree_image")],
        [InlineKeyboardButton("📂 مجلد المواد الشامل", url=DRIVE_GENERAL_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    welcome_message = (
        f"أهلاً بك يا {user_name} في بوت المواد الجامعية! 🎓✨\n"
        "مقدم من **فريق إبسلون بالتعاون مع فريق إنفنتي** 🚀\n\n"
        "اختر التصنيف أو السنة الدراسية المطلوبة للانتقال المباشر لمجلداتها فوراً:"
    )
    await update.message.reply_text(welcome_message, reply_markup=reply_markup, parse_mode="Markdown")

# أمر عرض القوائم /materials
async def materials_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🟡 السنة الأولى", callback_data="year_1")],
        [InlineKeyboardButton("🟣 مواد السنة الثانية", callback_data="year_2")],
        [InlineKeyboardButton("🔘 مواد السنة الثالثة", callback_data="year_3")],
        [InlineKeyboardButton("🟤 مواد السنة الرابعة", callback_data="year_4")],
        [InlineKeyboardButton("📚 حرات القسم", callback_data="elective_dept")],
        [InlineKeyboardButton("🩷 إجباري كلية", callback_data="college_req")],
        [InlineKeyboardButton("📌 الأسماء الشائعة", callback_data="send_names_image")],
        [InlineKeyboardButton("📊 العلامات والرموز", callback_data="send_marks_image")],
        [InlineKeyboardButton("🌳 شجرة التخصص", callback_data="send_tree_image")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "📂 **اختر القسم أو السنة الدراسية المطلوبة:**",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# دالة إرسال صورة الشجرة مباشرة
async def send_tree_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query:
        await query.answer()
        chat_id = query.message.chat_id
    else:
        chat_id = update.effective_chat.id

    image_path = "tree.png"
    try:
        if os.path.exists(image_path):
            await context.bot.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'), caption="🌳 **شجرة التخصص الرسمية لقسم الرياضيات والإحصاء**")
        else:
            await context.bot.send_message(chat_id=chat_id, text="📌 يرجى التأكد من وجود صورة الشجرة باسم `tree.png` داخل مجلد البوت.")
    except Exception as e:
        logging.error(f"Error sending tree image: {e}")
        await context.bot.send_message(chat_id=chat_id, text="عذراً حدث خطأ أثناء إرسال الصورة.")

# دالة إرسال صورة نظام العلامات والرموز مباشرة
async def send_marks_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query:
        await query.answer()
        chat_id = query.message.chat_id
    else:
        chat_id = update.effective_chat.id

    image_path = "marks.png"
    try:
        if os.path.exists(image_path):
            await context.bot.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'), caption="📊 **نظام العلامات والرموز**")
        else:
            await context.bot.send_message(chat_id=chat_id, text="📌 يرجى التأكد من وضع صورة العلامات والرموز في مجلد البوت وتسميتها `marks.png`.")
    except Exception as e:
        logging.error(f"Error sending marks image: {e}")
        await context.bot.send_message(chat_id=chat_id, text="عذراً حدث خطأ أثناء إرسال الصورة.")

# دالة إرسال صورة الأسماء الشائعة مباشرة
async def send_names_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query:
        await query.answer()
        chat_id = query.message.chat_id
    else:
        chat_id = update.effective_chat.id

    image_path = "common_names.png"
    try:
        if os.path.exists(image_path):
            await context.bot.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'), caption="📌 **الأسماء الشائعة للمواد**")
        else:
            await context.bot.send_message(chat_id=chat_id, text="📌 يرجى التأكد من وضع صورة الأسماء الشائعة في مجلد البوت وتسميتها `common_names.png`.")
    except Exception as e:
        logging.error(f"Error sending names image: {e}")
        await context.bot.send_message(chat_id=chat_id, text="عذراً حدث خطأ أثناء إرسال الصورة.")

# معالجة الأزرار والقوائم
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    
    if query.data == "send_tree_image":
        await send_tree_image(update, context)
        return
    elif query.data == "send_marks_image":
        await send_marks_image(update, context)
        return
    elif query.data == "send_names_image":
        await send_names_image(update, context)
        return

    await query.answer()

    if query.data == "year_1":
        keyboard = [
            [InlineKeyboardButton("🟡 كالكولاس 1", url=CALCULUS_1_URL), InlineKeyboardButton("🟡 كالكولاس 2", url=CALCULUS_2_URL)],
            [InlineKeyboardButton("🟡 مبادئ الإحصاء", url=PRINCIPLES_STATS_URL), InlineKeyboardButton("🟡 أسس الرياضيات", url=BASICS_URL)],
            [InlineKeyboardButton("🟡 مبادئ جبر خطي", url=LINEAR_1_URL)],
            [InlineKeyboardButton("🔙 العودة للقائمة الرئيسية", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="🟡 **مواد السنة الأولى:**", reply_markup=reply_markup, parse_mode="Markdown")
        
    elif query.data == "year_2":
        keyboard = [
            [InlineKeyboardButton("🟣 لوجيك", url=LOGIC_URL), InlineKeyboardButton("🟣 هندسة اقليدية واللااقليدية", url=EUCLIDEAN_GEOMETRY_URL)],
            [InlineKeyboardButton("🟣 تحليل وسيط", url=INTERMEDIATE_ANALYSIS_URL), InlineKeyboardButton("🟣 نظرية الاحتمال", url=PROB_URL)],
            [InlineKeyboardButton("🟣 معادلات تفاضلية عادية", url=DIFF_URL), InlineKeyboardButton("🟣 طرق رياضية", url=METHODS_URL)],
            [InlineKeyboardButton("🔙 العودة للقائمة الرئيسية", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="🟣 **مواد السنة الثانية:**", reply_markup=reply_markup, parse_mode="Markdown")

    elif query.data == "year_3":
        keyboard = [
            [InlineKeyboardButton("🔘 جبر خطي", url=LINEAR_2_URL), InlineKeyboardButton("🔘 برمجة خطية", url=LINEAR_PROGRAMMING_URL)],
            [InlineKeyboardButton("🔘 نظرية عدد", url=NUMBER_THEORY_URL), InlineKeyboardButton("🔘 تفاضل وتكامل متقدم (أدفانس)", url=ADVANCED_URL)],
            [InlineKeyboardButton("🔘 الجبر التجريدي 1", url=DRIVE_GENERAL_URL), InlineKeyboardButton("🔘 احصاء رياضي", url=MATHEMATICAL_STATS_URL)],
            [InlineKeyboardButton("🔘 طرق احصائية", url=STATISTICAL_METHODS_URL), InlineKeyboardButton("🔘 تحليل عددي", url=NUMERICAL_ANALYSIS_URL)],
            [InlineKeyboardButton("🔘 تحليل مركب", url=COMPLEX_ANALYSIS_URL), InlineKeyboardButton("🔘 تطبيقات رياضية حاسوبية", url=COMP_MATH_APPS_URL)],
            [InlineKeyboardButton("🔘 توبولوجي", url=TOPOLOGY_URL), InlineKeyboardButton("🔘 تحليل حقيقي 1 (Real 1)", url=REAL_1_URL)],
            [InlineKeyboardButton("🔙 العودة للقائمة الرئيسية", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="🔘 **مواد السنة الثالثة:**", reply_markup=reply_markup, parse_mode="Markdown")

    elif query.data == "year_4":
        keyboard = [
            [InlineKeyboardButton("🟤 تحليل حقيقي 2", url=REAL_2_URL), InlineKeyboardButton("🟤 الجبر التجريدي 2", url=ABSTRACT_ALGEBRA_2_URL)],
            [InlineKeyboardButton("🟤 النماذج الاحتمالية بحوث عمليات", url=OR_PROB_MODELS_URL), InlineKeyboardButton("🟤 أساليب تدريس الرياضيات", url=MATH_TEACHING_METHODS_URL)],
            [InlineKeyboardButton("🔙 العودة للقائمة الرئيسية", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="🟤 **مواد السنة الرابعة:**", reply_markup=reply_markup, parse_mode="Markdown")

    elif query.data == "elective_dept":
        keyboard = [
            [InlineKeyboardButton("📚 السلاسل الزمنية", url=TIME_SERIES_URL), InlineKeyboardButton("📚 مبادئ التمثيلية", url=REPRESENTATION_THEORY_URL)],
            [InlineKeyboardButton("📚 نظرية الرسوم", url=GRAPH_THEORY_URL), InlineKeyboardButton("📚 نماذج رياضية", url=MATH_MODELS_URL)],
            [InlineKeyboardButton("🔙 العودة للقائمة الرئيسية", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="📚 **حرات القسم:**", reply_markup=reply_markup, parse_mode="Markdown")

    elif query.data == "college_req":
        keyboard = [
            [InlineKeyboardButton("🩷 فيزياء 1", url=PHYSICS_1_URL), InlineKeyboardButton("🩷 فيزياء 2", url=PHYSICS_2_URL)],
            [InlineKeyboardButton("🩷 لاب الفيزياء", url=PHYSICS_LAB_URL), InlineKeyboardButton("🩷 لغة C++", url=CPP_URL)],
            [InlineKeyboardButton("🔙 العودة للقائمة الرئيسية", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="🩷 **متطلبات إجباري كلية:**", reply_markup=reply_markup, parse_mode="Markdown")

    elif query.data == "main_menu":
        keyboard = [
            [InlineKeyboardButton("🟡 مواد السنة الأولى", callback_data="year_1")],
            [InlineKeyboardButton("🟣 مواد السنة الثانية", callback_data="year_2")],
            [InlineKeyboardButton("🔘 مواد السنة الثالثة", callback_data="year_3")],
            [InlineKeyboardButton("🟤 مواد السنة الرابعة", callback_data="year_4")],
            [InlineKeyboardButton("📚 حرات القسم", callback_data="elective_dept")],
            [InlineKeyboardButton("🩷 إجباري كلية", callback_data="college_req")],
            [
                InlineKeyboardButton("📌 الأسماء الشائعة", callback_data="send_names_image"),
                InlineKeyboardButton("📊 العلامات والرموز", callback_data="send_marks_image")
            ],
            [InlineKeyboardButton("🌳 شجرة التخصص", callback_data="send_tree_image")],
            [InlineKeyboardButton("📂 مجلد المواد الشامل", url=DRIVE_GENERAL_URL)]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text="🏠 **القائمة الرئيسية:**", reply_markup=reply_markup, parse_mode="Markdown")

# البحث الفوري عبر الرسائل
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_query = update.message.text.strip()
    
    keyboard = [
        [InlineKeyboardButton("📂 فتح مجلد الدرايف الشامل", url=DRIVE_GENERAL_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"🔍 **نتيجة البحث:**\nوجدت طلبك بخصوص مادة (_{user_query}_).\n\n"
        f"يرجى الانتقال المباشر لمجلد الدرايف لتصفح كافة الملفات:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('materials', materials_link))
    application.add_handler(CommandHandler('tree', send_tree_image))
    application.add_handler(CommandHandler('marks', send_marks_image))
    application.add_handler(CommandHandler('names', send_names_image))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("🚀 بوت فريق إبسلون بالتعاون مع فريق إنفنتي يعمل الآن بالتعديلات الجديدة...")
    application.run_polling()