# auto monitor the wordpress container of im whether have a weird file in /var/www/html
import datetime, requests
from subprocess import call, PIPE, run

# bot info
bot_token = ""
chat_id = ""

def main() :
    content = filterWhiteList(lsContainerContent())
    if not content == "good" :
        send_msg_url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={content}"
        res = requests.get(send_msg_url) # this sends the message
        print(res)

def lsContainerContent() :
    container_name = "wordpress_xxx"
    file_path = "/var/www/html"
    result = run(["docker", "exec", container_name, "ls", file_path], stdout=PIPE, stderr=PIPE, universal_newlines=True)
    return result.stdout

def filterWhiteList(result) :
    result = result.split("\n")
    # white list of file in file_path
    white_list = ['index.php', 'license.txt', 'readme.html', 'test', 'wp-activate.php', 'wp-admin', 'wp-blog-header.php', 'wp-comments-post.php', 'wp-config-docker.php', 'wp-config-sample.php', 'wp-config.php', 'wp-content', 'wp-cron.php', 'wp-includes', 'wp-links-opml.php', 'wp-load.php', 'wp-login.php', 'wp-mail.php', 'wp-settings.php', 'wp-signup.php', 'wp-trackback.php', 'xmlrpc.php', 'wordfence-waf.php']
    # whether have the suspecious file
    file_not_in_white_list = False
    suspecious_file_name = ""
    # check
    for each_file in result :
        # not the empty file and not in the white list is suspecious
        if each_file and each_file not in white_list :
            file_not_in_white_list = True
            suspecious_file_name += each_file + "\n"
    # return the result
    if file_not_in_white_list :
        return "Have Suspecious File !\n" + suspecious_file_name
    else :
        return "good"

main()

