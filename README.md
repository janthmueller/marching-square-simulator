<div id="top"></div>

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![Xing][xing-shield]][xing-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">marching-square-simulator</h3>

  <p align="center">
    A simple interactive marching square simulator with pygame.
    <br />
    <a href="https://github.com/janthmueller/marching-square-simulator"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/janthmueller/marching-square-simulator">View Demo</a>
    ·
    <a href="https://github.com/janthmueller/marching-square-simulator/issues">Report Bug</a>
    ·
    <a href="https://github.com/janthmueller/marching-square-simulator/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

A simple interactive simulation of a marching square on binary iso-values.
You can draw black and white cells, move the marching square manually around and move it according to the iso-values (set by colors).

![Product Name Screen Shot][product-screenshot]






### Built With

Major frameworks/libraries used to bootstrap the project. 

* [pygame](https://www.pygame.org/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
### Prerequisites
### Installation

<!-- USAGE EXAMPLES -->
## Usage
###Start Simulation/Game

```sh
python marching_square.py
```

Optional Arguments:
```sh
  -h, --help            show this help message and exit
  --window_height WINDOW_HEIGHT
                        Change the window height. The default height is set to 500.
  --window_width WINDOW_WIDTH
                        Change the window width. The default height is set to 500.
  --block_size BLOCK_SIZE
                        Change the size of each block which represents isovalues. The default size is set to 20.
  --grid_color red_value green_value blue_value
                        Change the grid color rgb. The default color is grey with the rgb-values: 200 200 200.
  --empty_cell_color red_value green_value blue_value
                        Change the empty cell color rgb. The default color is white with the rgb-values: 255 255 255.
  --filled_cell_color red_value green_value blue_value
                        Change the filled cell color rgb. The default color is white with the rgb-values: 0 0 0.
  --square_color_walk red_value green_value blue_value
                        Change the square color in walk mode. The default color is blue with the rgb-values: 0 0 255.
  --square_color_march red_value green_value blue_value
                        Change the square color in walk mode. The default color is red with the rgb-values: 255 0 0.

```
### Control

WASD - move marching square freely
SPACE - move marching square by iso-values 
MOUSECLICK on cell - change cell color (white <-> black) / iso-value (0 <-> 1)

<!-- ROADMAP -->
## Roadmap

- [ ] Add Changelog


See the [open issues](https://github.com/janthmueller/marching-square-simulator/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Jan Müller

Project Link: [https://github.com/janthmueller/marching-square-simulator](https://github.com/janthmueller/marching-square-simulator)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments


* [Best README Template](https://github.com/othneildrew/Best-README-Template)
* 


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/janthmueller/marching-square-simulator.svg?style=for-the-badge
[contributors-url]: https://github.com/janthmueller/marching-square-simulator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/janthmueller/marching-square-simulator.svg?style=for-the-badge
[forks-url]: https://github.com/janthmueller/marching-square-simulator/network/members
[stars-shield]: https://img.shields.io/github/stars/janthmueller/marching-square-simulator.svg?style=for-the-badge
[stars-url]: https://github.com/janthmueller/marching-square-simulator/stargazers
[issues-shield]: https://img.shields.io/github/issues/janthmueller/marching-square-simulator.svg?style=for-the-badge
[issues-url]: https://github.com/janthmueller/marching-square-simulator/issues
[license-shield]: https://img.shields.io/github/license/janthmueller/marching-square-simulator.svg?style=for-the-badge
[license-url]: https://github.com/janthmueller/marching-square-simulator/blob/master/LICENSE.txt
[xing-shield]: https://img.shields.io/static/v1?style=for-the-badge&message=Xing&color=006567&logo=Xing&logoColor=FFFFFF&label=
[xing-url]: https://www.xing.com/profile/Jan_Mueller1015
[product-screenshot]: images/screenshot.png 
