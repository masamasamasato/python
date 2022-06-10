#オブジェクト指向言語   クラス(設計図)をもとにオブジェクト（インスタンス）を作っていく方法
#継承   クラスの機能を受け継いで新しいクラスを作る操作のこと　車クラスからトラッククラス、

class Car(object):  #親クラス　全ての車オブジェクトに共通するものをここでかく　
    def run(self):
        print('run')

class ToyotaCar(Car):
    pass

class TeslaCar(Car):    #車の中でもテスラにはこの機能、トヨタにはこの機能という具合に機能を付け加えたいときに継承を用いる
    def auto_run(self):
        print('auto run')

car = Car()
car.run

print("#################")

toyota_car = ToyotaCar()
toyota_car.run()

print("#################")

tesla_car = TeslaCar()
tesla_car.auto_run()