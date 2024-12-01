from utils import get_input
import part1
import part2

def run(input_file='input.txt'):
    get_input(input_file)

    part1.run('floop', g='poop')

    part2.run()

if __name__ == '__main__':
    run('test.txt')