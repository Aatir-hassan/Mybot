# import json
# import os
# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# TOKEN = "8734169949:AAF4XcCYvjorqyJ9BrA4r9mV-RqqY6iR1RM"
# DATA_FILE = "data.json"

# # ---------- LOAD ----------
# if os.path.exists(DATA_FILE):
#     with open(DATA_FILE, "r") as f:
#         data = json.load(f)
# else:
#     data = {}

# def save_data():
#     with open(DATA_FILE, "w") as f:
#         json.dump(data, f)


# def get_user(user_id):
#     user_id = str(user_id)
#     if user_id not in data:
#         data[user_id] = {
#             "tasks": [],
#             "syllabus": [],
#             "completed": []
#         }
#     return data[user_id]


# # START
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("Welcome! Your personal study tracker 📚")


# # ADD TASK
# async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user = get_user(update.effective_user.id)

#     task = " ".join(context.args)
#     if task == "":
#         await update.message.reply_text("Write something after /add")
#         return

#     user["tasks"].append(task)
#     save_data()

#     await update.message.reply_text(f"Task added: {task} ✅")


# # LIST TASKS
# async def list_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user = get_user(update.effective_user.id)

#     if not user["tasks"]:
#         await update.message.reply_text("No tasks yet 📭")
#         return

#     await update.message.reply_text("\n".join(user["tasks"]))


# # DONE TASK
# async def done(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user = get_user(update.effective_user.id)

#     task = " ".join(context.args)

#     if task == "":
#         await update.message.reply_text("Write task to mark done")
#         return

#     if task in user["tasks"]:
#         user["tasks"].remove(task)

#         if task in user["syllabus"]:
#             user["completed"].append(task)

#         save_data()
#         await update.message.reply_text(f"Completed: {task} ✅")
#     else:
#         await update.message.reply_text("Task not found ❌")


# # SET SYLLABUS
# async def set_syllabus(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user = get_user(update.effective_user.id)

#     text = " ".join(context.args)

#     if text == "":
#         await update.message.reply_text("Send topics like: Physics Kinematics NLM")
#         return

#     user["syllabus"] = text.split()
#     user["completed"] = []

#     save_data()

#     await update.message.reply_text(f"Syllabus saved: {', '.join(user['syllabus'])}")


# # PROGRESS
# async def progress(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user = get_user(update.effective_user.id)

#     if not user["syllabus"]:
#         await update.message.reply_text("No syllabus set ❌")
#         return

#     total = len(user["syllabus"])
#     done_count = len([t for t in user["completed"] if t in user["syllabus"]])

#     percent = int((done_count / total) * 100)

#     await update.message.reply_text(
#         f"Progress: {percent}% ({done_count}/{total}) 📊"
#     )


# # APP
# app = ApplicationBuilder().token(TOKEN).build()

# app.add_handler(CommandHandler("start", start))
# app.add_handler(CommandHandler("add", add))
# app.add_handler(CommandHandler("list", list_tasks))
# app.add_handler(CommandHandler("done", done))
# app.add_handler(CommandHandler("syllabus", set_syllabus))
# app.add_handler(CommandHandler("progress", progress))

# print("Bot running...")
# app.run_polling()


import json
import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ⚠️ IMPORTANT: Replace this with your NEW token
TOKEN = "YOUR_NEW_BOT_TOKEN"
DATA_FILE = "data.json"

# ---------- LOAD ----------
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
else:
    data = {}

def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def get_user(user_id):
    user_id = str(user_id)
    if user_id not in data:
        data[user_id] = {
            "tasks": [],
            "syllabus": [],
            "completed": []
        }
    return data[user_id]

# ---------- COMMANDS ----------

# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Your personal study tracker 📚")

# ADD TASK
async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = get_user(update.effective_user.id)

    task = " ".join(context.args)
    if task == "":
        await update.message.reply_text("Write something after /add")
        return

    user["tasks"].append(task)
    save_data()

    await update.message.reply_text(f"Task added: {task} ✅")

# LIST TASKS
async def list_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = get_user(update.effective_user.id)

    if not user["tasks"]:
        await update.message.reply_text("No tasks yet 📭")
        return

    await update.message.reply_text("\n".join(user["tasks"]))

# DONE TASK
async def done(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = get_user(update.effective_user.id)

    task = " ".join(context.args)

    if task == "":
        await update.message.reply_text("Write task to mark done")
        return

    if task in user["tasks"]:
        user["tasks"].remove(task)

        if task in user["syllabus"]:
            user["completed"].append(task)

        save_data()
        await update.message.reply_text(f"Completed: {task} ✅")
    else:
        await update.message.reply_text("Task not found ❌")

# SET SYLLABUS
async def set_syllabus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = get_user(update.effective_user.id)

    text = " ".join(context.args)

    if text == "":
        await update.message.reply_text("Send topics like: Physics Kinematics NLM")
        return

    user["syllabus"] = text.split()
    user["completed"] = []

    save_data()

    await update.message.reply_text(f"Syllabus saved: {', '.join(user['syllabus'])}")

# PROGRESS
async def progress(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = get_user(update.effective_user.id)

    if not user["syllabus"]:
        await update.message.reply_text("No syllabus set ❌")
        return

    total = len(user["syllabus"])
    done_count = len([t for t in user["completed"] if t in user["syllabus"]])

    percent = int((done_count / total) * 100)

    await update.message.reply_text(
        f"Progress: {percent}% ({done_count}/{total}) 📊"
    )

# ---------- TELEGRAM APP ----------
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("add", add))
app.add_handler(CommandHandler("list", list_tasks))
app.add_handler(CommandHandler("done", done))
app.add_handler(CommandHandler("syllabus", set_syllabus))
app.add_handler(CommandHandler("progress", progress))

# ---------- FLASK APP (FOR RENDER) ----------
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Bot is running ✅"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(host="0.0.0.0", port=port)

# ---------- RUN BOT ----------
def run_bot():
    print("Bot running...")
    app.run_polling()

# ---------- START BOTH ----------
if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    run_flask()