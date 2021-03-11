import config


class Seating:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def seats(self):
        config.val = ['S']*self.row
        for i in range(self.row):
            config.val[i] = ['S'] * self.column
        print('\n'.join([''.join(['{:3}'.format(item) for item in row])
                         for row in config.val]))
        '''for i in range(self.row):
            for j in range(self.column):
                print(config.val[i][j], end=" ")
            print('\n')'''
        return

    def ret(self):
        print('\n'.join([''.join(['{:3}'.format(item) for item in row])
                         for row in config.val]))
