import asyncio, discord, os
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix='!')
member_path = os.path.dirname(os.path.abspath(__file__))+"\member.txt"
m = open(member_path, 'r', encoding="utf-8")
member = m.read().split()

attendance = []

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    for i in range (len(member)):
        attendance.append(False)
    member.sort()

@bot.command()
async def 도움말(ctx):
    await ctx.send('!출석 이름\t-출결 상태를 출석으로 바꿉니다\n!출석확인\t-출석인원 수와 출결현황을 확인합니다\n!출석초기화\t-출결현황을 초기화합니다(회의가 시작하거나 끝났을 때 입력)')

@bot.command()
async def 출석(ctx, arg):
    if arg in member:
        attendance[member.index(arg)] = True
        await ctx.send(f'{arg} 출석')
    else:
        await ctx.send(f'{arg} 님은 출석부에 등록되지 않았습니다')
    
@bot.command()
async def 출석확인(ctx):
    
    for i in range(0, len(member)):
        if attendance[i]:
            await ctx.send(f'{member[i]} : 출석')
        else:
            await ctx.send(f'{member[i]} : 부재')
    await ctx.send(f"출석인원 {attendance.count(True)}명")

@bot.command()
async def 출석초기화(ctx):
    for i in range (len(attendance)):
        attendance[i] = False
    await ctx.send('출석목록 초기화')

@bot.command()
async def 신규등록(ctx, arg):
    if arg in member:
        await ctx.send(f'{arg} 님은 이미 등록되어 있습니다')
    else:
        member.append(arg)
        member.sort()
        newMemberIndex = member.index(arg)
        attendance.insert(newMemberIndex, False)

        await ctx.send(f'{arg} 님이 등록되었습니다')

bot.run(os.environ['token'])