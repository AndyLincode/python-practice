unicode_string = "中"
utf_bytes = unicode_string.encode()
print(utf_bytes)  # b'\xe4\xb8\xad'
result_string = utf_bytes.decode('utf-8')
print(result_string)  # 中
