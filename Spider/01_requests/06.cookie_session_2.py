
import requests

def main():

    # session = requests.session()
    post_url = "http://www.renren.com/PLogin.do"
    post_headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "Cookie":"anonymid=jqevq93zwqvvhs; depovince=GW; _r01_=1; JSESSIONID=abc0mItCOXmxI8FBiInGw; ick_login=f1af75ef-cfe3-4af9-af54-e58452e529f6; ick=e4b0d79e-7024-473c-8ce4-ea4b993f680f; XNESSESSIONID=39fe09866f75; jebecookies=1b47c69f-e6ed-469c-b763-6430f7b1ebd2|||||; _de=292313AA6F309B3C75AC6BB1D7847ADE; p=e801b4b0b153fec6e258c1b5917688da4; first_login_flag=1; ln_uact=17623702688; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=c55af692f435895e0a7889e16c8603d84; societyguester=c55af692f435895e0a7889e16c8603d84; id=969328524; xnsid=f1511da4; ver=7.0; loginfrom=null; wp_fold=0; vip=1; arp_scroll_position=0"}

    # post_data = {"email":"17623702688",
    #              "password":"3NR,/nen8P,Wr2qf,"}
    # session.post(post_url, headers= post_headers, data= post_data)
    # r = session.get("http://www.renren.com/969328524", headers = post_headers )

    r = requests.get("http://www.renren.com/969328524", headers= post_headers)


    with open('renren1.html', "w", encoding="utf8") as f:
        f.write(r.content.decode())


if __name__ == "__main__":
    main()