Usage:
$ git clone https://github.com/lhorgan/WHERE.IS.MY.CHARGER.git
$ cd WHERE.IS.MY.CHARGER/
$ python3
>> import prob as p
>> p.go(4, 0.8, 100)
[100, 38, 18, 0.47368421052631576, 0.5]
>> p.go(70, 0.99, 100000)
[100000, 2449, 1423, 0.5810534912209064, 0.5857988165680471]
>> p.go(4, 1, 100)
[1000, 242, 242, 1.0, 1.0]