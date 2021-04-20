import requests

member_url = "https://www.yaozh.com/member/"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363"
}

cookies = "yaozh_jobstatus=kptta67UcJieW6zKnFSe2JyXnoaab5dpmp2HnKZxanJT1qeSoMZYoNdzbZtaqsuYkpSXhpyqn26fhtHCpquUrJrOnlNu1HCWlHNZkm5ik5e31bE38e1afF0f3A081773d0E84027E8eTmJuZlVmgqJ%2BYn4OnoKKdU5ysa2SUcIeVb2eRbGSZmpaanJiWWaCy602619a5cdaabdeb37b2902f2c26f11b; yaozh_uidhas=1; yaozh_user=982459%09xh3033; db_w_auth=816960%09xh3033; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1600217673%2C1600304651%2C1600426539; yaozh_mylogin=1600426551; _gat=1; _gid=GA1.2.1396660894.1600426539; yaozh_logintime=1600426548; UtzD_f52b_lastvisit=1600422949; UtzD_f52b_lastact=1600426549%09uc.php%09; _ga=GA1.2.747337930.1600304651; UtzD_f52b_auth=0b2cLTp9zQUha523O7jIiBm%2FokJDXCwjFgdqhsAG2Rgg3wzILpnuZYXqzttttHDTIIkb0kGvR4tTeBLIQ2eQNHhC%2BxI; yaozh_userId=982459; acw_tc=2f624a0416004265383927013e506430b405f11a7436524da8e0e1fa31ca70; UtzD_f52b_saltkey=Of9J6jf9; PHPSESSID=5sq481t4eqoknnn9bmf9i1q376; acw_tc=2f624a0416004265383927013e506430b405f11a7436524da8e0e1fa31ca70"
# cookies_dict = {
#     "yaozh_jobstatus":"kptta67UcJieW6zKnFSe2JyXnoaab5dpmp2HnKZxanJT1qeSoMZYoNdzbZtaqsuYkpSXhpyqn26fhtHCpquUrJrOnlNu1HCWlHNZkm5ik5e31bE38e1afF0f3A081773d0E84027E8eTmJuZlVmgqJ%2BYn4OnoKKdU5ysa2SUcIeVb2eRbGSZmpaanJiWWaCy602619a5cdaabdeb37b2902f2c26f11b",
#     "yaozh_uidhas":"1",
#     "yaozh_user":"982459%09xh3033",
#     "db_w_auth":"816960%09xh3033",
#     "Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94":"1600217673%2C1600304651%2C1600426539",
#     "yaozh_mylogin":"1600426551",
#     "_gat":"1",
#     "_gid":"GA1.2.1396660894.1600426539",
#     "yaozh_logintime":"1600426548",
#     "UtzD_f52b_lastvisit":"1600422949",
#     "UtzD_f52b_lastact":"1600426549%09uc.php%09",
#     "_ga":"GA1.2.747337930.1600304651",
#     "UtzD_f52b_auth":"0b2cLTp9zQUha523O7jIiBm%2FokJDXCwjFgdqhsAG2Rgg3wzILpnuZYXqzttttHDTIIkb0kGvR4tTeBLIQ2eQNHhC%2BxI",
#     "yaozh_userId":"982459",
#     "acw_tc":"2f624a0416004265383927013e506430b405f11a7436524da8e0e1fa31ca70",
#     "UtzD_f52b_saltkey":"Of9J6jf9",
#     "PHPSESSID":"5sq481t4eqoknnn9bmf9i1q376",
#     "acw_tc":"2f624a0416004265383927013e506430b405f11a7436524da8e0e1fa31ca70",
# }


cookies_dict = {}
cookies_list = cookies.split("; ")
print(cookies_list)
for cookie in cookies_list:
    cookies_dict[cookie.split("=")[0]] = cookie.split("=")[1]

response = requests.get(member_url, headers=headers, cookies=cookies_dict)

data = response.content.decode()

with open("cokkie.html", "w", encoding="utf-8") as f:
    f.write(data)