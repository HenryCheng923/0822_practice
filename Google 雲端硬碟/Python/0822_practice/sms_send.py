from twilio.rest import Client

account_sid = 'ACfcdf725891e157ec05652de328fcc233'

auth_token = '21522d3e62d7097595b2a5e9a68b12f5'

client = Client(account_sid, auth_token)

message = client.messages.create(
	to = "+886987048924",
	from_ = "+12563673645",
	body = "成功寄給自己簡訊拉")
