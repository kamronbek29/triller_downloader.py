import requests


def get_download_url(link):
    get_request = requests.get(link)
    get_request_content = get_request.content
    get_request_content_str = str(get_request_content, 'utf-8')
    no_script = get_request_content_str.split('<noscript>')[1].split('</noscript>')[0]
    download_url = no_script.split('src="')[1].split('"')[0]

    return download_url


def download_video(download_url):
    get_request = requests.get(download_url)
    video_content = get_request.content

    with open('video.mp4', "wb") as file_to_save:
        file_to_save.write(video_content)


def main():
    input_url = input('Paste triller video url here: ')
    download_url = get_download_url(input_url.replace(' ', ''))
    print('Video downloading...')
    download_video(download_url)
    print('Video downloaded!')


if __name__ == '__main__':
    main()
