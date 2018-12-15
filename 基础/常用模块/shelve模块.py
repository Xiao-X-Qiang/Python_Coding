import shelve

f=shelve.open('hello')

names=['alex','rain','test']
info={'name':'alex','age':'22'}

f['nam']=names
f['info_dict']=info

f.close()

