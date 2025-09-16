# clear_data.py
import os
import shutil
from appdirs import user_data_dir

APP_NAME = "Autolinky"
APP_AUTHOR = "Mamdouh"

def clear_all_data():
    """يمسح الكريدينشالز وكوكيز LinkedIn"""
    # مسح الكريدينشالز
    config_file = os.path.join(user_data_dir(APP_NAME, APP_AUTHOR), "config.json")
    if os.path.exists(config_file):
        os.remove(config_file)
        print("✔ Credentials deleted.")

    # مسح كوكيز LinkedIn
    session_dir = os.path.join(user_data_dir(APP_NAME, APP_AUTHOR), "chrome_profile")
    if os.path.exists(session_dir):
        shutil.rmtree(session_dir)
        print("✔ LinkedIn cookies deleted.")

    print("✅ All data cleared!")

if __name__ == "__main__":
    confirm = input("Do you really want to delete all data? (y/n): ").lower()
    if confirm == "y":
        clear_all_data()
    else:
        print("❌ Operation cancelled.")
