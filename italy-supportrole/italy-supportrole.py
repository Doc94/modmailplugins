import discord
from discord import Embed, Guild, Member, Role
from discord.ext import commands
from discord.ext.commands import Bot, Cog, Context, Greedy, group
from discord.utils import get

class SupportRoleManagent(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)

    @commands.command()
    @commands.has_any_role(659513332218331155, 676408167063879715)
    async def givesupport(self, ctx: Context, user: discord.Member):
        role = get(user.guild.roles, id=683333884871573534)
        await ctx.send("its gone?")
        await user.add_roles(role)
        await ctx.send(f"hey {ctx.author.name}, {user.name} has been giving a role called: {role.name}")

    @commands.command()
    @commands.has_any_role(659513332218331155, 676408167063879715)
    async def removesupport(self, ctx: Context, user: discord.Member):
        role = get(user.guild.roles, id=683333884871573534)
        await ctx.send("nah")
        await user.remove_roles(role)
        await ctx.send(f"hey {ctx.author.name}, {user.name} has been remove of a role called: {role.name}")



def setup(bot):
    bot.add_cog(SupportRoleManagent(bot))
