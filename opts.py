import argparse
from numpy import zeros

def init_opts():
    parser = argparse.ArgumentParser(description="Simulation of a marching square with pygames")
    parser.add_argument('--window_height', type=int,
                        help='Change the window height. The default height is set to 500.',
                        default=500)
    parser.add_argument('--window_width', type=int,
                        help='Change the window width. The default height is set to 500.',
                        default=500)
    parser.add_argument('--block_size', type=int,
                        help='Change the size of each block which represents isovalues. The default size is set to 20.',
                        default=20)
    parser.add_argument('--grid_color', metavar=("red_value", "green_value", "blue_value"), nargs=3, type=int,
                        help = 'Change the grid color rgb. The default color is grey with the rgb-values: 200 200 200.', default = [200, 200, 200])

    parser.add_argument('--empty_cell_color', metavar=("red_value", "green_value", "blue_value"), nargs=3, type=int,
                        help = 'Change the empty cell color rgb. The default color is white with the rgb-values: 255 255 255.', default = [255, 255, 255])

    parser.add_argument('--filled_cell_color', metavar=("red_value", "green_value", "blue_value"), nargs=3, type=int,
                        help='Change the filled cell color rgb. The default color is white with the rgb-values: 0 0 0.',
                        default=[0, 0, 0])
    parser.add_argument('--square_color_walk', metavar=("red_value", "green_value", "blue_value"), nargs=3, type=int,
                        help='Change the square color in walk mode. The default color is blue with the rgb-values: 0 0 255.',
                        default=[0, 0, 255])
    parser.add_argument('--square_color_march', metavar=("red_value", "green_value", "blue_value"), nargs=3, type=int,
                        help='Change the square color in walk mode. The default color is red with the rgb-values: 255 0 0.',
                        default=[255, 0, 0])


    args = parser.parse_args()

    if args.window_width % args.block_size != 0 or args.window_height % args.block_size != 0:
        raise ValueError("window_width % block_size and window_height % block_size must be zero")

    Options.args = args

    # init global mutable values
    Options.march_cube_center_pos = [args.block_size, args.block_size]
    Options.square_color = args.square_color_walk
    Options.iso_values = zeros((args.window_height, args.window_width))


class Options:

    @property
    @staticmethod
    def args(self):
        return self.__args

    @args.setter
    @staticmethod
    def args(self, value):
        self.__args = value

    @property
    @staticmethod
    def march_cube_center_pos(self):
        return self.__march_cube_center_pos

    @march_cube_center_pos.setter
    @staticmethod
    def march_cube_center_pos(self, value):
        self.__march_cube_center_pos = value

    @property
    @staticmethod
    def square_color(self):
        return self.__square_color

    @square_color.setter
    @staticmethod
    def square_color(self, value):
        self.__square_color = value

    @property
    @staticmethod
    def iso_values(self):
        return self.__iso_values

    @iso_values.setter
    @staticmethod
    def iso_values(self, value):
        self.__iso_values = value

