from opencc import OpenCC
from abc import ABC, abstractmethod

MODE = ["hk2s", "s2hk", "s2t", "s2tw", "s2twp", "t2hk", "t2s", "t2tw", "tw2s", "tw2sp"]

class Fn:
    
    def __init__(self, args:list) -> None:
        try:
            self.selector = args[1]
            self.args = args[2::]
        except:
            print("FNC: arguments error")
        else:
            self.check()
        
    def check(self):
        Fnc.check(self.selector, self.args)
    
    def get_fnc(self):
        if self.selector == "convert":
            return CCFnc(mode=self.args[0])
        if self.selector == "remove":
            return RemoveFnc(replace_word=self.args[0])

class Fnc(ABC):

    @abstractmethod
    def convert_filename(self, old_filename):
        pass
    
    @staticmethod
    def check(selector:str, args:list):
        if selector not in ["convert", "remove"]:
            raise Exception("FNC [mode] not found")
        
        if selector == "convert":
            if len(args) < 2:
                raise Exception(f"FNC Arguments Error: {selector} [mode] [paths...]")
            if args[0] not in MODE:
                raise Exception(f"FNC {selector} [mode] not found")
        
        if selector == "remove":
            if len(args) < 2:
                raise Exception(f"FNC Arguments Error: {selector} [remove_word] [paths...]")
    
class CCFnc(Fnc):
    
    def __init__(self, mode:str) -> None:
        if mode not in MODE:
            raise Exception("[mode] not found")
        self.opencc = OpenCC(config=mode)
    
    def convert_filename(self, old_filename) -> str:
        new_filename = self.opencc.convert(old_filename)
        
        if len(new_filename)+3 <= len(old_filename):
            return old_filename, False
        return new_filename, True
    
class RemoveFnc(Fnc):
    
    def __init__(self, replace_word:str) -> None:
        self.replace_word = replace_word
    
    def convert_filename(self, old_filename:str):
        new_filename = old_filename.replace(self.replace_word, "")
        if old_filename == new_filename:
            return old_filename, False
        return new_filename, True