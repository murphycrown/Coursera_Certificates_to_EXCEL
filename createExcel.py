import pandas as pd
def createExcel():
    with open('certificate_names.txt','r') as namesFile:
        names=namesFile.read().splitlines()
    with open('verification_links.txt','r') as linksFile:
        links=linksFile.read().splitlines()
    data={
      "Certificate Title":names,
      "Verification Link":links

    }
    df=pd.DataFrame(data)
    df.to_excel("output_file.xlsx",index=False)
    print("Excel file created succesfully!!!")
if __name__=="__main__":
    createExcel()