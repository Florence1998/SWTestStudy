from encap_demo import Account

print("1")
print(Account._username)  # 不建议。输入.后，不会有该保护属性联想。且强制使用后会有波浪线提示
