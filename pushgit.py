from os import system as st
from time import sleep

def tambah(link,main):
    st('git config --global user.email "aldyansyahcp@gmail.com"')
    st('git config --global user.name "aldyansyahcp"')
    st("git init")
    sleep(2)
    st("git add *")
    st("git commit -m 'push termuk'")
    sleep(2)
    st(f"git branch -M {main}")
    st(f"git remote add origin {link}")
    sleep(2)
    st(f"git push origin {main}")
    print("berhasil push")

if __name__ == "__main__":
    lin = input('masukan link gitnya: ')
    br = input("pilih branch main/master: ")
    tambah(lin,br)
