username1 = 'farukces25'
password1 = '29ko1k9o'

username = input('Username = ').lower().strip()
password = input('Password = ').lower().strip()

if username == username1:
    if password == password1:
     print('Giriş Başarılı')
    else:
     print('Parola Yanlış!')
else:
    print('Kullanıcı Adı Yanlış!')



