
import requests

def main():

    session = requests.session()
    post_url = "http://www.renren.com/PLogin.do"
    post_headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
    post_data = {"email":"17623702688",
                 "password":"3NR,/nen8P,Wr2qf,"}

    session.post(post_url, headers= post_headers, data= post_data)

    r = session.get("http://www.renren.com/969328524", headers = post_headers )

    with open('renren.html', "w", encoding="utf8") as f:
        f.write(r.content.decode())


if __name__ == "__main__":
    main()