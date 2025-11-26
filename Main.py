from datetime import *
import json
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup, KeyboardButton
from aiogram import F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.types import CallbackQuery
from Units.Classes import *

def add_user(user_id):
    filepath = "/data/all_users.json"

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = f.read().strip()
            if not data:
                all_users = []
            else:
                all_users = json.loads(data)
                if not isinstance(all_users, list):
                    all_users = []
    except (OSError, json.JSONDecodeError, ValueError):
        all_users = []

    
    if user_id not in all_users:
        all_users.append(user_id)

        
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(all_users, f, ensure_ascii=False, indent=2)

        return "added"
    
    return "already exists"
    

    return
def main():
    print(add_user("admin"))