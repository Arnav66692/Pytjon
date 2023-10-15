import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        
        f = open(file_from,'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.Bng88ioZXGzgvCPEvwklHBLipc8UpodRCTCel7AMeK7Sqg9N43AK8DSM4GMGb0tFrR_lf0zjmHChUaRuVxzTV4Mf-9KUYVfwuJFnuWsoXgm8FUvjZPAWfxAwA7apwO5ZgCSyziebqYJu'
    transferData = TransferData(access_token)

    file_from = input('enter the file path to transfer: ')
    file_to = input('enter the full path to upload to DropBox: ')


    transferData.upload_file(file_from, file_to)
    print('file has been moved')

main()    


