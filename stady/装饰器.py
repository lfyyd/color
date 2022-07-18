def func(tst):
    def aa():
        print('----a----')
        tst()
        print('----b---')

    return aa


@func
def tst():
    print('--------tst-----')


a = tst
a()

