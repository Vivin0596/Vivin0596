import speedtest
speed_test = speedtest.Speedtest()
while True:
    print('uploading...')
    upload_speed = speed_test.upload()
    print('downloading...')
    download_speed = speed_test.download()
