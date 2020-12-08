import asyncio
from aiohttp import ClientSession


async def get_download_url(link):
    async with ClientSession() as session:
        async with session.get(link) as get_request:
            get_request_content = await get_request.content.read()
            get_request_content_str = str(get_request_content, 'utf-8')
            no_script = get_request_content_str.split('<noscript>')[1].split('</noscript>')[0]
            download_url = no_script.split('src="')[1].split('"')[0]

            return download_url


async def download_video(video_url):
    async with ClientSession() as session:
        async with session.get(video_url) as get_video:
            with open('video.mp4', "wb") as file_to_save:
                file_content = await get_video.content.read()
                file_to_save.write(file_content)


async def main():
    input_url = input('Paste triller video url here: ')
    download_url = await get_download_url(input_url.replace(' ', ''))
    print('Video downloading...')
    await download_video(download_url)
    print('Video downloaded!')


if __name__ == '__main__':
    asyncio.run(main())
