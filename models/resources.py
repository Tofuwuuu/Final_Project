"""
Everything in this file contains path/data from resources folder.
The developer must write everything resource-related here.
"""
import os
from PIL import Image

#base paths for different types of resources
_font_path = os.path.abspath("./resources/fonts") + "\\"
_image_path = os.path.abspath("./resources/images") + "\\"
_image_nav_path = _image_path + "nav-icons\\"

#global vars for caching resources that can be loaded
__image_cache = {}

class constants:
    WIN_WIDTH = 900
    WIN_HEIGHT = 600

class fonts:
    pass

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