from mcstatus import MinecraftServer
from PIL import Image, ImageDraw, ImageFont
import os,sys,base64,io


def image_creator(title,descr,ip_port,num,ms):
    path = os.path.split(os.path.realpath(__file__))[0]

    bgpath = os.path.join(path,"background.png")
    fontpath = os.path.join(path,"SourceHanSansCN-Medium.otf")

    font = ImageFont.truetype(fontpath, 15)
    bg = Image.open(bgpath).convert('RGBA')
    text_overlay = Image.new('RGBA', bg.size, (255, 255, 255, 0))
    image_draw = ImageDraw.Draw(text_overlay)
    image_draw.text((8, 8), title, font=font, fill=(154, 205, 196, 255))#标题
    image_draw.text((8,30), descr, font=font, fill=(255, 255, 255, 255))#描述
    image_draw.text((403,30),num, font=font, fill=(255, 255, 255, 255))#人数
    image_draw.text((8,50), ip_port, font=font, fill=(128, 128, 128, 255))#ip_端口
    image_draw.text((395,8),ms, font=font, fill=(50, 205, 50, 255))#延迟
    image_with_text = Image.alpha_composite(bg, text_overlay)
    return image_with_text 

def status_get(ip_port,title,motd):
    server = MinecraftServer.lookup(ip_port)
    status = server.status()
    latency = server.ping()
    query = server.query()
    player_p = str(status.players.online)+"/"+str(status.players.max)
    image = image_creator(title,motd,"地址:"+ip_port,player_p,str(int(latency))+"ms")
    img_buffer = io.BytesIO()
    image.save(img_buffer, format='PNG')
    byte_data = img_buffer.getvalue()
    #base64_str = base64.b64encode(byte_data)
    return byte_data
    #return image
    
if __name__ == "__main__":
    pass