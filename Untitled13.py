#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.display import display, HTML

display(HTML('''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Catch the Falling Objects</title>
<style>
    body {
        margin: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #000;
    }
    canvas {
        border: 1px solid #fff;
        background-color: #000;
    }
    .scoreboard {
        position: absolute;
        top: 10px;
        left: 50%;
        transform: translateX(-50%);
        color: #fff;
        font-size: 24px;
    }
</style>
</head>
<body>
<div class="scoreboard" id="scoreboard">Score: 0</div>
<canvas id="gameCanvas" width="600" height="400"></canvas>
<script>
    const canvas = document.getElementById('gameCanvas');
    const context = canvas.getContext('2d');
    const scoreboard = document.getElementById('scoreboard');

    const basketWidth = 100;
    const basketHeight = 20;
    const objectSize = 20;
    const objectSpeed = 2;
    let basketX = (canvas.width - basketWidth) / 2;
    let score = 0;

    let fallingObjects = [];

    function drawBasket(x) {
        context.fillStyle = '#fff';
        context.fillRect(x, canvas.height - basketHeight, basketWidth, basketHeight);
    }

    function drawObject(x, y) {
        context.fillStyle = '#fff';
        context.fillRect(x, y, objectSize, objectSize);
    }

    function moveObjects() {
        for (let i = 0; i < fallingObjects.length; i++) {
            fallingObjects[i].y += objectSpeed;
            if (fallingObjects[i].y + objectSize > canvas.height) {
                fallingObjects.splice(i, 1);
                i--;
            }
        }
    }

    function checkCollision() {
        for (let i = 0; i < fallingObjects.length; i++) {
            if (
                fallingObjects[i].y + objectSize >= canvas.height - basketHeight &&
                fallingObjects[i].x + objectSize > basketX &&
                fallingObjects[i].x < basketX + basketWidth
            ) {
                fallingObjects.splice(i, 1);
                score++;
                updateScoreboard();
                i--;
            }
        }
    }

    function updateScoreboard() {
        scoreboard.textContent = `Score: ${score}`;
    }

    function draw() {
        context.clearRect(0, 0, canvas.width, canvas.height);
        drawBasket(basketX);
        for (let object of fallingObjects) {
            drawObject(object.x, object.y);
        }
        moveObjects();
        checkCollision();

        requestAnimationFrame(draw);
    }

    function spawnObject() {
        const x = Math.random() * (canvas.width - objectSize);
        fallingObjects.push({ x: x, y: 0 });
    }

    canvas.addEventListener('mousemove', function(event) {
        const canvasPosition = canvas.getBoundingClientRect();
        basketX = event.clientX - canvasPosition.left - basketWidth / 2;
        if (basketX < 0) basketX = 0;
        if (basketX > canvas.width - basketWidth) basketX = canvas.width - basketWidth;
    });

    setInterval(spawnObject, 1000);
    draw();
</script>
</body>
</html>
'''))

