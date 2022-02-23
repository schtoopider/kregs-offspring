

import interactions
from key import TOKEN

bot = interactions.Client(token= TOKEN)
scope = 774868449993949195

@bot.command(
    name= 'heheheha', 
    description= "我操你妈，呵呵呵哈",
    scope= scope
)
async def heheheha(ctx):
    await ctx.send("雪花飘飘，北风萧萧")

bot.start()
