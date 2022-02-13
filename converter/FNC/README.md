# File Name Convertor

Convert all folder/file names, including convert to another Chinese (Traditional/Simplified Chinese), delete specific words.

### Installation
```
pip install -r requirements.txt
```
### Usage
##### Convert Chinese Filename
```
python main.py convert [opencc-mode] [paths..]
# python main.py convert s2t /Users/jerry/Document/资料1/ /Users/jerry/Document/资料2/
```
##### Remove specific word
```
python main.py remove [word] [paths..]
# python main.py remove "jerry" /Users/jerry/Document/jerry-data1/
# It will replace "jerry" to "" in all file/folder names of provided path
```

### OpenCC

| Mode | Description |
| ---- | ----------- |
| hk2s | 繁體中文 (香港) -> 簡體中文 |
| s2hk | 簡體中文 -> 繁體中文 (香港) |
| s2t | 簡體中文 -> 繁體中文 |
| s2tw | 簡體中文 -> 繁體中文 (台灣) |
| s2twp | 簡體中文 -> 繁體中文 (台灣, 包含慣用詞轉換) |
| t2hk | 繁體中文 -> 繁體中文 (香港) |
| t2s | 繁體中文 -> 簡體中文 |
| t2tw | 繁體中文 -> 繁體中文 (台灣) |
| tw2s | 繁體中文 (台灣) -> 簡體中文 |
| tw2sp | 繁體中文 (台灣) -> 簡體中文 (包含慣用詞轉換 ) |