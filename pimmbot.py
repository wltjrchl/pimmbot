import asyncio, discord, os, unicodedata
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix='!')
member = ['최지석',
        '김제민',
        '마혜진',
        '임원빈',
        '김태준',
        '이정석',
        '김민기',
        '이시은',
        '김상엽',
        '이동준',
        '김수은',
        '박진화',
        '진성호',
        '이종하',
        '오승재',
        '조진성',
        '나병찬',
        '김경재',
        '김정우',
        '조영진',
        '황찬희',
        '이성호',
        '임지민',
        '강대희',
        '조윤장']
member.sort()
attendance = []
for i in member:
    attendance.append(False)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def 도움말(ctx):
    await ctx.send('!출석 이름\t-출결 상태를 출석으로 바꿉니다\n!출석확인\t-결석자 수와 출결현황을 확인합니다\n!총원확인\t-총원을 확인합니다\n!출석초기화\t-출결현황을 초기화합니다(회의가 시작하거나 끝났을 때 입력)')

@bot.command()
async def 출석(ctx, arg):
    if arg in member:
        attendance[member.index(arg)] = True
        await ctx.send(f"{arg} 출석")
    else:
        await ctx.send(f"{arg} 님은 출석부에 등록되지 않았습니다")
    
@bot.command()
async def 출석확인(ctx):
    await ctx.send(f"총원 {len(member)}명")
    await ctx.send(f"출석인원 {attendance.count(True)}명")
    await ctx.send(f"부재인원 {attendance.count(False)}명")
    for i in range(len(member)):
        if attendance[i] == False:
            await ctx.send(f"{member[i]} 결석")
            
@bot.command()
async def 총원확인(ctx):
    for i in member:
        await ctx.send(f'{i}')

@bot.command()
async def 출석초기화(ctx):
    for i in range (len(attendance)):
        attendance[i] = False
    await ctx.send('출석목록 초기화')
bot.run('NzQwNTAyNjY5ODM5NTY0ODQw.Xyp82g.SyO8loGlVzhDAKWj3lTTS1PGk2c')
