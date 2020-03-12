from helium import *
from utils import *

# Api Docs: https://heliumhq.com/docs/api_documentation#python
def hacpai_checkin(account):
    start_chrome("https://hacpai.com", headless=False)
    go_to("https://hacpai.com/login")
    click(S("#verifyHacpaiIcon"))
    write(account["username"], S("#nameOrEmail"))
    write(account["password"], S("#loginPassword"))
    click(S("#loginBtn"))
    go_to("https://hacpai.com")
    go_to("https://hacpai.com/activity/checkin")
    if Text("今日签到获得").exists():
        print("今日已经签到. 👏")
    else:
        # click 领取今日签到奖励 button.
        click(S(".green"))
        print("今日成功签到. ✔︎")
    kill_browser()


if __name__ == "__main__":
    hacpai_account = get_config("hacpai.com")
    hacpai_checkin(hacpai_account)
