import ctypes
from ctypes import wintypes
import os
from typing import Optional

# Structure for Windows File Dialogs
class OPENFILENAMEW(ctypes.Structure):
    _fields_ = [
        ("lStructSize", wintypes.DWORD),
        ("hwndOwner", wintypes.HWND),
        ("hInstance", wintypes.HINSTANCE),
        ("lpstrFilter", wintypes.LPCWSTR),
        ("lpstrCustomFilter", wintypes.LPWSTR),
        ("nMaxCustFilter", wintypes.DWORD),
        ("nFilterIndex", wintypes.DWORD),
        ("lpstrFile", wintypes.LPWSTR),
        ("nMaxFile", wintypes.DWORD),
        ("lpstrFileTitle", wintypes.LPWSTR),
        ("nMaxFileTitle", wintypes.DWORD),
        ("lpstrInitialDir", wintypes.LPCWSTR),
        ("lpstrTitle", wintypes.LPCWSTR),
        ("Flags", wintypes.DWORD),
        ("nFileOffset", wintypes.WORD),
        ("nFileExtension", wintypes.WORD),
        ("lpstrDefExt", wintypes.LPCWSTR),
        ("lCustData", wintypes.LPARAM),
        ("lpfnHook", ctypes.c_void_p),
        ("lpTemplateName", wintypes.LPCWSTR),
        ("pvReserved", ctypes.c_void_p),
        ("dwReserved", wintypes.DWORD),
        ("FlagsEx", wintypes.DWORD),
    ]

OFN_FILEMUSTEXIST = 0x00001000
OFN_PATHMUSTEXIST = 0x00000800
OFN_OVERWRITEPROMPT = 0x00000002

def _show_dialog(title: str, filter_str: str, default_ext: str, save: bool = False) -> Optional[str]:
    """Internal helper to show Windows native file dialog."""
    # Initialize the structure
    ofn = OPENFILENAMEW()
    ofn.lStructSize = ctypes.sizeof(OPENFILENAMEW)
    
    # Buffer for the selected file path
    buf = ctypes.create_unicode_buffer(1024)
    ofn.lpstrFile = ctypes.cast(buf, wintypes.LPWSTR)
    ofn.nMaxFile = 1024
    
    ofn.lpstrTitle = title
    ofn.lpstrFilter = filter_str.replace('|', '\0') + '\0\0'
    ofn.lpstrDefExt = default_ext
    
    if save:
        ofn.Flags = OFN_PATHMUSTEXIST | OFN_OVERWRITEPROMPT
        success = ctypes.windll.comdlg32.GetSaveFileNameW(ctypes.byref(ofn))
    else:
        ofn.Flags = OFN_FILEMUSTEXIST | OFN_PATHMUSTEXIST
        success = ctypes.windll.comdlg32.GetOpenFileNameW(ctypes.byref(ofn))
    
    if success:
        return buf.value
    return None

def get_open_file_path(title: str = "Select Dataset", filter_str: str = "CSV Files (*.csv)|*.csv|All Files (*.*)|*.*") -> Optional[str]:
    """Show native 'Open File' dialog."""
    return _show_dialog(title, filter_str, "csv", save=False)

def get_save_file_path(title: str = "Save Models", filter_str: str = "Text Files (*.txt)|*.txt|Markdown Files (*.md)|*.md", default_ext: str = "txt") -> Optional[str]:
    """Show native 'Save File As' dialog."""
    return _show_dialog(title, filter_str, default_ext, save=True)
