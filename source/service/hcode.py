from AESman import decode

#----------------------------------------------------------------
wwpd = [
['hr47SBcWbN4qOCHvcPwTR97NyXB8ZI21sVXznQxYjRI=',""],
['Dy2kbXRyVmUupwIbF4k2I97NyXB8ZI21sVXznQxYjRI=',""],
['xWsuDslAr4kTl1lcUJbt6YUuuyYhOutoYVSYZ0K/NOAcOEq2h1Wi/oa0eRLgoMWhs8dMWaFM+VjBCuK+eIMz197NyXB8ZI21sVXznQxYjRLezclwfGSNtbFV850MWI0S',""],
['HkaeOVy5TmtJU7m7fWtJc/OCFDFdCQUcKlUXd6/eWAjezclwfGSNtbFV850MWI0S3s3JcHxkjbWxVfOdDFiNEg==',""],
['PcLlvYfm9WK3rtWvVYQ9Rd7NyXB8ZI21sVXznQxYjRI=',""],
["mi7+veq5R1Pwz1s6BkMtu97NyXB8ZI21sVXznQxYjRI=",""],
['JAUiiPgZLSoyq/afYHgItt7NyXB8ZI21sVXznQxYjRI=',""],
['HolOFzW/yuTxPLuYBhSgmd7NyXB8ZI21sVXznQxYjRI=',""],
["q46Xw6BnUuepqJi3DajWK97NyXB8ZI21sVXznQxYjRI=",""],
['LNt9XC6fLBw4fi2rIMoAmd7NyXB8ZI21sVXznQxYjRI=',""],
['hTxyBesoKxZF3t+R9Ek8wN7NyXB8ZI21sVXznQxYjRI=',""],
["4zPAM6ZkGBTJLKt5/ShTv97NyXB8ZI21sVXznQxYjRI=",""],
["1/QCEzZT7oKJ/XiuyyP1M97NyXB8ZI21sVXznQxYjRI=",""],
['xwFfAaGki7XFepxIwE/YCt7NyXB8ZI21sVXznQxYjRI=',""],
["26tOwzvftcMKG7nEBh1Rct7NyXB8ZI21sVXznQxYjRI=",""],
["0fKxYMfAmzI0DtpSwDH7pt7NyXB8ZI21sVXznQxYjRI=",""],
["P79LERl4IJSxy+Dd+2riCd7NyXB8ZI21sVXznQxYjRI=",""],
["pMF0SaL8uQ27sW9/Ca2Xgt7NyXB8ZI21sVXznQxYjRI=",""],
["s6HCIWG1w8FuHlXZ2uPSsN7NyXB8ZI21sVXznQxYjRI=",""],
["QLimc0q/rpjQ8/UHz026RN7NyXB8ZI21sVXznQxYjRI=",""],
["i2yL2S+7BNqYa6SM+jamv97NyXB8ZI21sVXznQxYjRI=",""],
["IWmNyGy6UGyO9tx7AIQcSt7NyXB8ZI21sVXznQxYjRI=",""],
["xnTvB15I5YX8lz4zV0YaZ97NyXB8ZI21sVXznQxYjRI=",""],
["fd9I3lEIPzo0xde10fMydAUI55BCKkb9b+gkORRs4nTezclwfGSNtbFV850MWI0S3s3JcHxkjbWxVfOdDFiNEg==",""],
["HM2iMu51d3IuZA+HA21QmN7NyXB8ZI21sVXznQxYjRI=",""],
["7cFnMS3UYul8ZZM8k61J3t7NyXB8ZI21sVXznQxYjRI=",""],
["jreW6yDqml/p5/IYEsCWBd7NyXB8ZI21sVXznQxYjRI=",""],
["Shy3Ur+nC6WJjNXvJ1dgUd7NyXB8ZI21sVXznQxYjRI=",""],
["mFdbabd8SP0qwjp85WfYgt7NyXB8ZI21sVXznQxYjRI=",""],
["1u3BVnSMdHXiOYiYASCvM97NyXB8ZI21sVXznQxYjRI=",""]]

def reconstitute(key, badness):
    for i in range(len(badness)):
        badness[i][1] = decode(key, badness[i][0])

