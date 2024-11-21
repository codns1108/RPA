import qrcode

name = (input("이름을 입력하세요"))
scode = int(input("학번을 입력하세요"))
major = (input("의료정보과"))

qr_data = f"{name} {scode} {major}"
qr_img = qrcode.make(qr_data)

save_path = 'my_info_data.png'
qr_img.save(save_path)


