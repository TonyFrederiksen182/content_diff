import sys

# 引数チェック
argc = len(sys.argv)
if argc != 3:
    print('usage: python3 %s <target file> <reference file>' % sys.argv[0])
    quit()

# 引数で指定されたファイルをオープン
with open(sys.argv[1], 'r') as f_target:
    lines_target = f_target.readlines()

with open(sys.argv[2], 'r') as f_ref:
    lines_ref    = f_ref.readlines()

# 比較元の一行が比較先に含まれているかチェック
for line_target in lines_target:
    print(line_target.rstrip('\n') + ': ', end='')
    for line_ref in lines_ref:
        if line_target == line_ref:
            print('Found')
            break
    else:
        print('Not found')

