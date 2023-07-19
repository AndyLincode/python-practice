import pandas as pd
from collections import Counter


def count_words(files_path, sheet_name, column_name):
    # 讀取excel檔案
    df = pd.read_excel(files_path, sheet_name=sheet_name)
    # 將欄位組成一個字串
    words_str = " ".join(df[column_name].astype(str))
    # 算字母或符號出現幾次 回傳dict {'A': xxx, 'B': xxx, ...}
    word_count = Counter(words_str)
    print(word_count)
    return word_count


files_path = "models.xlsx"
sheet_name = "工作表1"
column_name = "A"

word_count = count_words(files_path, sheet_name, column_name)

for word, count in word_count.items():
    print(f"{word}: {count} 次")

# 將結果轉成DataFrame
result_df = pd.DataFrame(list(word_count.items()), columns=['word', 'count'])
# 寫入excel 建立一個sheet (COUNT_RESULT)
with pd.ExcelWriter(files_path, engine='openpyxl', mode='a') as writer:
    result_df.to_excel(writer, sheet_name='COUNT_RESULT', index=False)
