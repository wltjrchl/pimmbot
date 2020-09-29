import asyncio, discord, os
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix='!')
member = []
attendance = []

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def 도움말(ctx):
    await ctx.send('!출석 이름\t-출결 상태를 출석으로 바꿉니다\n!출석확인\t-출석인원 수와 출결현황을 확인합니다\n!출석초기화\t-출결현황을 초기화합니다(회의가 시작하거나 끝났을 때 입력)\n!등록 이름\t-리스트에 회원을 등록합니다\n!제거 이름\t-회원을 리스트에서 제거합니다')

@bot.command()
async def 출석(ctx, arg):
    if arg in member:
        attendance[member.index(arg)] = True
        await ctx.send(f'{arg} 출석')
    else:
        await ctx.send(f'{arg} 님은 출석부에 등록되지 않았습니다')
    
@bot.command()
async def 출석확인(ctx):
    await ctx.send(f"총원 {len(attendance)}명")
    await ctx.send(f"출석인원 {attendance.count(True)}명")
    await ctx.send(f"부재인원 {attendance.count(False)}명")
    for i in range(0, len(member)):
        if attendance[i] == False:
            await ctx.send(f'{member[i]}')

@bot.command()
async def 출석초기화(ctx):
    for i in range (len(attendance)):
        attendance[i] = False
    await ctx.send('출석목록 초기화')

@bot.command()
async def 등록(ctx, arg):
    if arg in member:
        await ctx.send(f'{arg} 님은 이미 등록되어 있습니다')
    else:
        member.append(arg)
        member.sort()
        attendance.insert(member.index(arg), False)
        await ctx.send(f'{arg} 님이 등록되었습니다')


@bot.command()
async def 제거(ctx, arg):
    if arg in member:
        index = member.index(arg)
        del attendance[index]
        del member[index]
        await ctx.send(f'{arg} 님을 제거합니다')
    else:
        await ctx.send(f'{arg} 님은 등록되어 있지 않습니다')
token = os.environ["Bot_Token"]
bot.run(token)