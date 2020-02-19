while True:
	pwd = input('請輸入密碼：')
	if pwd == 'a123456':
		print('登入成功')
		break
	elif pwd != 'a123456':
		print('密碼錯誤', '你還有', C, '次機會')
		while pwd >=3:
	
