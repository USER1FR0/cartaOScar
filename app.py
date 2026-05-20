from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Galaxia</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Segoe UI',sans-serif;
}

body{
    overflow:hidden;
    height:100vh;
    background:black;
    color:white;
}

/* ESPACIO */

.space{
    position:fixed;
    width:100%;
    height:100%;
    background:
    radial-gradient(circle at center,
    rgba(20,40,90,0.4) 0%,
    rgba(0,0,0,1) 70%);
    animation:zoomSpace 25s ease-in-out infinite alternate;
}

@keyframes zoomSpace{
    from{
        transform:scale(1);
    }

    to{
        transform:scale(1.08);
    }
}

/* ESTRELLAS */

.stars{
    position:absolute;
    width:100%;
    height:100%;
}

.star{
    position:absolute;
    background:white;
    border-radius:50%;
    animation:twinkle infinite alternate;
}

@keyframes twinkle{

    from{
        opacity:0.2;
        transform:scale(0.6);
    }

    to{
        opacity:1;
        transform:scale(1.3);
    }
}

/* NEBULOSA */

.nebula{
    position:absolute;
    width:1200px;
    height:1200px;

    background:
    radial-gradient(circle,
    rgba(100,0,255,0.25),
    rgba(0,150,255,0.12),
    transparent 70%);

    border-radius:50%;

    filter:blur(80px);

    top:-400px;
    left:-300px;

    animation:rotateNebula 100s linear infinite;
}

@keyframes rotateNebula{

    from{
        transform:rotate(0deg);
    }

    to{
        transform:rotate(360deg);
    }
}

/* PLANETAS */

.planet{
    position:absolute;
    border-radius:50%;
    background-size:cover;
    background-position:center;
    box-shadow:
    inset -40px -20px 80px rgba(0,0,0,0.8),
    0 0 50px rgba(255,255,255,0.2);
}

/* TIERRA */

.earth{
    width:420px;
    height:420px;

    left:-100px;
    bottom:-100px;

    background-image:
    url('https://upload.wikimedia.org/wikipedia/commons/9/97/The_Earth_seen_from_Apollo_17.jpg');

    animation:
    earthFloat 20s ease-in-out infinite alternate,
    rotatePlanet 100s linear infinite;
}

.earth::after{
    content:"";

    position:absolute;
    inset:-20px;

    border-radius:50%;

    background:
    radial-gradient(circle,
    rgba(0,150,255,0.45),
    transparent 70%);

    filter:blur(30px);

    z-index:-1;
}

/* SATURNO */

.saturn{
    width:260px;
    height:260px;

    right:-80px;
    top:70px;

    background-image:
    url('https://upload.wikimedia.org/wikipedia/commons/c/c7/Saturn_during_Equinox.jpg');

    animation:
    saturnFloat 25s ease-in-out infinite alternate,
    rotatePlanet 120s linear infinite;
}

.ring{
    position:absolute;

    width:350px;
    height:120px;

    border:8px solid rgba(255,255,255,0.25);

    border-radius:50%;

    right:-120px;
    top:140px;

    transform:rotate(-20deg);

    filter:blur(0.5px);

    animation:saturnFloat 25s ease-in-out infinite alternate;
}

/* MARTE */

.mars{
    width:150px;
    height:150px;

    left:-100px;
    top:60%;

    background-image:
    url('https://upload.wikimedia.org/wikipedia/commons/0/02/OSIRIS_Mars_true_color.jpg');

    animation:
    marsMove 40s linear infinite,
    rotatePlanet 80s linear infinite;
}

/* MOVIMIENTOS */

@keyframes earthFloat{
    from{
        transform:translateY(0px);
    }

    to{
        transform:translateY(-30px);
    }
}

@keyframes saturnFloat{
    from{
        transform:translateY(0px);
    }

    to{
        transform:translateY(25px);
    }
}

@keyframes marsMove{

    from{
        transform:translateX(0px);
    }

    to{
        transform:translateX(1800px);
    }
}

@keyframes rotatePlanet{

    from{
        background-position:0px 0px;
    }

    to{
        background-position:1200px 0px;
    }
}

/* COMETAS */

.comet{
    position:absolute;

    width:5px;
    height:220px;

    background:
    linear-gradient(
    to bottom,
    rgba(255,255,255,1),
    rgba(120,200,255,0.7),
    transparent);

    border-radius:50%;

    transform:rotate(45deg);

    filter:blur(1px);

    animation:cometMove linear forwards;
}

@keyframes cometMove{

    from{
        transform:
        translate(0px,0px)
        rotate(45deg);

        opacity:1;
    }

    to{
        transform:
        translate(1700px,1700px)
        rotate(45deg);

        opacity:0;
    }
}

/* ASTEROIDES */

.asteroid{
    position:absolute;

    background:#777;
    border-radius:50%;

    opacity:0.7;

    animation:asteroidMove linear infinite;
}

@keyframes asteroidMove{

    from{
        transform:translateX(0px);
    }

    to{
        transform:translateX(-2000px);
    }
}

/* TEXTO SIN FONDO */

.message{
    position:absolute;

    top:50%;
    left:50%;

    transform:translate(-50%,-50%);

    width:90%;
    max-width:900px;

    text-align:center;

    z-index:10;

    animation:floatText 6s ease-in-out infinite alternate;
}

@keyframes floatText{

    from{
        transform:
        translate(-50%,-50%)
        translateY(0px);
    }

    to{
        transform:
        translate(-50%,-50%)
        translateY(-12px);
    }
}

.title{

    font-size:4rem;

    margin-bottom:30px;

    color:white;

    text-shadow:
    0 0 20px #60a5fa,
    0 0 40px #3b82f6;
}

.text{

    font-size:1.6rem;

    line-height:2.8rem;

    color:white;

    text-shadow:
    0 0 10px rgba(0,0,0,0.9),
    0 0 20px rgba(0,0,0,0.8);
}

.highlight{

    color:#7dd3fc;

    font-size:2rem;

    font-weight:bold;

    text-shadow:
    0 0 20px #38bdf8,
    0 0 40px #0ea5e9;
}

</style>
</head>

<body>

<div class="space"></div>

<div class="nebula"></div>

<div class="stars" id="stars"></div>

<div class="planet earth"></div>

<div class="planet saturn"></div>

<div class="ring"></div>

<div class="planet mars"></div>

<div class="message">

    <div class="title">
        🌌 Para Ti 🌌
    </div>

    <div class="text">

        A veces la distancia se siente enorme,
        como si hubiera galaxias completas entre nosotros.

        <br><br>

        Pero incluso así,
        sigues apareciendo en mis pensamientos
        en los momentos más simples del día.

        <br><br>

        Extraño hablar contigo,
        reír contigo
        y sentir que todo es más tranquilo cuando estás aquí.

        <br><br>

        Tal vez ahora solo podamos ver el mismo cielo desde lugares distintos,
        pero aún así siento que seguimos conectados ✨

        <br><br>

        <span class="highlight">
            Te extraño mucho, tilino ❤️
        </span>

    </div>

</div>

<script>

/* ESTRELLAS */

const stars = document.getElementById("stars");

for(let i=0;i<700;i++){

    const star = document.createElement("div");

    star.classList.add("star");

    let size = Math.random()*3;

    star.style.width = size + "px";
    star.style.height = size + "px";

    star.style.left = Math.random()*100 + "%";
    star.style.top = Math.random()*100 + "%";

    star.style.animationDuration =
    (Math.random()*4+2)+"s";

    stars.appendChild(star);
}

/* COMETAS */

function createComet(){

    const comet = document.createElement("div");

    comet.classList.add("comet");

    comet.style.top =
    Math.random()*40 + "%";

    comet.style.left =
    Math.random()*20 + "%";

    comet.style.animationDuration =
    (Math.random()*2+2)+"s";

    document.body.appendChild(comet);

    setTimeout(()=>{
        comet.remove();
    },4000);
}

setInterval(createComet,1200);

/* ASTEROIDES */

function createAsteroid(){

    const asteroid = document.createElement("div");

    asteroid.classList.add("asteroid");

    asteroid.style.width =
    (Math.random()*8+3)+"px";

    asteroid.style.height =
    asteroid.style.width;

    asteroid.style.top =
    Math.random()*100 + "%";

    asteroid.style.left =
    Math.random()*100 + "%";

    asteroid.style.animationDuration =
    (Math.random()*20+10)+"s";

    document.body.appendChild(asteroid);

    setTimeout(()=>{
        asteroid.remove();
    },30000);
}

setInterval(createAsteroid,400);

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)