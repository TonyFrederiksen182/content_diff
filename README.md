content_diff.py

概要
---
引数で渡されたファイルの中身を比較するスクリプト  
第１引数：比較元  
第２引数：比較先  

使い方
---
python3 content_diff.py <比較元ファイル> <比較先ファイル>  

例）
$ echo -e "aaa\nbbb\nccc" > target.txt  
$ echo -e "ddd\naaa\nccc\nbbb" > reference.txt  
$ python3 content_diff.py target.txt reference.txt  
aaa: Found  
bbb: Found  
ccc: Found  
  

