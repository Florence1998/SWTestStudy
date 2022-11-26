"""
邓布利多将他的旧个人电话簿备份为文本文件。他可以在文件的每一行找到电话号码（格式为+X-abc-def-ghij，其中X代表一个或两个数字）、< >括起来的是姓名，剩余为地址信息。

不幸的是，一切都是混杂的，事情并不总是按同一顺序进行；部分行中充斥着非字母数字字符（除了内部的电话号码和姓名）。

邓布利多的电话簿线路示例：

“/+1-541-754-3010 156 Alphand_St.<J Steeve>\n”
“133，Green，Rd.<E Kustur>NY-56423；+1-541-914-3010！\n"
“<Anastasia>+48-421-674-8974 Via Quirinal Roma\n”
你能帮邓布利多做一个程序吗？给定他的电话簿中的行数和电话号码num，它会返回这个号码的字符串：“phone=>num，Name=>Name，Address=>Address”

例如:
s = "/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"

phone(s, "1-541-754-3010") should return "Phone => 1-541-754-3010, Name => J Steeve, Address => 156 Alphand St."
如果在文本中找到多个人使用同一个电话号码，则返回 : "Error => Too many people: phone_num"
如果在文本中未找到电话号则返回: "Error => Not found: phone_num"
题目难度：一般
题目来源： Phone Directory | Codewars 1

def phone(strng: str, num: str) -> str:
    # your code
    return

dr = ("/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010;\n"
"+1-541-984-3012 <P Reed> /PO Box 530; Pollocksville, NC-28573\n :+1-321-512-2222 <Paul Dive> Sequoia Alley PQ-67209\n"
"+1-741-984-3090 <Peter Reedgrave> _Chicago\n :+1-921-333-2222 <Anna Stevens> Haramburu_Street AA-67209\n"
"+1-111-544-8973 <Peter Pan> LA\n +1-921-512-2222 <Wilfrid Stevens> Wild Street AA-67209\n"
"<Peter Gone> LA ?+1-121-544-8974 \n <R Steell> Quora Street AB-47209 +1-481-512-2222!\n"
"<Arthur Clarke> San Antonio $+1-121-504-8974 TT-45120\n <Ray Chandler> Teliman Pk. !+1-681-512-2222! AB-47209,\n"
"<Sophia Loren> +1-421-674-8974 Bern TP-46017\n <Peter O'Brien> High Street +1-908-512-2222; CC-47209\n"
"<Anastasia> +48-421-674-8974 Via Quirinal Roma\n <P Salinger> Main Street, +1-098-512-2222, Denver\n"
"<C Powel> *+19-421-674-8974 Chateau des Fosses Strasbourg F-68000\n <Bernard Deltheil> +1-498-512-2222; Mount Av.  Eldorado\n"
"+1-099-500-8000 <Peter Crush> Labrador Bd.\n +1-931-512-4855 <William Saurin> Bison Street CQ-23071\n"
"<P Salinge> Main Street, +1-098-512-2222, Denve\n")

assert phone(dr, "48-421-674-8974") == "Phone => 48-421-674-8974, Name => Anastasia, Address => Via Quirinal Roma"
assert phone(dr, "1-921-512-2222") == "Phone => 1-921-512-2222, Name => Wilfrid Stevens, Address => Wild Street AA-67209"
assert phone(dr, "1-908-512-2222") == "Phone => 1-908-512-2222, Name => Peter O'Brien, Address => High Street CC-47209"
assert phone(dr, "1-541-754-3010") == "Phone => 1-541-754-3010, Name => J Steeve, Address => 156 Alphand St."
assert phone(dr, "1-121-504-8974") == "Phone => 1-121-504-8974, Name => Arthur Clarke, Address => San Antonio TT-45120"
assert phone(dr, "1-498-512-2222") == "Phone => 1-498-512-2222, Name => Bernard Deltheil, Address => Mount Av. Eldorado"
assert phone(dr, "1-098-512-2222") == "Error => Too many people: 1-098-512-2222"
assert phone(dr, "5-555-555-5555") == "Error => Not found: 5-555-555-5555"

"""phone(strng: str, num: str) -> str:
    # your code
    return

dr = ("/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010;\n"
"+1-541-984-3012 <P Reed> /PO Box 530; Pollocksville, NC-28573\n :+1-321-512-2222 <Paul Dive> Sequoia Alley PQ-67209\n"
"+1-741-984-3090 <Peter Reedgrave> _Chicago\n :+1-921-333-2222 <Anna Stevens> Haramburu_Street AA-67209\n"
"+1-111-544-8973 <Peter Pan> LA\n +1-921-512-2222 <Wilfrid Stevens> Wild Street AA-67209\n"
"<Peter Gone> LA ?+1-121-544-8974 \n <R Steell> Quora Street AB-47209 +1-481-512-2222!\n"
"<Arthur Clarke> San Antonio $+1-121-504-8974 TT-45120\n <Ray Chandler> Teliman Pk. !+1-681-512-2222! AB-47209,\n"
"<Sophia Loren> +1-421-674-8974 Bern TP-46017\n <Peter O'Brien> High Street +1-908-512-2222; CC-47209\n"
"<Anastasia> +48-421-674-8974 Via Quirinal Roma\n <P Salinger> Main Street, +1-098-512-2222, Denver\n"
"<C Powel> *+19-421-674-8974 Chateau des Fosses Strasbourg F-68000\n <Bernard Deltheil> +1-498-512-2222; Mount Av.  Eldorado\n"
"+1-099-500-8000 <Peter Crush> Labrador Bd.\n +1-931-512-4855 <William Saurin> Bison Street CQ-23071\n"
"<P Salinge> Main Street, +1-098-512-2222, Denve\n")

assert phone(dr, "48-421-674-8974") == "Phone => 48-421-674-8974, Name => Anastasia, Address => Via Quirinal Roma"
assert phone(dr, "1-921-512-2222") == "Phone => 1-921-512-2222, Name => Wilfrid Stevens, Address => Wild Street AA-67209"
assert phone(dr, "1-908-512-2222") == "Phone => 1-908-512-2222, Name => Peter O'Brien, Address => High Street CC-47209"
assert phone(dr, "1-541-754-3010") == "Phone => 1-541-754-3010, Name => J Steeve, Address => 156 Alphand St."
assert phone(dr, "1-121-504-8974") == "Phone => 1-121-504-8974, Name => Arthur Clarke, Address => San Antonio TT-45120"
assert phone(dr, "1-498-512-2222") == "Phone => 1-498-512-2222, Name => Bernard Deltheil, Address => Mount Av. Eldorado"
assert phone(dr, "1-098-512-2222") == "Error => Too many people: 1-098-512-2222"
assert phone(dr, "5-555-555-5555") == "Error => Not found: 5-555-555-5555"