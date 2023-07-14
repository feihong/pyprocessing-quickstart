def setup():
    size(400, 400)
    background(200)

def draw():
    textSize(60)
    textAlign(CENTER)
    text('Hello World!', width/2, height/2)
    
    # This just produces gibberish, unicode isn't supported
    # text('你好世界！', width/2, 50)
