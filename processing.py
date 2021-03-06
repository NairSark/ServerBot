from discord import Embed
import random

def doge(message):
    """
    Доге
    """
    permits=["374914059679694848", "421637061787779072", "431897105163091979"]
    if message.channel.id not in permits: return;

    embed = Embed(color = 0x00ff00)
    embed.set_author(name = str(message.author.name), icon_url = str(message.author.avatar_url))
    lines = [line.rstrip('\n') for line in open('data_lists/dogelist')]
    for i in range(10): random.shuffle(lines);
    embed.set_image(url = lines[random.randint(0, len(lines)-1)])

    return ["embed", embed]

def help(author, prefix):
    """
    Справка по командам
    """
    embed = Embed(color = 0x00ff00)
    embed.set_author(name = str(author.name), icon_url = str(author.avatar_url))
    embed.set_thumbnail(url = "https://happycoin.club/wp-content/uploads/2017/05/dogecoin_2.png")

    embed.add_field(name = "Забавы",
    value = ("`{0}doge`- получить порцию доге\n"
            "`{0}points` - посчитать догекоины в кошельке"
            ).format(prefix), inline = False)
    return ["embed", embed]

def points(author, points):
    """
    Посчитать поинты пользователя.
    """

    embed = Embed(color = 0x00ff00)
    embed.set_author(name = str(author.name), icon_url = str(author.avatar_url))
    embed.add_field(name = "Догекоины", value = str(points), inline = True)
    return ["embed", embed]

def get_top_list(author, users):
    """
    Получить топ пользователей
    """

    embed = Embed(color=0x00ff00)
    embed.set_author(name=str(author.name), icon_url=str(author.avatar_url))
    embed.set_thumbnail(url="https://happycoin.club/wp-content/uploads/2017/05/dogecoin_2.png")
    count=1
    for user in users:
        embed.add_field(name="{}. {}".format(count, user[0]), value="%s догекойнов"%(str(user[1])),inline=True)
        count+=1
    return ["embed", embed]
