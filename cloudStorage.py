#%%
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
   
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.ArTsCSuHrqAktJZ_KuY5lhq-yFdW-CQ_xBVHK7EJv0LhcqzHvWdjp0nmWuJnjZ03EOoJlBZCKPy49W5w5RvGeIDPeoqP-TKpeyEsOquDldFcHbcoCiGtkAvsRynw6lLQsy64FY8'
    transferData = TransferData(access_token)

    file_from = input("Enter the file Path to transfer")
    file_to = input("Enter the full path to upload to the dropbox")
    # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File has Been Moved")

main()
# %%
