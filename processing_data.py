from atexit import _run_exitfuncs
import csv
import glob
from json import load
import os

def read_data(path_data):

    '''
    Đọc dữ liệu trong một file csv
    input: path.csv
    output: danh sách label, content
    '''

    with open(path_data, encoding='utf8') as f:
        reader = csv.reader(f)
        count = 0
        list_content=[]
        for row in reader:
            if count >= 30000:
                list_content.append(row)
            count += 1
            if count == 35000:
                break
    return list_content

def load_data(root_path):

    '''
    Load toàn bộ dữ liệu từ các file csv
    input: path file chứa data
    output: danh sách label, content của toàn bộ từng file csv
    '''

    list_path = glob.glob(os.path.join(root_path, "*.csv"))
    list_all_content = []
    for path in list_path:
        print(path)
        list_content = read_data(path)
        list_all_content.append(list_content)

    return list_all_content

def replace_word(text):
    dictionary = [['Hok',' hk '," K "," Ko "," ko ",' kh '," k ", " không "], 
                  [" cử ", " của "], 
                  ['🤪','😬','☹️','😾','🤡','😁','🤩','😃','🤔','🤨','😀','💰','❤️','🌼','🐟','<','💞','👌','😆','🌶','😛','🤤','😋','😘','😚','😊','🥴','😓','🤧','💕','😍','"','👍','☺️','😈','🥺','🥰','🙆','💍','😩','🤣','🤦🏼‍','♂','🤕','😭','😑','@@','😞','😌','🤬','😂','🌚','🙂','😒',':',')','(','😢','😥','🙄','🥲',' ft ',' f ','  ','👎', ''], 
                  ['SP','Sp','sp', 'sản phẩm'], 
                  ['đunvs', 'đúng'], 
                  [" qc ", "quảng cáo"],
                  [' đk ',"đc","dc", "được"],
                  [" lểi ", "đểu"],
                  [' lói ', 'nói'],
                  ['Cl','qq','vl',' lồn ','lol','cc',' l ', ' *** '],
                  [' nma ',' nhưng mà '],
                  [' z đó ',' vậy đó '],
                  ['trơid',' tr ',' trời '],
                  ['mn',' MN ', ' mọi người '],
                  [' lm ',' làm '],
                  [' j ',' v ', 'vậy'],
                  [' ip ', 'iphone'],
                  ['vs', 'với'],
                  ['sz', 'size'],
                  ['nhma', 'nhưng mà'],
                  [' trc ', ' trước ']
                  ]

    for word in dictionary:
        for i in range (0, len(word) -1):
            re_word = word[len(word)-1]
            text = text.replace(word[i], re_word)
    return text

def check_text(text):
    list_word = text.split(" ")
    for word in list_word:

        if len(word)>5:
            return False

    if len(list_word) == 1:
        return False
    return True


def save_csv(root_path, list_content):
    path =root_path + '//data_clean.csv'
    with open(path, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        for row in list_content:
            writer.writerow(row)

if __name__ == "__main__":
    root_path = '.\\data'
    path_raw_data = root_path + '\\data_raw\\data_train_in_group'
    list_content = load_data(path_raw_data)
    index_content = 0
    new_list = []
    for i in range(0,len(list_content)):
        count = 0
        for j in range(0, len(list_content[i])):
            text = list_content[i][j][1]
            
            new_text = replace_word(text)

            if check_text(new_text):
                count+=1
                new_list.append([list_content[i][j][0],new_text])
        print("Số lượng lấy từ {} sao: {}".format(i + 1,count))
    print(new_list[0])
    save_csv(root_path, new_list)
    
