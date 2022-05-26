# pylint: disable=too-many-arguments
"""Imports for sorter"""
import shutil
from pathlib import Path
import os
from sys import platform
import re


def normalize(name):
    """Func to normalize values"""
    table_symbols = (
        "абвгґдеєжзиіїйклмнопрстуфхцчшщюяыэАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЮЯЫЭьъЬЪ",
        (
            "a",
            "b",
            "v",
            "h",
            "g",
            "d",
            "e",
            "ye",
            "zh",
            "z",
            "y",
            "i",
            "yi",
            "y",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "r",
            "s",
            "t",
            "u",
            "f",
            "kh",
            "ts",
            "ch",
            "sh",
            "shch",
            "yu",
            "ya",
            "y",
            "ye",
            "A",
            "B",
            "V",
            "H",
            "G",
            "D",
            "E",
            "Ye",
            "Zh",
            "Z",
            "Y",
            "I",
            "Yi",
            "Y",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "R",
            "S",
            "T",
            "U",
            "F",
            "KH",
            "TS",
            "CH",
            "SH",
            "SHCH",
            "YU",
            "YA",
            "Y",
            "YE",
            "_",
            "_",
            "_",
            "_",
            "a",
            "b",
            "v",
            "h",
            "g",
            "d",
            "e",
            "ye",
            "zh",
            "z",
            "y",
            "i",
            "yi",
            "y",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "r",
            "s",
            "t",
            "u",
            "f",
            "Kh",
            "Ts",
            "Ch",
            "Sh",
            "Shch",
            "Yu",
            "Aa",
            "y",
            "Ye",
            "_",
            "_",
            "_",
            "_",
        ),
    )
    map_cyr_to_latin = {ord(src): dest for src, dest in zip(*table_symbols)}
    reject_x = re.compile(r"[^\w_]")
    return reject_x.sub("_", name.translate(map_cyr_to_latin))


def make_folders(_dir, folder_list, folder_sep):
    """Func to make folders"""
    for step in enumerate(folder_list):
        if not os.path.exists(f"{_dir}{folder_sep}{folder_list[step[0]]}"):
            os.makedirs(f"{_dir}{folder_sep}{folder_list[step[0]]}")


def move_files(
    path, item_name, file_type, folder_name, base_path_to, folder_sep, files_type
):
    """Func to move files"""
    path_str = f"{base_path_to}{folder_sep}{folder_name}{folder_sep}{item_name}"
    check_exist_path = os.path.exists(path_str)
    if file_type in files_type.get(folder_name) and not check_exist_path:
        path_from = f"{path}{folder_sep}{item_name}"
        to_path = f"{base_path_to}{folder_sep}{folder_name}{folder_sep}{item_name}"
        shutil.move(path_from, to_path)


def find_files_and_sort(path, main_path, folder_list, folder_sep, files_type):
    """Func to find and sort files"""
    for item_name in os.listdir(path):
        path_from = f"{path}{folder_sep}{item_name}"
        if (
            item_name not in folder_list
            and os.path.isfile(path_from)
            and item_name != ".DS_Store"
        ):
            file_type = item_name.split(".")[-1]
            rem_suffix = item_name.removesuffix(f".{file_type}")
            path_to_unpack = f"{main_path}{folder_sep}archives{folder_sep}{rem_suffix}"
            for folder_name in folder_list:
                if folder_name != "archives":
                    move_files(
                        path,
                        item_name,
                        file_type,
                        folder_name,
                        main_path,
                        folder_sep,
                        files_type,
                    )
                elif file_type in files_type.get("archives") and not os.path.exists(
                    path_to_unpack
                ):
                    shutil.unpack_archive(path_from, path_to_unpack)
                    os.remove(path_from)
        elif item_name not in folder_list and os.path.isdir(path_from):
            find_files_and_sort(
                path_from, main_path, folder_list, folder_sep, files_type
            )


def rename_files_and_folders(path, folder_sep):
    """Func to rename files and folders"""
    for folder_item in os.listdir(path):
        path_to_folder = f"{path}{folder_sep}{folder_item}"
        path_after_normalize = f"{path}{folder_sep}{normalize(folder_item)}"
        file_type = folder_item.split(".")[-1]
        rem_suffix = folder_item.removesuffix(f".{file_type}")
        normalize_name = f"{normalize(rem_suffix)}.{file_type}"
        if os.path.isfile(path_to_folder) and folder_item != ".DS_Store":
            shutil.move(path_to_folder, f"{path}{folder_sep}{normalize_name}")
        elif os.path.isdir(path_to_folder):
            shutil.move(path_to_folder, path_after_normalize)
            rename_files_and_folders(path_after_normalize, folder_sep)


def remove_empty_folders(path_abs, folder_list, folder_sep):
    """Func to remove empty folders"""
    walk = list(os.walk(path_abs))
    for path, _, folders_items in walk[::-1]:
        folder_name = path.split(folder_sep)[-1]
        len_0 = len(os.listdir(path)) == 0 and folder_name not in folder_list
        len_1 = len(os.listdir(path)) == 1 and folder_name not in folder_list
        if len_0 or len_1 and ".DS_Store" in folders_items:
            shutil.rmtree(path)


def sort(_dir: str) -> str:
    """Func to call all functions step by step"""
    folder_sep = "//" if platform == "win32" else "/"
    _dir = Path(_dir)
    main_path = _dir
    if not os.path.exists(main_path):
        return "No such directory."
    folder_list = ["images", "documents", "audio", "video", "archives"]
    files_type = {
        "video": ["avi", "mp4", "mov", "mkv"],
        "audio": ["mp3", "ogg", "wav", "amr"],
        "images": ["jpeg", "png", "jpg", "svg"],
        "archives": ["zip", "gz", "tar"],
        "documents": ["doc", "docx", "txt", "pdf", "xlsx", "pptx"],
    }
    make_folders(_dir, folder_list, folder_sep)
    rename_files_and_folders(str(_dir), folder_sep)
    find_files_and_sort(str(_dir), main_path, folder_list, folder_sep, files_type)
    remove_empty_folders(_dir, folder_list, folder_sep)
    return "Successfully sorted"
