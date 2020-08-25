from mcstatus import MinecraftServer
from PIL import Image, ImageDraw, ImageFont
import os,sys,base64,io

class Server_Stats:
    def __image_creator(self,title,descr,ip_port,num,ms):
        self.path = os.path.split(os.path.realpath(__file__))[0]

        self.bgpath = os.path.join(self.path,"background.png")
        self.fontpath = os.path.join(self.path,"SourceHanSansCN-Medium.otf")

        self.font = ImageFont.truetype(self.fontpath, 15)
        self.bg = Image.open(self.bgpath).convert('RGBA')
        self.text_overlay = Image.new('RGBA', self.bg.size, (255, 255, 255, 0))
        self.image_draw = ImageDraw.Draw(self.text_overlay)
        self.image_draw.text((8, 8), title, font=self.font, fill=(154, 205, 196, 255))#标题
        self.image_draw.text((8,30), descr, font=self.font, fill=(255, 255, 255, 255))#描述
        self.image_draw.text((403,30),num, font=self.font, fill=(255, 255, 255, 255))#人数
        self.image_draw.text((8,50), ip_port, font=self.font, fill=(128, 128, 128, 255))#ip_端口
        self.image_draw.text((395,8),ms, font=self.font, fill=(50, 205, 50, 255))#延迟
        self.image_with_text = Image.alpha_composite(self.bg, self.text_overlay)
        return self.image_with_text 

    def status_get(self,ip_port,title,motd):
        self.server = MinecraftServer.lookup(ip_port)
        self.status = self.server.status()
        self.latency = self.server.ping()
        #query = server.query()
        self.player_p = str(self.status.players.online)+"/"+str(self.status.players.max)
        self.image = self.__image_creator(title,motd,"地址:"+ip_port,self.player_p,str(int(self.latency))+"ms")
        self.img_buffer = io.BytesIO()
        self.image.save(self.img_buffer, format='PNG')
        self.byte_data = self.img_buffer.getvalue()
        #base64_str = base64.b64encode(byte_data)
        return self.byte_data
        #return image
        
if __name__ == "__main__":
    server_1  = Server_Stats()
    img = server_1.status_get("mcyyy.co","title","motd")
    with open("C:\\Users\\Max\\Desktop\lena.jpg","wb") as f:
        f.write(img)