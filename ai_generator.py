from PIL import Image


def analyze_image(image_path):

    image = Image.open(image_path)

    width = image.width
    height = image.height

    return {
        "width": width,
        "height": height
    }


def generate_website(image_path):

    info = analyze_image(
        image_path
    )


    html = """
<!DOCTYPE html>

<html>

<head>

<title>Generated Website</title>

</head>

<body>

<header class="navbar">

<h2>My Website</h2>

<nav>

<a href="#">Home</a>

<a href="#">About</a>

<a href="#">Services</a>

<a href="#">Contact</a>

</nav>

</header>


<section class="hero">

<h1>Welcome to My Website</h1>

<p>
This website was generated from a screenshot.
</p>

<button>Get Started</button>

</section>


<section class="cards">

<div class="card">

<h2>Feature 1</h2>

<p>
Easy website generation.
</p>

</div>


<div class="card">

<h2>Feature 2</h2>

<p>
Responsive design.
</p>

</div>


<div class="card">

<h2>Feature 3</h2>

<p>
Automatic code generation.
</p>

</div>

</section>

</body>

</html>
"""


    css = """

body {

margin: 0;

font-family: Arial;

background: #f4f4f4;

}


.navbar {

display: flex;

justify-content: space-between;

padding: 20px;

background: #35207a;

color: white;

}


.navbar a {

color: white;

margin: 10px;

text-decoration: none;

}


.hero {

text-align: center;

padding: 80px;

background: #7652d4;

color: white;

}


.hero button {

padding: 12px 25px;

border: none;

border-radius: 8px;

}


.cards {

display: flex;

gap: 20px;

padding: 40px;

}


.card {

flex: 1;

background: white;

padding: 25px;

border-radius: 10px;

box-shadow:
0 5px 15px rgba(0,0,0,0.1);

}

"""


    return {

        "html": html,

        "css": css,

        "width": info["width"],

        "height": info["height"]

    }