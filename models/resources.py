"""
Everything in this file contains path/data from resources folder.
The developer must write everything resource-related here.
"""
import os
from PIL import Image

#base paths for different types of resources
_image_path = os.path.abspath("./resources/images") + "\\"
_image_nav_path = _image_path + "nav-icons\\"

#global vars for caching resources that can be loaded
__image_cache = {}

class constants:
    HOUR_VALUES = ["08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
    MINUTE_VALUES = ["00", "15", "30", "45"]

    PLACEHOLDER_TEACHER = "Choose a teacher"
    PLACEHOLDER_DATE = 'Pick a date'
    PLACEHOLDER_TIME = 'Pick a time'
    PLACEHOLDER_TIME_START = 'Input session start'
    PLACEHOLDER_TIME_END = 'Input session end'


    THEME_GREEN = ("#95D5B2", "#081c15")
    THEME_YELLOW = ("#Fdf0d5", "#081c15")
    THEME_BLUE = ("#DFE9F1", "gray")
    THEME_DARKGREEN = ("#80B699", "#1F664D")
    THEME_TEXT = ("#2B9348", "#Fdf0d5")
    THEME_DEFAULT = ('white', '#242424')
    THEME_GRAY = ("gray75", "gray25")
    THEME_BNW = ('black', 'white')

    WIN_SMALL_WIDTH = 900
    WIN_SMALL_HEIGHT = 600
    WIN_WIDTH = 1200
    WIN_HEIGHT = 800

class regex:
    REGEX_EMAIL = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'

class fonts:
    POPPINS = "Poppins"

class images:

    class nav_ico:
        home_dark = _image_nav_path + "home-dark.png"
        home_light = _image_nav_path + "home-light.png"
        faculty_dark = _image_nav_path + "faculty-dark.png"
        faculty_light = _image_nav_path + "faculty-light.png"
        calendar_dark = _image_nav_path + "calendar-dark.png"
        calendar_light = _image_nav_path + "calendar-light.png"
        consultation_dark = _image_nav_path + "consultation-dark.png"
        consultation_light = _image_nav_path + "consultation-light.png"
        settings_dark = _image_nav_path + "settings-dark.png"
        settings_light = _image_nav_path + "settings-light.png"
        menu_dark = _image_nav_path + "menu-dark.png"
        menu_light = _image_nav_path +  "menu-light.png"
        alert_notif_dark = _image_nav_path +  "alert-notif-dark.png"
        alert_notif_light = _image_nav_path +  "alert-notif-light.png"
        notif_dark = _image_nav_path +  "notif-dark.png"
        notif_light = _image_nav_path +  "notif-light.png"
        list_task_dark = _image_nav_path +  "list-task-dark.png"
        list_task_light = _image_nav_path +  "list-task-light.png"
        history_dark = _image_nav_path +  "history-dark.png"
        history_light = _image_nav_path +  "history-light.png"
        filter_dark = _image_nav_path +  "filter-dark.png"
        filter_light = _image_nav_path +  "filter-light.png"
        sort_dark = _image_nav_path +  "sort-dark.png"
        sort_light = _image_nav_path +  "sort-light.png"
        user_profile_dark = _image_nav_path +  "user-profile-dark.png"
        user_profile_light = _image_nav_path +  "user-profile-light.png"
        logout_dark = _image_nav_path +  "logout-dark.png"
        logout_light = _image_nav_path +  "logout-light.png"
        search_dark = _image_nav_path + "search-dark.png"
        search_light = _image_nav_path + "search-light.png"
        go_next_dark  = _image_nav_path + "go-next-dark.png"
        go_next_light  = _image_nav_path + "go-next-light.png"
        add_dark = _image_nav_path + "add-dark.png"
        add_light = _image_nav_path + "add-light.png"
        check_dark = _image_nav_path + "check-dark.png"
        check_light = _image_nav_path + "check-light.png"
        deny_dark = _image_nav_path + "deny-dark.png"
        deny_light = _image_nav_path + "deny-light.png"
        pending_dark = _image_nav_path + "pending-dark.png"
        pending_light = _image_nav_path + "pending-light.png"

    #ico
    window_icon = _image_path + "window-icon.ico"

    #png
    customtkinter_logo_single = _image_path + "CustomTkinter_logo_single.png"
    poster = _image_path + "Poster.png"
    image_icon_light = _image_path + "image_icon_light.png"
    home_dark = _image_path + "home_dark.png"
    home_light = _image_path + "home_light.png"
    chat_dark = _image_path + "chat_dark.png"
    chat_light = _image_path + "chat_light.png"
    add_user_dark = _image_path + "add_user_dark.png"
    add_user_light = _image_path + "add_user_light.png"
    cvsu_consult_logo = _image_path + "CvSU Consult Logo.png"
    login_bg = _image_path + "login_bg.png"

def fetch_image(path: str) -> Image:
    """
    Fetch Image using path as a key. If the image is already loaded,
    the loaded image will be returned instead of loading another instance
    the image.
    """
    #check whether image is in cache or not
    if(path not in __image_cache):
        __image_cache[path] = Image.open(path)
        __image_cache[path].load()  #load image

    return __image_cache[path]
    
def Dispose():
    for k in __image_cache:
        __image_cache[k].close()

    __image_cache.clear()