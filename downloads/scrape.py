import cfscrape
import subprocess

def main():
    links_file = open('dl_client.txt', 'r')
    lines = links_file.readlines()

    scraper = cfscrape.create_scraper()
    count = 0
    # Strip newline char
    for line in lines:
        count += 1
        print(line)
        if(line != ''):
            cookie_arg, user_agent = cfscrape.get_cookie_string(line)
            cmd = "curl --cookie {cookie_arg} -A {user_agent} {url}"
            print(subprocess.check_output(cmd.format(cookie_arg=cookie_arg, user_agent=user_agent, url=line), shell=True))

if __name__ == "__main__":
    main()