import random,string,json
a = {
    "riderId": None,
    "riderName": None,
    "riderCardno": None,
    "riderMobile": None,
    "insureDate": None,
    "orgId": None,
    "stationId": None,
    "workingHours": None,
    "offWorkingHours": None,
    "bizSourceType": None,
    "bizCreatetime": None,
}

seed1 = "1234567890"

seed2 = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

if __name__=="__main__":
    for aa in a:
        if aa in ["riderId","riderCardno","riderMobile","orgId","stationId","bizSourceType"]:
            a[aa]=''.join(random.sample(seed1, 8))
        elif aa in ["bizCreatetime","insureDate"]:
            a[aa]="2019-01-01 01:01:01"
        else:
            a[aa] = ''.join(random.sample(seed2, 8))


    print(json.dumps(a,indent=4))