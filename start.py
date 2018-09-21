
import Config
from colorama import init
init(autoreset=True)
class test(Config.Config,Config.Colored):

    def run(self):
        s = Config.Config.PASSWORD_DIC_DIR
        print(s)
        print(Config.Colored.red(s=s))
        print(Config.Colored.black(s))
        print(Config.Colored.blue(s))
        print(Config.Colored.cyan(s))
        print(Config.Colored.magenta(s))
        print(Config.Colored.white(s))
        print(Config.Colored.yellow(s))
        print(Config.Colored.white_green(s))
        #print(Config.c.PASSWORD_DIC_DIR)

if __name__ == '__main__':
    a = test()
    a.run()
