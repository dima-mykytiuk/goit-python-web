import shutil
from pathlib import Path
import os
from sys import argv, platform
import re
from threading import RLock, Thread


class ThreadMoveFiles(Thread):
    def __init__(self, path, item_name, file_type, folder_name, main_path, locker):
        super().__init__()
        self.path = path
        self.item_name = item_name
        self.file_type = file_type
        self.folder_name = folder_name
        self.main_path = main_path
        self.locker = locker
        
    def run(self):
        self.locker.acquire()
        check_exist_path = os.path.exists(f'{self.main_path}{folder_sep}{self.folder_name}{folder_sep}{self.item_name}')
        if self.file_type in files_type.get(self.folder_name) and not check_exist_path:
            path_from = f'{self.path}{folder_sep}{self.item_name}'
            to_path = f'{self.main_path}{folder_sep}{self.folder_name}{folder_sep}{self.item_name}'
            shutil.move(path_from, to_path)
        self.locker.release()


class ThreadRemove(Thread):
    def __init__(self, path, locker):
        super().__init__()
        self.path = path
        self.locker = locker
    
    def run(self):
        self.locker.acquire()
        shutil.rmtree(self.path)
        self.locker.release()


class ThreadMoveArch(Thread):
    def __init__(self, path_from, path_to_unpack, locker):
        super().__init__()
        self.path_from = path_from
        self.path_to_unpack = path_to_unpack
        self.locker = locker
    
    def run(self):
        self.locker.acquire()
        shutil.unpack_archive(self.path_from, self.path_to_unpack)
        os.remove(self.path_from)
        self.locker.release()


def normalize(name):
    table_symbols = ('абвгґдеєжзиіїйклмнопрстуфхцчшщюяыэАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЮЯЫЭьъЬЪ', (
        'a', 'b', 'v', 'h', 'g', 'd', 'e', 'ye', 'zh', 'z', 'y', 'i', 'yi', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's',
        't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', 'yu', 'ya', 'y', 'ye', 'A', 'B', 'V', 'H', 'G', 'D', 'E', 'Ye',
        'Zh', 'Z', 'Y', 'I', 'Yi', 'Y', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'F', 'KH', 'TS', 'CH', 'SH',
        'SHCH', 'YU', 'YA', 'Y', 'YE', '_', '_', '_', '_', 'a', 'b', 'v', 'h', 'g', 'd', 'e', 'ye', 'zh', 'z', 'y', 'i',
        'yi', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'Kh', 'Ts', 'Ch', 'Sh', 'Shch', 'Yu', 'Aa',
        'y', 'Ye', '_', '_', '_', '_'))
    map_cyr_to_latin = {ord(src): dest for src, dest in zip(*table_symbols)}
    rx = re.compile(r"[^\w_]")
    return rx.sub('_', name.translate(map_cyr_to_latin))


def make_folders():
    for x in range(0, len(folder_list)):
        if not os.path.exists(f'{_dir}{folder_sep}{folder_list[x]}'):
            os.makedirs(f'{_dir}{folder_sep}{folder_list[x]}')


def find_files_and_sort(path):
    lock = RLock()
    for item_name in os.listdir(path):
        path_from = f'{path}{folder_sep}{item_name}'
        if item_name not in folder_list and os.path.isfile(path_from) and item_name != '.DS_Store':
            file_type = item_name.split('.')[-1]
            rem_suffix = item_name.removesuffix(f'.{file_type}')
            path_to_unpack = f'{main_path}{folder_sep}archives{folder_sep}{rem_suffix}'
            for folder_name in folder_list:
                if folder_name != 'archives':
                    move = ThreadMoveFiles(path, item_name, file_type, folder_name, main_path, lock)
                    move.start()
                elif file_type in files_type.get('archives') and not os.path.exists(path_to_unpack):
                    move_arch = ThreadMoveArch(path_from, path_to_unpack, lock)
                    move_arch.start()
        elif item_name not in folder_list and os.path.isdir(path_from):
            find_files_and_sort(path_from)


def rename_files_and_folders(path):
    for folder_item in os.listdir(path):
        path_to_folder = f'{path}{folder_sep}{folder_item}'
        path_after_normalize = f'{path}{folder_sep}{normalize(folder_item)}'
        file_type = folder_item.split('.')[-1]
        rem_suffix = folder_item.removesuffix(f'.{file_type}')
        normalize_name = f'{normalize(rem_suffix)}.{file_type}'
        if os.path.isfile(path_to_folder) and folder_item != '.DS_Store':
            shutil.move(path_to_folder, f'{path}{folder_sep}{normalize_name}')
        elif os.path.isdir(path_to_folder):
            shutil.move(path_to_folder, path_after_normalize)
            rename_files_and_folders(path_after_normalize)


def remove_empty_folders(path_abs):
    lock = RLock()
    walk = list(os.walk(path_abs))
    for path, folders, folders_items in walk[::-1]:
        folder_name = path.split(folder_sep)[-1]
        len_0 = len(os.listdir(path)) == 0 and folder_name not in folder_list
        len_1 = len(os.listdir(path)) == 1 and folder_name not in folder_list and '.DS_Store' in folders_items
        if len_0 or len_1:
            remove = ThreadRemove(path, lock)
            remove.start()


if __name__ == '__main__':
    if platform == "win32":
        folder_sep = '//'
    else:
        folder_sep = '/'
    _dir = Path(argv[1])
    main_path = _dir
    folder_list = ['images', 'documents', 'audio', 'video', 'archives']
    files_type = {
        'video': ['avi', 'mp4', 'mov', 'mkv'],
        'audio': ['mp3', 'ogg', 'wav', 'amr'],
        'images': ['jpeg', 'png', 'jpg', 'svg'],
        'archives': ['zip', 'gz', 'tar'],
        'documents': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'],
    }
    make_folders()
    rename_files_and_folders(str(_dir))
    find_files_and_sort(str(_dir))
    remove_empty_folders(_dir)
